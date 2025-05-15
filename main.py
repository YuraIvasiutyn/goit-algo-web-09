from scrapyng.scrapy_site import get_full_data_and_dump_to_json
from crud.load_data import insert_authors, insert_quotes

url = "http://quotes.toscrape.com/"

if __name__ == "__main__":
    get_full_data_and_dump_to_json(url)
    insert_authors()
    insert_quotes()
