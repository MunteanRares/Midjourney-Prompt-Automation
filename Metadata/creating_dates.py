from random import choice, randint
from Metadata.image_data import ImageStoredData


CATEGORIES = ["0", "Animals", "Buildings and Architecture", "Business", "Drinks", "The Environment", "States of Mind",
              "Food", "Graphic Resources", "Hobbies and Leisure", "Industry", "Landscapes", "Lifestyle", "People",
              "Plants and Flowers", "Culture and Religion", "Science", "Social Issues", "Sports", "Technology",
              "Transport", "Travel"]


class CreatingDates:
    def __init__(self, images):
        self.images = images

    def take_data_from_json_for_image_data(self):
        # ADD HERE FOR OTHER CSV SITES ================================
        #DREAMSTIME:
        title_dreamstime = []
        titlelist_dreamstime = []
        #FREEPIK:
        freepik_title = []
        titlelist_freepik = []
        #ADOBE:
        title = []
        title_list = []
        keywords = []
        keyword_list = []
        for image in self.images:
            for keyword in image["keywords"]:
                if keyword["name"] not in keyword_list and keyword["name"].count("-") == 0:
                    keyword_list.append(keyword["name"])

        for number in range(1, 50):
            keywords.append(choice(keyword_list))
        the_49_keywords = ", ".join(keywords)

        category = self.images[randint(3, 6)]["category_hierarchy"][0]["name"]
        category_id = CATEGORIES.index(category)

        for image in self.images:
            if len(image["title"]) < 136 and image["title"].count(":") == 0 and image["title"].count("-"):
                title_list.append(image["title"])
        title.append(choice(title_list))
        title_adobe = "".join(title)

# ADD HERE FOR OTHER CSV SITES ================================

        for image in self.images:
            if len(image["title"]) < 101 and image["title"].count(":") == 0 and image["title"].count("-"):
                titlelist_freepik.append(image["title"])
        freepik_title.append(choice(titlelist_freepik))
        title_freepik = "".join(freepik_title)


        for image in self.images:
            if len(image["title"]) < 131 and image["title"].count(":") == 0 and image["title"].count("-"):
                titlelist_dreamstime.append(image["title"])
        title_dreamstime.append(choice(titlelist_dreamstime))
        dreamstime_title = "".join(title_dreamstime)


        image_data = ImageStoredData(
            keywords=the_49_keywords,
            category=category_id,
            title=f"{title_adobe}. Beautiful simple AI generated image",
            dreamstime_title=f"{dreamstime_title}",
# ADD HERE FOR OTHER CSV SITES ===============================
            title_freepik=f"{title_freepik}",
        )

        return image_data
