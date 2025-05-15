import requests
import json
import re
from bs4 import BeautifulSoup


def get_full_data_and_dump_to_json(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    quotes_list = []
    authors_list = []

    for i in range(0, len(quotes)):
        tagsforquote = tags[i].find_all('a', class_='tag')
        tags_text = [tag.text for tag in tagsforquote]
        data_dict = {
            "tags": tags_text,
            "author": authors[i].text,
            "quote": quotes[i].text
        }
        quotes_list.append(data_dict)

        authors_data = get_author_info(url, authors[i].text)
        authors_list.append(authors_data)

    with open('json/quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes_list, f, ensure_ascii=False, indent=4)

    with open('json/authors.json', 'w', encoding='utf-8') as f:
        json.dump(authors_list, f, ensure_ascii=False, indent=4)


def get_author_info(url, author):
    url_part = re.sub(r"[.\s]+", "-", author)
    new_url = url + 'author/' + url_part

    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, "html.parser")

    fullname = soup.find('h3', class_='author-title')
    born_date = soup.find('span', class_='author-born-date')
    born_location = soup.find('span', class_='author-born-location')
    description = soup.find('div', class_='author-description')

    result = {
        "fullname": fullname.text,
        "born_date": born_date.text,
        "born_location": born_location.text,
        "description": description.text.strip()
    }

    return result


