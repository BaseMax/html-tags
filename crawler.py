import requests
from bs4 import BeautifulSoup
import json

target_url = "https://www.w3schools.com/tags/default.asp"

response = requests.get(target_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'ws-table-all notranslate'})
    
    result = []

    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 2:
            tag_element = cols[0].find('a')
            name = tag_element.text if tag_element else cols[0].text.strip()
            link = ("https://www.w3schools.com/tags/" + tag_element['href']) if tag_element else ""
            brief = cols[1].text.strip()

            if name and link:
                result.append({
                    "name": name,
                    "link": link,
                    "brief": brief
                })

    with open('html_tags.json', 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    print("JSON file 'html_tags.json' has been successfully created!")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
