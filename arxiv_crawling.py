import subprocess
import os
import tarfile
import tempfile
import shutil
import concurrent.futures

from bs4 import BeautifulSoup
import PyPDF2
import requests


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdffile:
        reader = PyPDF2.PdfReader(pdffile)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_text_from_gz(file_path):
    # Extract the .tex files from the gzipped archive
    temp_dir = tempfile.mkdtemp()
    tex_files = []

    with tarfile.open(file_path, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.name.endswith('.tex'):
                tex_file_path = os.path.join(temp_dir, member.name)
                tar.extract(member, path=temp_dir)
                tex_files.append(tex_file_path)

    if not tex_files:
        raise ValueError("No .tex files found in the archive.")

    # Use opendetex to extract the text from the .tex files
    try:
        text = extract_text_from_tex(tex_files)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise RuntimeError("Failed to extract text using opendetex.") from e
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

    return text


def extract_text_from_tex(tex_files):
    # Determine the order of priority for tex files
    priority_files = ['ms.tex', 'main.tex']

    # Find the first file in the priority list that exists in tex_files
    tex_file = next((file for file in priority_files if file in tex_files), None)

    # If no priority file is found, use the first file in tex_files
    if tex_file is None:
        tex_file = tex_files[0]

    # Use opendetex to extract the text from the chosen .tex file
    process = subprocess.Popen(['opendetex', '-sr', tex_file], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    text = output.decode('utf-8')

    return text



def extract_text_from_tar(file_name):
    # Use tar and opendetex to extract the text from the .tar file
    process1 = subprocess.Popen(['tar', 'xf', file_name, '--to-stdout'], stdout=subprocess.PIPE)
    process2 = subprocess.Popen(['opendetex', '-sr'], stdin=process1.stdout, stdout=subprocess.PIPE)
    process1.stdout.close()

    output, _ = process2.communicate()

    return output.decode('utf-8')



def get_file_type(file_name):
    try:
        result = subprocess.run(['file', '-b', '--mime-type', file_name], capture_output=True, text=True)
        file_type = result.stdout.strip().lower()

        if 'gzip' in file_type:
            return 'gzip'
        elif 'pdf' in file_type:
            return 'pdf'
        elif 'empty' in file_type:
            return 'empty'
        else:
            return None
    except subprocess.SubprocessError:
        return None


def download_file(url):
    paper_id = url.split('/')[-1].split('v')[0]
    source_url = f"https://arxiv.org/e-print/{paper_id}"

    response = requests.get(source_url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return file_name


def cleanup_temp_files(file_name):
    os.remove(file_name)


def process_arxiv_paper(url):
    try:
        # Download the file
        file_path = download_file(url)
        if not file_path:
            return None

        # Determine the file type based on the downloaded file
        file_type = get_file_type(file_path)

        if file_type == 'pdf':
            # Extract text from the PDF file
            text = extract_text_from_pdf(file_path)

        elif file_type == 'gzip':
            # Extract text from the gzip file
            text = extract_text_from_gz(file_path)

        else:
            print('other case')
            text = ''

        text = clean_text(text)

        # Extract paper title and abstract from arXiv webpage
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paper_title = soup.find('h1', class_='title').text.strip()
        paper_abstract = soup.find('blockquote', class_='abstract mathjax').text.strip()

        # Clean up the downloaded file
        cleanup_temp_files(file_path)

        return paper_title, paper_abstract, text

    except Exception as e:
        print(f"Error processing URL: {url}")
        print(str(e))
        return None


def clean_text(text):
    text.replace('\n', '')
    text = ' '.join([line.strip() for line in text.splitlines() if line.strip()])
    return text


def process_single_arxiv_paper(url):
    processed_paper = process_arxiv_paper(url)
    if processed_paper:
        title, abstract, text = processed_paper
        output_dict = {'title': title, 'abstract': abstract, 'text': text}
        return output_dict
    return {'title': '', 'abstract': '', 'text': ''}


# Read the URLs from the file
with open("sources/urls_arxiv.txt", "r") as file:
    urls = [url.strip() for url in file.readlines()]

# Process the arXiv papers using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the tasks to the executor
    futures = [executor.submit(process_single_arxiv_paper, url) for url in urls]

    # Collect the results as they become available
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            print(result)
