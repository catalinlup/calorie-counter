import urllib
import os
from bs4 import BeautifulSoup

ALBERT_HEIJN_BASE_URL = 'https://www.ah.nl/producten/product/'

def create_full_url(product_id: str) -> str:
    """
    Creates the full url to make a request to AH website.
    """
    return os.path.join(ALBERT_HEIJN_BASE_URL, product_id)

def make_request(url: str) -> str:
    request = urllib.request.urlopen(url)
    return request.read()


def parse_table_entry(table_entry) -> list:
    """
    Parses the table entries into numerical values, adding the measurement unit as a field name
    """

    if table_entry[0] == 'Energie':
        start_index = table_entry[1].find('(') + 1
        end_index = table_entry[1].find('kcal)') - 1
        return ['Energie [kcal]', float(table_entry[1][start_index : end_index])]
    
    return [f'{table_entry[0]} [g]', float(table_entry[1][:table_entry[1].find('g') - 1])]

def convert_table_to_dict(table) -> dict:
    # extract table data as a list of lists
    table_data = [[cell.text for cell in row("td")]
                         for row in table("tr")]
    # get rid of empty lists
    table_data = list(filter(lambda x: len(x) > 0, table_data))

    # parse the data to numerical values
    table_data = list(map(parse_table_entry, table_data))

    return dict(table_data)

def extract_nutri_table_from_html(html_data: str) -> dict:
    """
    Given a html product page, extracts the nutritional data as a python dictionary.
    If no data was found, returns an empty dictionary.
    """
    soup = BeautifulSoup(html_data, 'html.parser')

    tables = soup.find_all('table', {'class': lambda s: 'product-info-nutrition' in s})

    if len(tables) == 0:
        return {}
    
    # extract table
    table = tables[0]

    return convert_table_to_dict(table)


def get_albert_heijn_product_nutri_data(product_id: str) -> dict:
    """
    Returns nutri data about the albert heijn product based on its id.
    """
    return extract_nutri_table_from_html(make_request(create_full_url(product_id)))


print(get_albert_heijn_product_nutri_data('wi123864'))

