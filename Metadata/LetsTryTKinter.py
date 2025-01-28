import random
import pandas
from tkinter import *
from tkinter import messagebox
from Metadata.searchingmetadata import GetData
from Metadata.creating_dates import CreatingDates
from Metadata.creating_dataframe import CreateDataFrame
from Metadata.creating_dataframe import CreateDataFrame_FREEPIK


BACKGROUND_THEME = "#76ABAE"
FONT_COLOR = "#EEEEEE"
BACKGROUND_THEME_2 = "#31363F"
MIDJ_MODEL = "Midjourney 6"


class AdobeAutomationUI:
    def __init__(self, generatedobj_instance):
        ### WINDOW SETTINGS
        self.window = Toplevel()
        self.window.geometry("550x700+1100+100")
        self.window.title("Adobe stock Automation")
        self.window.config(background=BACKGROUND_THEME, pady=20, padx=20)
        self.generatedobj_instance = generatedobj_instance

        #### IMAGE REF
        self.icon = PhotoImage(file="Metadata/img/Icon.png")
        self.image = PhotoImage(file="Metadata/img/adobe-stock.png")

        #### WINDOW ICON
        self.window.iconphoto(False, self.icon)

        #### DISPLAY IMAGE
        self.canvas = Canvas(self.window, width=230, height=230, background=BACKGROUND_THEME, highlightthickness=0)
        self.canvas.create_image(115, 115, image=self.image)
        self.canvas.grid(column=1, row=1, padx=20, pady=20)

        ### DISPLAY WINDOW
        self.metadata_window_interface()



    def metadata_window_interface(self):
        # Top Label
        self.welcome = Label(self.window, text="Welcome to the Stock Contributor Automation!",
                             font=("Bahnschrift SemiBold", 17, "normal"),
                             background=BACKGROUND_THEME)
        self.welcome.grid(column=1, row=0)
        # Label under image
        self.complete_pls = Label(self.window, text="Complete the fields below:", font=("Bahnschrift SemiBold", 15, "normal"),
                                  background=BACKGROUND_THEME)
        self.complete_pls.grid(column=1, row=2)


        # Required Label
        self.required = Label(self.window,text="(fields that are marked with * are required)",
                              font=("Bahnschrift SemiBold", 11, "normal"),
                              background=BACKGROUND_THEME)
        self.required.grid(column=1, row=3)
        # For space
        self.space = Canvas(self.window, width=500, height=60,background=BACKGROUND_THEME, highlightthickness=0)
        self.space.grid(column=1, row=4, pady=10)


        # TextBox Label 1.
        self.text_box1 = Label(self.window, text="*Number of Images: ",
                               font=("Bahnschrift SemiBold", 13, "normal"),
                               background=BACKGROUND_THEME)
        self.text_box1.grid(column=0, row=5, stick=W, columnspan=2)
        # Entry1.
        self.nr_images = Entry(self.window, width=37, background=BACKGROUND_THEME_2, highlightcolor="black",
                               font=("Bahnschrift Bold", 12, "normal"), foreground=FONT_COLOR,
                               insertbackground=FONT_COLOR)
        self.nr_images.grid(column=0, row=5, columnspan=2, stick=E)
        self.nr_images.insert(string="400", index=0)


        # TextBox Label 2.
        self.text_box2 = Label(self.window, text="*Extension (jpg, png, mov4): ",
                               font=("Bahnschrift SemiBold", 13, "normal"),
                               background=BACKGROUND_THEME)
        self.text_box2.grid(column=0, row=6, stick=W, columnspan=2)
        # Entry2.
        self.extension = Entry(self.window, width=30, background=BACKGROUND_THEME_2, highlightcolor="black",
                               font=("Bahnschrift Bold", 12, "normal"), foreground=FONT_COLOR,
                               insertbackground=FONT_COLOR)
        self.extension.grid(column=0, row=6, columnspan=2, stick=E)
        self.extension.insert(string="JPEG", index=0)


        # FILE NAMES TEXT
        self.text_box3 = Label(self.window, text="*File Names: ",
                               font=("Bahnschrift SemiBold", 13, "normal"),
                               background=BACKGROUND_THEME)
        self.text_box3.grid(column=0, row=7, stick=W, columnspan=2)
        # FILE NAMES
        self.file_names = Entry(self.window, width=42, background=BACKGROUND_THEME_2, highlightcolor="black",
                               font=("Bahnschrift Bold", 12, "normal"), foreground=FONT_COLOR,
                               insertbackground=FONT_COLOR)
        self.file_names.grid(column=0, row=7, columnspan=2, stick=E)


        # TextBox Label 3.
        self.text_box4 = Label(self.window,text="*Similar Image URL:",
                               font=("Bahnschrift SemiBold", 13, "normal"),
                               background=BACKGROUND_THEME)
        self.text_box4.grid(column=0, row=8, stick=W, columnspan=2)
        self.text_box4.focus()
        # Entry3.
        self.similar = Entry(self.window, width=37, background=BACKGROUND_THEME_2, highlightcolor="black",
                             font=("Bahnschrift Bold", 12, "normal"), foreground=FONT_COLOR,
                             insertbackground=FONT_COLOR)
        self.similar.grid(column=0, row=8, columnspan=2, stick=E)


        # TextBox Label 4.
        self.text_box5 = Label(self.window, text="Add Keywords: ",
                               font=("Bahnschrift SemiBold", 13, "normal"),
                               background=BACKGROUND_THEME)
        self.text_box5.grid(column=0, row=9, stick=W, columnspan=2)
        # Entry4.
        self.keys = Entry(self.window, width=41, background=BACKGROUND_THEME_2, highlightcolor="black",
                          font=("Bahnschrift Bold", 12, "normal"), foreground=FONT_COLOR,
                          insertbackground=FONT_COLOR)
        self.keys.grid(column=0, row=9, columnspan=2, stick=E)


        # DropDown Text
        self.dropdown = Label(self.window, text="Choose the image type: ",
                              font=("Bahnschrift SemiBold", 13, "normal"),
                              background=BACKGROUND_THEME)
        self.dropdown.grid(column=0, row=10, stick=W, columnspan=2)
        # DropDown Menu
        options = ["Photos", "Illustrations", "Vector", "Videos"]
        self.variable = StringVar(self.window)
        self.variable.set(options[0])
        self.image_type = OptionMenu(self.window, self.variable, "Illustrations", "Vectors", "Photos", "Videos")
        self.image_type.config(highlightthickness=0, background=BACKGROUND_THEME_2,
                               font=("Bahnschrift Bold", 10, "normal"), foreground=FONT_COLOR, width=38,
                               activebackground=FONT_COLOR)
        self.image_type.grid(column=1, row=10, columnspan=2, stick=E)


        # Generate Button
        self.button = Button(self.window, text="Generate Metadata", font=("Bahnschrift Bold", 12, "normal"),
                             background=BACKGROUND_THEME_2, foreground=FONT_COLOR, command=self.get_input)
        self.button.grid(column=1, row=11, pady=20)


    def fill_url_from_generateurl(self):
        self.similar.delete(0, END)
        self.keys.delete(0, END)
        self.file_names.delete(0, END)
        self.file_names.focus()


        self.similar.insert(string=self.generatedobj_instance.url, index=0)
        self.keys.insert(string=self.generatedobj_instance.keyword, index=0)
        self.file_names.insert(string=self.generatedobj_instance.keyword_filenames, index=0)


    def get_input(self):
        extension = self.extension.get().lower()
        file_names = self.file_names.get().lower()
        model = MIDJ_MODEL
        keyword = self.keys.get()
        url = self.similar.get()
        nr_img = int(self.nr_images.get())
        image_type = self.variable.get()
        media = 0
        if image_type == "Photos":
            media = 1
        elif image_type == "Illustrations":
            media = 2
        elif image_type == "Vectors":
            media = 3
        elif image_type == "Videos":
            media = 4
        self.welcome.config(text="Your CSV file is getting ready...\nPlease don't close the window.")
        data_variants = []
    # try:
        frame_data_del = CreateDataFrame(keywords="", title="",
                                         category="",
                                         image_extension="", file_names="")
        frame_data_del.deletes_data_from_dataframe()


