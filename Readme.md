
# Remove Background

### A Python command-line tool for removing the background from an image, cropping, formatting, masking, adding a background image, adding colors to the background, and so on...

**It uses [Remove-bg's](https://www.remove.bg/) Api**

**Get Api Key From [Here](https://www.remove.bg/api#remove-background), If the API key is not saved, you will be asked for it while running the tool.**

## Installation

Install Background Remover

```bash
  git clone https://github.com/ASACHIT/IMG-Background-Remover.git
  cd IMG-Background-Remover
  pip3 install -r requirements.txt
  python3 removebg.py  
```

## All Input Flags

| Flag/Arg | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `--setapi` | `string` | **Required**. Your API key. Set or Edit Existing Api key |
| `--img` | `URL or IMG path` | **Required**. Direct Image Url or Image File Path |
| `--filename` | `string` | **Optional**. Set Output File Name. **Default**: bg_remove.png |
| `--size` | `string` | **Optional**. Output Image Resolution Size |
| `--type` | `string` | **Optional**. Type Of Foreground Object. **Default**: 'autodetect' |
| `--format` | `string` | **Optional**. Output Image File Format (PNG,JPG,ZIP). **Default**: 'png' |
| `--crop` | `boolean` | **Optional**. Wheather To Crop All Empty Regions Of Image. **Default**: 'False' |
| `--bgcolor` | `Hex/Name` | **Optional**. Add Solid Background Color. Accepts `Hex color code` or color `name` |
| `--bgimgurl` | `IMG URL` | **Optional**. Paste Another image in Background. Accepts Direct Image URL |
| `--bgimgfile` | `IMG FILE` | **Optional**. Paste Another Image in Background. Accepts Image File |

## or

#### use ```-h``` for manual list

## Screenshot 📷

![App Screenshot](https://i.imgur.com/NrIn2Y4.png)

## small tutorial
https://user-images.githubusercontent.com/73944456/163343102-db7c8b17-a2d0-4121-ab3f-eab99f4bbbc8.mp4



## Features

- In a couple seconds, removes the background with just one command.
- Both IMAGE FILE and DIRECT IMAGE URI are supported.
- user can define output format
- user can provide image resolution
- Background color, image can be masked
- Output image Can be Cropped
- Cross platform
- Everything can be done with just a few commands 😉😜
  
Found a bug ? or got an error? okay Feel Open to [open an issue](<https://github.com/ASACHIT/background-remover/issues>)😅
