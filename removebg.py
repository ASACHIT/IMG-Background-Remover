import json

import requests

from cmds import parsecmds

# https://github.com/ASACHIT/background-remover.git

arguments = parsecmds()


class Api_stuff:
    @staticmethod
    def save_api_key() -> None:
        with open("apikey.txt", "w") as f:
            f.write(input("🤦No api key saved found, Input Key: ").strip())
            print("Api key saved successfully ✅,Restart the Program 🌟 ")
            exit()

    @staticmethod
    def read_stored_Api():
        try:
            with open("apikey.txt", "r") as f:
                key = f.read()
                return key
        except FileNotFoundError:
            raise FileNotFoundError


class Other_stuff:
    @staticmethod
    def save_image(filename, image) -> None:
        with open(filename, "wb") as out:
            out.write(image)
            print(f"✔ Image saved successfully with filename {filename}😉")

    @staticmethod
    def print_error(error) -> None:
        json_response = json.loads(error)
        error_detail_dict = json_response["errors"][0]
        got_an_error = f"""
            Error: {error_detail_dict.get('title')}
            Reason: {error_detail_dict.get('code')}
            Detail: {error_detail_dict.get('detail')}"""
        print(got_an_error)


class Remove_background:
    def __init__(self):
        try:
            self.key = Api_stuff().read_stored_Api()
        except FileNotFoundError:
            Api_stuff().save_api_key()

    def remove(self) -> None:
        if (arguments.img).startswith("http"):

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
                Other_stuff().save_image(arguments.filename, response.content)
            else:
                Other_stuff().print_error(response.text)

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
                Other_stuff().save_image(arguments.filename, response.content)
            else:
                Other_stuff().print_error(response.text)


if __name__ == "__main__":
    Remove_background().remove()
