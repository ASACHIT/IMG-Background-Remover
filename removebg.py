import json

import requests
from rich.console import Console

from cmds import parsecmds

console = Console()

# pasring commands
arguments = parsecmds()


class Api_stuff:
    """
    Class with methods to save api key and Read stored key
    """

    @staticmethod
    def save_api_key() -> None:
        """
        Saves api key to file
        """
        with open(".apikey.txt", "w") as f:
            f.write(input("🤦No api key saved found, Input Key: ").strip())
            console.print(
                "Api key saved successfully:White_Heavy_Check_Mark: Restart the Program :glowing_star: "
            )
            exit()

    @staticmethod
    def read_stored_Api():
        """
        Reads api key from file
        """
        try:
            with open(".apikey.txt", "r") as f:
                key = f.read()
                return key
        except FileNotFoundError:
            # console.print_exception(show_locals=True)
            Api_stuff.save_api_key()


class Other_stuff:
    """
    Class with methods to save Bg Removed images and print formatted errors
    """

    @staticmethod
    def save_image(filename, image) -> None:
        """
        Saves image to file
        """
        with open(filename, "wb") as out:
            out.write(image)
            console.print(
                f":White_Heavy_Check_Mark: [bold green]Background Removed and Saved Image successfully with name {filename}   :winking_face: [/bold green]"
            )

    @staticmethod
    def print_error(error) -> None:
        """
        Prints formatted error
        """
        json_response = json.loads(error)
        error_detail_dict = json_response["errors"][0]
        got_an_error = f"""
            :sob: [bold yellow] Error [/bold yellow]: [red] {error_detail_dict.get('title')} [/red]
            :thinking_face: [bold yellow] Reason [/bold yellow]: [red] {error_detail_dict.get('code')} [/red]
            :page_with_curl: [bold yellow] Detail [/bold yellow]: [red] {error_detail_dict.get('detail')} [/red]
            """
        console.print(got_an_error)


class Remove_background:
    """
    Main class to remove background and that calls other classes"""

    def __init__(self):
        try:
            self.key = Api_stuff().read_stored_Api()
        except FileNotFoundError:
            Api_stuff().save_api_key()

    def remove(self) -> None:
        """
        method to remove background
        """
        with console.status("[bold green] Removing Background") as status:

            if (arguments.img).startswith("http"):
                console.print(" [bold yellow] Uploading Image From URL")
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
                    console.print("[bold yellow] Downloading Image")
                    Other_stuff().save_image(arguments.filename, response.content)
                else:
                    Other_stuff().print_error(response.text)

            else:
                console.print(" [bold yellow] uploading image from local")
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
                    console.print("[bold yellow] Downloading Image")
                    Other_stuff().save_image(arguments.filename, response.content)
                else:
                    Other_stuff().print_error(response.text)


if __name__ == "__main__":
    Remove_background().remove()
