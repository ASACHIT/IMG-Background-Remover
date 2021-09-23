import argparse

from removebg import RemoveBg

api_key = "fyabAxQTv8kwkQoF9JhKzvF7"

cmd_parser = argparse.ArgumentParser(
    prog="REMOVEBG",
    description="Remove Background of Image, Lots of Other Features",
)
cmd_parser.add_argument(
    "--img", type=str, help="Path of Image to Remove Bg", required=True
)
cmd_parser.add_argument(
    "--fn",
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
    "--ch",
    type=str,
    help="request the finalized image ('rgba') or an alpha mask ('alpha')",
    required=False,
    default="output.jpg",
)
cmd_parser.add_argument(
    "--s",
    type=bool,
    help="whether to add an artificial shadow",
    required=False,
    default="output.jpg",
)
cmd_parser.add_argument(
    "--bg",
    type=str,
    help="background (None = no background, path, url, color hex code (e.g. '81d4fa', 'fff'), color name (e.g. 'green'))",
    required=False,
    default="None",
)


class bgrm:
    def __init__(self):
        arguments = cmd_parser.parse_args()
        rmbg = RemoveBg("fyabAxQTv8kwkQoF9JhKzvF7", "error.log",)

        if (arguments.img).startswith("htt"):
            rmbg.remove_background_from_img_url(
                arguments.img,
                size=arguments.size,
                bg_color=arguments.bg
                # type=arguments.type,
                # new_file_name=arguments.fn,
                # shadow=arguments.s,
                # channel=arguments.ch,
            )
        else:
            rmbg.remove_background_from_img_file(
                arguments.img,
                size=arguments.size,
                # type=arguments.type,
                # new_file_name=arguments.fn,
                # shadow=arguments.s,
                # channel=arguments.ch,
            )


bgrm()
