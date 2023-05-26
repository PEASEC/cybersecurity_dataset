import trafilatura


urls = open('sources/urls_web.txt').read().split()

for url in urls:
    content = trafilatura.fetch_url(url)
    text = trafilatura.extract(content, output_format='json', include_comments=False)
    print(text)
