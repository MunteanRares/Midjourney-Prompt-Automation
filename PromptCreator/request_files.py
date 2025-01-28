import requests

ADOBE_ENDPOINT = "https://stock.adobe.io/Rest/Media/1/Search/Files"
HEADER = {
    "x-api-key": "c91e300504994550b8210591d4df4d3b",
    "x-Product": ":)"
}


class Request:

    def __init__(self, words, url, media):
        self.words = words
        self.url = url
        self.media = media

    def get_json(self):
        parameters = {
                "search_parameters[words]": self.words,
                "locale": "en_US",
                "search_parameters[limit]": 100,
                "search_parameters[order]": "relevance",
                "search_parameters[similar_url]": self.url,
                "result_columns[]": ["id", "title", "keywords", "thumbnail_html_tag", "category", "category_hierarchy", "nb_results"],
                "search_parameters[filters][content_type:video]": 0,
                "media_type_id": self.media,
                }

        response = requests.get(url=ADOBE_ENDPOINT, headers=HEADER, params=parameters)
        json = response.json()
        # print(json)
        return json
