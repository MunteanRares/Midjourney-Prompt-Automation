
ImageMetaDataAdobe = {
            "Filename": [],
            "Title": [],
            "Keywords": [],
            "Category": [],
        }

# ADD HERE FOR OTHER CSV SITES ================================


ImageMetaDataFreepik = {
            "Filename": [],
            "Title": [],
            "Keywords": [],
            "Prompt": [],
            "Model": [],
        }

class CreateDataFrame:
    def __init__(self, keywords, title, category, image_extension, file_names):
        self.keywords = keywords
        self.title = title
        self.category = category
        self.image_extension = image_extension
        self.file_names = file_names

    def add_data_to_dataframe(self, amount_of_times):
        ImageMetaDataAdobe["Filename"].append(f"{self.file_names} ({amount_of_times}).{self.image_extension}")
        ImageMetaDataAdobe["Title"].append(self.title)
        ImageMetaDataAdobe["Keywords"].append(self.keywords)
        ImageMetaDataAdobe["Category"].append(self.category)
        return ImageMetaDataAdobe

    def deletes_data_from_dataframe(self):
        ImageMetaDataAdobe["Filename"].clear()
        ImageMetaDataAdobe["Title"].clear()
        ImageMetaDataAdobe["Keywords"].clear()
        ImageMetaDataAdobe["Category"].clear()
        return ImageMetaDataAdobe

# ADD HERE CLASS FOR OTHER CSV SITES ================================
class CreateDataFrame_FREEPIK:
    def __init__(self, title, keywords, prompt, model, image_extension, file_names):
        self.title = title
        self.keywords = keywords
        self.prompt = prompt
        self.model = model
        self.image_extension = image_extension
        self.file_names = file_names

    def add_data_to_dataframe(self, amount_of_times):
        ImageMetaDataFreepik["Filename"].append(f"{self.file_names} -{amount_of_times}.{self.image_extension}")
        ImageMetaDataFreepik["Title"].append(self.title)
        ImageMetaDataFreepik["Keywords"].append(self.keywords)
        ImageMetaDataFreepik["Prompt"].append(self.prompt)
        ImageMetaDataFreepik["Model"].append(self.model)
        return ImageMetaDataFreepik

    def deletes_data_from_dataframe(self):
        ImageMetaDataFreepik["Filename"].clear()
        ImageMetaDataFreepik["Title"].clear()
        ImageMetaDataFreepik["Keywords"].clear()
        ImageMetaDataFreepik["Prompt"].clear()
        ImageMetaDataFreepik["Model"].clear()
        return ImageMetaDataFreepik
