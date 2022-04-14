import argparse


def parsecmds():
    """
    Parses the command line arguments and returns the parsed arguments
    """
    cmd_parser = argparse.ArgumentParser(
        prog="REMOVEBG",
        description="Remove Background of Image, With A Lot More Features",
    )
    cmd_parser.add_argument(
        "--setapi",
        type=str,
        help="add new or edit stored api key (use with '--img' flag",
        required=False,
        default="empty",
    )
    cmd_parser.add_argument(
        "--img", type=str, help="Path of Image or Image URL to Remove Bg", required=True
    )
    cmd_parser.add_argument(
        "--filename",
        type=str,
        help="Output Name Of Imagefile | Default:'bg_removed.png'",
        required=False,
        default="bg_removed.png",
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
        "--crop",
        type=bool,
        help="Whether to crop off all empty regions | Takes Boolean(true/false)(default: false).",
        required=False,
        default="false",
    )
    cmd_parser.add_argument(
        "--bgcolor",
        type=str,
        help="Adds a solid color background.HEX color(e.g.81d4fa) or name(e.g. green).RGBA hex codes supported",
        required=False,
        default="",
    )
    cmd_parser.add_argument(
        "--bgimgurl",
        type=bool,
        help="Adds a background image from a direct image url",
        required=False,
    )
    cmd_parser.add_argument(
        "--bgimgfile",
        type=bool,
        help="Adds a background image from a file name/path",
        required=False,
    )
    arguments = cmd_parser.parse_args()

    if not arguments.setapi == "empty":
        with open(".apikey.txt", "w") as f:
            f.write(arguments.setapi)
        print("[bold green] API Key Stored Successfully")

    return arguments