# ADD HERE FOR OTHER CSV SITES ================================
        frame_data_del_freepik = CreateDataFrame_FREEPIK(keywords="",
                                                         title="", prompt="",
                                                         image_extension="",
                                                         model="", file_names="")
        frame_data_del_freepik.deletes_data_from_dataframe()



        for _ in range(1, 10):
            data = GetData(url, keyword, media)
            json_file = data.images()
            data_variants.append(json_file)

        for num in range(1, nr_img + 1):
            pls = CreatingDates(random.choice(data_variants))
            image_data = pls.take_data_from_json_for_image_data()

            frame_data = CreateDataFrame(keywords=image_data.keywords, title=image_data.title,
                                         category=image_data.category,
                                         image_extension=extension, file_names=file_names)
            df = frame_data.add_data_to_dataframe(amount_of_times=num)

# ADD HERE FOR OTHER CSV SITES ================================


            frame_data_freepik = CreateDataFrame_FREEPIK(keywords=image_data.keywords, title=image_data.title_freepik,
                                                         prompt=image_data.title,
                                                         image_extension=extension, model=model, file_names=file_names)
            df_freepik = frame_data_freepik.add_data_to_dataframe(amount_of_times=num)

        # self.nr_images.delete(0, END)
        self.similar.delete(0, END)
        self.keys.delete(0, END)
        self.file_names.delete(0, END)
        self.welcome.config(text="Welcome to the Stock Contributor Automation!")
        self.nr_images.focus()

        dataf = pandas.DataFrame(df)
        if self.generatedobj_instance.keyword_filenames == "":
            dataf.to_csv(f"C:/Users/rares/Desktop/csv/adobe/{file_names}-adobe.csv", index=False)
        else:
            dataf.to_csv(f"C:/Users/rares/Desktop/csv/adobe/{self.generatedobj_instance.keyword_filenames}-adobe.csv", index=False)

# ADD HERE FOR OTHER CSV SITES ================================


        dataf_freepik = pandas.DataFrame(df_freepik)
        if self.generatedobj_instance.keyword_filenames == "":
            dataf_freepik.to_csv(
                f"C:/Users/rares/Desktop/csv/freepik/{file_names}-freepik.csv",
                index=False, sep=";")

        else:
            dataf_freepik.to_csv(
                f"C:/Users/rares/Desktop/csv/freepik/{self.generatedobj_instance.keyword_filenames}-freepik.csv",
                index=False, sep=";")

        # messagebox.showinfo(title="Yay!", message="Your CSV with the metadata was saved!")




