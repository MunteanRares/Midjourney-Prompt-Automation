import random

class CreatingPrompts:
    def __init__(self, json, image_type, pixel, sref_yes_no, sref, nr_images, artist_yes_no, artist_name, threed, text_in_image):
        self.prompt_list = []
        self.json = json
        self.sref = sref
        self.sref_yes_no = sref_yes_no
        self.pixel = pixel
        self.image_type = image_type
        self.nr_prompts = nr_images
        self.artist_name = artist_name
        self.threed = threed
        self.artist_yes_no = artist_yes_no
        self.text_in_image = text_in_image

        if self.text_in_image:
            self.add_text_to_image = f', "{self.text_in_image}"'
        else:
            self.add_text_to_image = ""

        if self.artist_yes_no:
            self.prompt_edit1 = f" in the style of {artist_name}"
        elif not self.artist_yes_no:
            self.prompt_edit1 = ""

        if self.sref_yes_no:
            self.prompt_edit = f" --sref {sref} --sw 45"
        elif not self.sref_yes_no:
            self.prompt_edit = ""

        if self.image_type == 1 or self.image_type == 4:
            self.prompt_start = f"/imagine prompt: stock photography, professional shot, natural lighting,{self.prompt_edit1} "
            # self.prompt_start = f"/imagine prompt: stock photography, natural lighting,{self.prompt_edit1} "
        elif self.image_type == 2 and self.pixel == 0 and threed == False:
            self.prompt_start = f"/imagine prompt: digital made, simple,{self.prompt_edit1} "
        elif self.image_type == 2 and self.pixel == 0 and threed == True:
            self.prompt_start = f"/imagine prompt: 3D render, minimalist, simple,{self.prompt_edit1} "
        elif self.image_type == 2 and self.pixel == 1:
            self.prompt_start = f"/imagine prompt: 2d, pixelart, flat art, parallax background,{self.prompt_edit1} "
        elif self.image_type == 3:
            self.prompt_start = f"/imagine prompt: vector, simple bold vector,{self.prompt_edit1} "

    def create_prompt(self):
        for _ in range(0, self.nr_prompts):
            key_list = []
            title_init = self.json["files"][random.randint(0, 99)]["title"].lower()
            title_final = title_init.replace(".", "").replace("generative", "").replace("generated", "").replace(" ai",
                                                                                                                 "")
            for _ in range(0, 4):
                try:
                    key_init = self.json["files"][random.randint(0, 10)]["keywords"][0]["name"].lower()
                except IndexError:
                    continue
                if key_init not in key_list:
                    key_list.append(key_init)
            self.prompt_list.append(f"{self.prompt_start}{title_final}, {key_list[0]}{self.add_text_to_image} --ar 3:2{self.prompt_edit} --s 200 --c 20")
        # print(self.prompt_list)
        # print(len(self.prompt_list))
        return self.prompt_list
