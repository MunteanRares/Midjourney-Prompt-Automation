import requests
from random import randint
import os

# =============================== AUTH =============================== #

# API_KEY = os.environ.get("adobe_stock_api")
HEADER = {
    "x-api-key": "c91e300504994550b8210591d4df4d3b",
    "x-product": ":)"
}

# =============================== DETAILS =============================== #

ADOBE_ENDPOINT = "https://stock.adobe.io/Rest/Media/1/Search/Files"
PAGE_NUMBER = randint(1, 20)
CATEGORIES = ["0", "Animals", "Buildings and Arhitecture", "Business", "Drinks", "The Environment", "States of Mind",
              "Food", "Graphic Resources", "Hobbies and Leisure", "Industry", "Landscapes", "Lifestyle", "People",
              "Plants and Flowers", "Culture and Religion", "Science", "Social Issues", "Sports", "Technology",
              "Transport", "Travel"]


class GetData:
    def __init__(self, similar_url, words, media):
        self.similar_url = similar_url
        self.words = words
        self.media = media

    def images(self):

        parameters = {
            "search_parameters[words]": self.words,
            "locale": "en_US",
            "search_parameters[limit]": 100,
            "search_parameters[order]": "relevance",
            "search_parameters[offset]": PAGE_NUMBER,
            "search_parameters[similar_url]": self.similar_url,
            "result_columns[]": ["id", "title", "keywords", "thumbnail_html_tag", "category", "category_hierarchy", "nb_results"],
            "search_parameters[filters][content_type:video]": 0,
            "media_type_id": self.media,
        }

        response = requests.get(ADOBE_ENDPOINT, headers=HEADER, params=parameters)
        file_data = response.json()
        # print(response.json())
        images = file_data["files"]
        # print(response.json())
        return images
