import requests
from PromptCreator.GenerateUrlFolder.Functions import *

######## NEVER CHANGING ########
ADOBE_STOCK_API = "https://stock.adobe.io/Rest/Media/1/Search/Files"
API_KEY = "c91e300504994550b8210591d4df4d3b"
HEADER = {
    "x-api-key": API_KEY,
    "X-product": "Love"
}
ORDER = ["relevance", "creation", "featured", "nb_downloads", "undiscovered"]

######## GENERATE URL CLASS ########
class GenerateUrl:
    ######## VARIABLES INSIDE CLASS ########
    def __init__(self):
        self.url_index = 0
        self.this_session_photos = []
        self.url = ""
        self.keyword = ""
        self.keyword_filenames = ""
        self.found_photos = {}

    ######## METHODS ########
    def request_new_photos(self):
        parameters = {
            "search_parameters[limit]": 100,
            "search_parameters[offset]": read_offset(),
            "search_parameters[order]": ORDER[2],
            "search_parameters[filters][gentech]": "false",
            "search_parameters[filters][content_type:photo]": 1,
            "search_parameters[filters][content_type:illustration]": 0,
            "search_parameters[filters][content_type:vector]": 0,
            "search_parameters[filters][content_type:video]": 0,
            "search_parameters[filters][content_type:template]": 0,
            "search_parameters[filters][content_type:3d]": 0,
            "result_columns[]": ["keywords", "thumbnail_url"]
        }
        # REQUEST #
        request = requests.get(ADOBE_STOCK_API, params=parameters, headers=HEADER)
        self.found_photos = request.json()
        print(self.found_photos)
        for photos in self.found_photos["files"]:
            self.this_session_photos.append(photos["thumbnail_url"])


    def generate_url_keyword(self):
        photo_url = self.this_session_photos[self.url_index]

        while is_url_in_data(photo_url):
            self.url_index += 1

            if self.url_index > len(self.this_session_photos) - 2:
                self.url_index = 0
                current_offset = int(read_offset()) + 100

                with open("PromptCreator/data/offset.txt", "w") as offset_data:
                    offset_data.write(str(current_offset))
                self.this_session_photos = []
                self.request_new_photos()
            photo_url = self.this_session_photos[self.url_index]

        self.keyword = self.found_photos["files"][self.url_index]["keywords"][0]["name"]
        self.keyword_filenames = f"{self.found_photos['files'][self.url_index]['keywords'][0]['name']} {self.found_photos['files'][self.url_index]['keywords'][1]['name']}"
        print(self.keyword)
        self.url = photo_url
        with open("PromptCreator/data/used_photos_url.csv", "a") as data:
            data.write(photo_url + "\n")
