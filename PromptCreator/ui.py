import asyncio
import pprint
import random
import os
from PromptCreator.GenerateUrlFolder.GenerateUrl import GenerateUrl
from PromptCreator.request_files import Request
from PromptCreator.creating_prompts import CreatingPrompts
from playwright.async_api import async_playwright
from tkinter import *
from Metadata.LetsTryTKinter import AdobeAutomationUI

THEME_1 = "#35374B"
THEME_2 = "#344955"
THEME_3 = "#50727B"
THEME_4 = "#78A083"
TIMEOUT_BETWEEN_12_PROMPTS = 960000
FONT = "white"


class Ui:
    def __init__(self):
        #### Def Variables
        self.added_photos = 0
        self.prompt_dict = {}

        #### Window Settings
        self.window = Tk()
        self.window.geometry("800x450+100+300")
        self.window.title("Auto Prompts ;D")
        self.window.config(padx=20, pady=20, background=THEME_3)

        #### When Initiated - Request Photos For List
        self.generateUrlObj = GenerateUrl()
        self.generateUrlObj.request_new_photos()

        #### Open Both Windows With Interface
        self.open_metadataWindow()
        self.window_interface()



    def window_interface(self):
        #### Label 1
        self.label1 = Label(text="Number of prompts (required): ", font=("Bahnschrift SemiBold", 12, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label1.grid(column=0, row=0, stick=W, columnspan=2, pady=4)
        #### Entry 1
        self.nr_prompts = Entry(width=56, background=THEME_1, foreground=FONT, insertbackground=FONT,
                                font=("Bahnschrift SemiBold", 12, "normal"))
        self.nr_prompts.grid(column=0, row=0, stick=E, columnspan=2, pady=4)
        self.nr_prompts.insert(string="11", index=0)


        #### Label 2
        self.label2 = Label(text="Enter keywords separated by a space (required): ",
                            font=("Bahnschrift SemiBold", 13, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label2.grid(column=0, row=1, pady=4)
        #### Entry 2
        self.words = Entry(width=40, background=THEME_1, foreground=FONT, insertbackground=FONT,
                           font=("Bahnschrift SemiBold", 12, "normal"))
        self.words.grid(column=1, row=1, pady=4)


        #### Label 3
        self.label3 = Label(text="Enter URL for reference (required): ", font=("Bahnschrift SemiBold", 12, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label3.grid(column=0, row=2, stick=W, columnspan=2, pady=4)
        #### Entry 2
        self.url = Entry(width=52, background=THEME_1, foreground=FONT, insertbackground=FONT,
                         font=("Bahnschrift SemiBold", 12, "normal"))
        self.url.grid(column=0, row=2, stick=E, columnspan=2, pady=4)


        #### Label 4
        self.label4 = Label(text="Choose media type: ", font=("Bahnschrift SemiBold", 12, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label4.grid(column=0, row=3, stick=W, columnspan=2, pady=4)
        #### Entry 4
        self.media_options = ["Photos", "Illustrations", "Vector", "Videos", "Pixel"]
        self.variable = StringVar(self.window)
        self.variable.set(self.media_options[0])
        self.image_type = OptionMenu(self.window, self.variable, "Illustrations", "Vectors", "Photos", "Videos",
                                     "Pixel")
        self.image_type.config(highlightthickness=0, background=THEME_4,
                               font=("Bahnschrift Bold", 9, "normal"), foreground=THEME_1, width=78,
                               activebackground=FONT)
        self.image_type.grid(column=0, row=3, columnspan=2, stick=E, pady=4)


        #### Label 5
        self.sref = Label(text="Sref (optional): ", font=("Bahnschrift SemiBold", 12, "normal"),
                          background=THEME_3, foreground=FONT)
        self.sref.grid(column=0, row=4, columnspan=2, stick=W, pady=4)
        #### Entry 5
        self.srefentry = Entry(width=68, background=THEME_1, foreground=FONT, insertbackground=FONT,
                               font=("Bahnschrift SemiBold", 12, "normal"))
        self.srefentry.grid(column=0, row=4, stick=E, columnspan=2, pady=4)


        #### Label 6
        self.label6 = Label(text="Enter an artist name (optional): ", font=("Bahnschrift SemiBold", 12, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label6.grid(column=0, row=5, stick=W, columnspan=2, pady=4)
        #### Entry 6
        self.artist = Entry(width=56, background=THEME_1, foreground=FONT, insertbackground=FONT,
                            font=("Bahnschrift SemiBold", 12, "normal"))
        self.artist.grid(column=0, row=5, stick=E, columnspan=2, pady=4)


        #### Label 7
        self.label7 = Label(text="3D: ", font=("Bahnschrift SemiBold", 12, "normal"),
                            background=THEME_3, foreground=FONT)
        self.label7.grid(column=0, row=7, stick=W, columnspan=2, pady=4)
        #### Entry 7
        self.tred_options = ["Yes", "No"]
        self.variables = StringVar(self.window)
        self.variables.set(self.tred_options[1])
        self.three = OptionMenu(self.window, self.variables, "Yes", "No")
        self.three.config(highlightthickness=0, background=THEME_4,
                          font=("Bahnschrift Bold", 9, "normal"), foreground=THEME_1, width=78,
                          activebackground=FONT)
        self.three.grid(column=0, row=7, columnspan=2, stick=E, pady=4)


        #### Label 8
        self.text_prompt = Label(text="Write in img (optional): ", font=("Bahnschrift SemiBold", 12, "normal"),
                                 background=THEME_3, foreground=FONT)
        self.text_prompt.grid(column=0, row=6, stick=W, columnspan=2, pady=4)
        #### Entry 8
        self.text_prompt_entr = Entry(width=56, background=THEME_1, foreground=FONT, insertbackground=FONT,
                                      font=("Bahnschrift SemiBold", 12, "normal"))
        self.text_prompt_entr.grid(column=0, row=6, stick=E, columnspan=2, pady=4)


        #### Create Images Button
        self.create_images = Button(text="Create Images!", font=("Bahnschrift Bold", 12, "normal"), background=THEME_4,
                                    foreground=THEME_1, activebackground=THEME_2, activeforeground=FONT,
                                    command=self.create_in_discord)
        self.create_images.grid(column=0, row=8, pady=8, columnspan=1)


        #### Nr Of Images Label:
        self.nr_of_imgs = Label(text=f"Nr Of Imgs Added: 0 ", font=("Bahnschrift SemiBold", 12, "normal"),
                                background=THEME_3, foreground=FONT)
        self.nr_of_imgs.grid(column=0, row=8, columnspan=2)


        #### Add Images Button
        self.add_image = Button(text="Add Image", font=("Bahnschrift Bold", 12, "normal"), background=THEME_4,
                                foreground=THEME_1, activebackground=THEME_2, activeforeground=FONT,
                                command=self.add_images)
        self.add_image.grid(column=1, row=8, pady=8, columnspan=2)


        #### Generate Url Button
        self.generateUrlButton = Button(text="Generate Url", font=("Bahnschrift Bold", 12, "normal"),
                                        background=THEME_4,
                                        foreground=THEME_1, activebackground=THEME_2, activeforeground=FONT,
                                        command=lambda:[self.generateUrlObj.generate_url_keyword(),
                                                        self.fill_url(),
                                                        self.metadata_window_app.fill_url_from_generateurl(),
                                                        self.metadata_window_app.get_input()])
        self.generateUrlButton.grid(column=0, row=9, pady=9, columnspan=3)


        #### KEEP WIDNDOW OPEN BWEI
        self.window.mainloop()


    def fill_url(self):
        self.words.delete(0, END)
        self.url.delete(0, END)
        self.srefentry.delete(0, END)
        self.artist.delete(0, END)
        self.text_prompt_entr.delete(0, END)

        self.url.insert(string=self.generateUrlObj.url, index=0)
        self.words.insert(string=self.generateUrlObj.keyword, index=0)
        self.srefentry.insert(string=self.generateUrlObj.url, index=0)


    def add_images(self):
        #### Getting data from entries
        trd = False
        word = self.words.get()
        url = self.url.get()
        media = self.variable.get()
        sref = self.srefentry.get()
        artist_yes_no = self.artist.get()
        number_prompts = int(self.nr_prompts.get())
        threed = self.variables.get()
        the_text = self.text_prompt_entr.get()

        if the_text == "":
            text_in_image = ""
        else:
            text_in_image = the_text

        if threed == "Yes":
            trd = True
        elif threed == "No":
            trd = False

        if artist_yes_no == "":
            artist = False
        else:
            artist = True

        if sref == "":
            sref_yes_no = False
        else:
            sref_yes_no = True

        #### Ifs
        mediaid = 0
        pixel_yes_no = 0
        if media == "Pixel":
            pixel_yes_no = 1
        if media == "Photos":
            mediaid = 1
        elif media == "Illustrations" or media == "Pixel":
            mediaid = 2
        elif media == "Vectors":
            mediaid = 3
        elif media == "Videos":
            mediaid = 4

        #### REQUESTS + CREATING PROMPTS
        response = Request(words=word, url=url, media=mediaid)
        json = response.get_json()
        create = CreatingPrompts(json=json, image_type=mediaid, pixel=pixel_yes_no, sref_yes_no=sref_yes_no, sref=sref,
                                 nr_images=number_prompts, artist_yes_no=artist, artist_name=artist_yes_no, threed=trd,
                                 text_in_image=text_in_image)
        prompt_list = create.create_prompt()
        self.added_photos += 1
        self.prompt_dict[f"prompt_list{self.added_photos}"] = prompt_list
        self.nr_of_imgs.config(text=f"Nr of imgs added : {self.added_photos}")

        #### print(prompt_list)
        pprint.pp(self.prompt_dict)
        self.words.delete(0, END)
        self.url.delete(0, END)
        self.srefentry.delete(0, END)
        self.artist.delete(0, END)
        self.text_prompt_entr.delete(0, END)


    #### Starts Discord With the Added Images Prompts
    def create_in_discord(self):
        #### BROWSING AND ADDING PROMPTS INTO DISC

        password = os.environ["DISC_PAS"]
        pprint.pp(len(self.prompt_dict))

        async def main():
            async with async_playwright() as playwright:
                browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
                user_agent_strings = [
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.60"
                    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2227.0 Safari/537.36',
                    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3497.92 Safari/537.36',
                    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/89.0.0.0",
                    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
                    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.0.0",
                    # "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
                    # "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                    # "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                    # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.0.0",
                    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
                    # "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
                    # "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                    # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                    # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/87.0.0.0",
                    # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Vivaldi/4.3.2439.56"
                ]
                user_agent = random.choice(user_agent_strings)
                context = await browser.new_context(user_agent=user_agent)
                midj_tab = await context.new_page()
                await midj_tab.add_init_script("""
                navigator.webdriver = false
                Object.defineProperty(navigator, 'webdriver', {
                get: () => false
                })
                """
                                               )
                await midj_tab.goto("https://discord.com/channels/@me/1046140247618109500")
                await midj_tab.wait_for_timeout(4453)
                await midj_tab.locator("#uid_7").fill(os.environ["DISC_MAIL"])
                await midj_tab.wait_for_timeout(4230)
                await midj_tab.locator("#uid_9").fill(password)
                await midj_tab.get_by_role("button", name="Log In").click()
                await midj_tab.goto("https://discord.com/channels/@me/1046140247618109500")

                for num_of_prompt_list in range(1, len(self.prompt_dict) + 1):
                    for _ in range(0, 4):
                        for num in range(0, len(self.prompt_dict[f"prompt_list{num_of_prompt_list}"])):
                            await midj_tab.wait_for_timeout(3752)
                            await midj_tab.get_by_role("textbox", name="Message @Midjourney Bot").fill(self.prompt_dict[f"prompt_list{num_of_prompt_list}"][num])
                            await midj_tab.get_by_role("textbox", name="Message @Midjourney Bot").press("Enter")
                        await midj_tab.wait_for_timeout(TIMEOUT_BETWEEN_12_PROMPTS)

                await browser.close()

        asyncio.run(main())


    #### Open Metadata Window
    def open_metadataWindow(self):
        self.metadata_window_app = AdobeAutomationUI(self.generateUrlObj)