# ACDownloader
This script has been made for you due to the problem of deleting the monthly video files of the virtual class of Tabriz University and not adding the possibility of offline download within the site.

💎 Enjoy it 💎

## Contents

1. [Requirements](#requirements)
2. [Initial setup](#initial-setup)
3. [How it works](#how-it-works)
4. [Output](#output)
5. [Known issues](#known-issues)
6. [License](#license)

## Requirements

- [python](https://www.python.org/)
- [ffmpeg](https://ffmpeg.org/)
- [kmplayer](https://www.kmplayer.com/)

## Initial setup

On Windows, download latest version of [Python](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe) & [Ffmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z) & [KMPlayer](https://soft98.ir/multi-media/video-player/278-kmplayer-dl.html) and install Python and KMPlayer.

On Ubuntu, open your terminal by pressing `Ctrl+Alt+T` and install the FFmpeg & KMPlayer & Python package, by typing:
```
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt-get install python3.8
sudo apt-get install kmplayer
```

## How it works

If you are a Windows user, extract after downloading the code, then copy `ffmpeg.exe` to that folder, else this unnecessary.

![one](https://uupload.ir/files/v7td_screenshot_2021-03-31_140544.png)

In order to have a video version of the held class, you need to get the address of the desired class as follows:

![two](https://uupload.ir/files/1k84_screenshot_2021-03-31_134100.png)

Then open commands.text and insert command as following and pressing `Ctrl+s`:
```
echo class_link_1 > saved_file_name_1
echo class_link_2 > saved_file_name_2
...
```

Now hold `shift` and `right click` on the code folder and select Terminal or PowerShell and enter the following command:
```
python main.py
```

At the end, follow the instructions that you see inside Terminal or PowerShell.

## Output

If the master has used the `share screen` feature, the output will be a video file in `flv` format, otherwise an audio file will be saved in the `output` folder.

## Known issues

- ~If the teacher allows a student to speak, the sound will not be inserted into the output at the appropriate time~

# License

```
Copyright 2021 ErfanSn

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
