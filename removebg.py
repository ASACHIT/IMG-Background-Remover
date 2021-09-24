import json

import requests

from cmds import parsecmds

arguments = parsecmds()

# ask api key and saves creating txt file
def ask_api_key():
    with open("apikey.txt", "w") as f:
        f.write(input("🤦No api key saved found, Input Key: ").strip())
        print("Api key saved successfully ✅,Restart the Program 🌟 ")
        exit()


def print_error(error):
    json_response = json.loads(error)
    error_detail_dict = json_response["errors"][0]
    got_an_error = f"""
        Error: {error_detail_dict.get('title')}
        Reason: {error_detail_dict.get('code')}
        Detail: {error_detail_dict.get('detail')}"""
    print(got_an_error)


def save_image(filename, image):
    with open(filename, "wb") as out:
        out.write(image)


class Remove_background:
    def __init__(self) -> None:
        try:
            with open("apikey.txt", "r") as f:
                self.key = f.read()
                if self.key == "":
                    ask_api_key()
        except FileNotFoundError:
            ask_api_key()

    def remove(self):
        if (arguments.img).startswith("htt"):

            response = requests.post(
                "https://api.remove.bg/v1.0/removebg",
                data={
                    "image_url": arguments.img,
                    "size": arguments.size,
                    "type": arguments.type,
                    "format": arguments.format,
                    "crop": arguments.crop,
                    "bg_color": arguments.bgcolor,
                    "bg_image_url": arguments.bgimgurl,
                    "bg_image_file": arguments.bgimgfile,
                },
                headers={"X-Api-Key": self.key},
            )
            if response.status_code == requests.codes.ok:
                save_image(arguments.filename, response.content)
            else:
                print_error(response.text)

        else:
            response = requests.post(
                "https://api.remove.bg/v1.0/removebg",
                files={"image_file": open(arguments.img, "rb")},
                data={
                    "size": arguments.size,
                    "type": arguments.type,
                    "format": arguments.format,
                    "crop": arguments.crop,
                    "bg_color": arguments.bgcolor,
                    "bg_image_url": arguments.bgimgurl,
                    "bg_image_file": arguments.bgimgfile,
                },
                headers={"X-Api-Key": self.key},
            )
            if response.status_code == requests.codes.ok:
                save_image(arguments.filename, response.content)
            else:
                print_error(response.text)


if __name__ == "__main__":
    Remove_background().remove()
