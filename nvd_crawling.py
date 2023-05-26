import requests
from bs4 import BeautifulSoup
import json

# read CVE ids from the text file
with open('sources/ids_nvd.txt', 'r') as file:
    cve_ids = [line.strip() for line in file]

# initialize an empty list to store CVE ids and their descriptions
cve_data =  []

for cve_id in cve_ids:
    # make a GET request to the NVD API
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/{cve_id}"
    response = requests.get(url)
    
    # if the request is successful
    if response.status_code == 200:
        # load the JSON data from the response
        data = json.loads(response.text)
        
        # extract the description from the JSON data
        description = data['result']['CVE_Items'][0]['cve']['description']['description_data'][0]['value']
        
        # add the CVE id and its description to the dictionary
        cve_data += description

# Save the cves to a file
with open('sources/cves.txt', 'w') as f:
    for cve in cve_data:
        f.write("%s\n" % cve)
