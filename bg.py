import argparse
import requests

api_key = "fyabAxQTv8kwkQoF9JhKzvF7"

cmd_parser = argparse.ArgumentParser(
    prog="REMOVEBG",
    description="Remove Background of Image, Lots of Other Features",
)
cmd_parser.add_argument(
    "--img", type=str, help="Path of Image to Remove Bg", required=True
)
cmd_parser.add_argument(
    "--filename",
    type=str,
    help="Output Name Of Image",
    required=False,
    default="output.jpg",
)
cmd_parser.add_argument(
    "--size",
    type=str,
    help="size of the output image ('auto' = highest available resolution, 'preview'",
    required=False,
    default="auto",
)
cmd_parser.add_argument(
    "--type",
    type=str,
    help="foreground object ('auto' = autodetect, 'person', 'product', 'car')",
    required=False,
    default="auto",
)
cmd_parser.add_argument(
    "--format",
    type=str,
    required=False,
    help="Image Type of Output JPG, PNG, ZIP | PNG for Transparent !",
    default="png",
)
cmd_parser.add_argument(
    "--ch",
    type=str,
    help="request the finalized image ('rgba') or an alpha mask ('alpha')",
    required=False,
)

cmd_parser.add_argument(
    "--bgcolor",
    type=str,
    help="Adds a solid color background.HEX color(e.g.81d4fa) or name(e.g. green).RGBA digit hex codes are also supported",
    required=False,
    default="",
)

cmd_parser.add_argument(
    "--bg-img-url",
    type=bool,
    help="Adds a background image from a URL",
    required=False,
    default="",
)
cmd_parser.add_argument(
    "--bg-img-file",
    type=bool,
    help="Adds a background image from a file name/path",
    required=False,
    default="",
)
cmd_parser.add_argument(
    "--crop",
    type=bool,
    help="Whether to crop off all empty regions | Takes Boolean(true/false)(default: false).",
    required=False,
    default="false",
)


class bgrm:
    def __init__(self):
        arguments = cmd_parser.parse_args()
        if (arguments.img).startswith("htt"):
            response = requests.post(
                "https://api.remove.bg/v1.0/removebg",
                data={
                    "image_url": "https://www.remove.bg/example.jpg",
                    "size": arguments.size,
                    "type": arguments.type,
                    "format": arguments.format,
                    "crop": arguments.crop,
                    "bg_color": arguments.bgcolor,
                },
                headers={"X-Api-Key": api_key},
            )
            if response.status_code == requests.codes.ok:
                with open(arguments.filename, "wb") as out:
                    out.write(response.content)
            else:
                print("Error:", response.status_code, response.text)

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
                },
                headers={"X-Api-Key": api_key},
            )
            if response.status_code == requests.codes.ok:
                with open(arguments.filename, "wb") as out:
                    out.write(response.content)
            else:
                print("Error:", response.status_code, response.text)


bgrm()
