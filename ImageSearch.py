import requests
import key
import random
import datetime



def search ():
    api_key = key.google_api_key
    search_engine_id= key.google_search_engine_key
    # define search params:
    query = "Pikachu"
    num = 1
    start = random.randrange(1,200)
    date_before = int(str(datetime.datetime.now().year-random.randrange(0,2))+str('{:02d}'.format(datetime.datetime.now().month))+str('{:02d}'.format(datetime.datetime.now().day)))
    date_after = date_before-10000
    
    custom_search_url = f'https://customsearch.googleapis.com/customsearch/v1?cx={search_engine_id}&num={num}&q={query}&searchType=image&key={api_key}&start={start}&sort=date:r:{date_after}:{date_before}'

    # fetch the json response and item array
    data = requests.get(custom_search_url).json()
    search_item = data.get("items")

    for i, get_link in enumerate (search_item):
        link = get_link.get("link")

    return link
