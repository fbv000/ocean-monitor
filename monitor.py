import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4'])

from bs4 import BeautifulSoup
import requests

# URL of the dashboard page
url = 'https://ocean.xyz/stats/37SN2dyo9xWdJ3owHafLvUNLAPkexxXHZy.default'

# Fetch the page content
response = requests.get(url)
page_content = response.text

# Parse the HTML content
soup = BeautifulSoup(page_content, 'html.parser')

for row in soup.find_all('tr', class_='table-row'):
    # Assuming the worker's name is in the first td
    name_link = row.find('td', class_='hide-overflow')
    name = name_link.text.strip() if name_link else 'Unknown Worker'
    
    status_div = row.find('div', class_='status-online-text')
    # Check if status_div exists before accessing .text
    status = status_div.text.strip() if status_div else 'Offline'
    if name != "Unknown Worker" and name != "Total":   
        if status == 'Offline':
            print(f"{name} is currently offline.")
        else:
            print(f"{name} is online.")
