def read_offset():
    with open("PromptCreator/data/offset.txt", "r") as offset_num:
        offset_result = offset_num.read()
    return int(offset_result)

def is_url_in_data(new_url):
    with open("PromptCreator/data/used_photos_url.csv", "r") as data_csv:
        url_list = data_csv.read().split("\n")
        if new_url in url_list:
            return True
        else:
            return False