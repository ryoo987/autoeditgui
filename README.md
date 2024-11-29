# autoeditgui

## Project Purpose
This project aims to provide a user-friendly GUI for the Auto-Editor CLI but with a few more added features. This GUI is designed for personal use.
Added features include: audio analysis summary, serving to allow users to make educated decisions on auto-cutting their video.

## Copyright Notice
© [2024] [Rina Yoo]. All rights reserved.

## License
**Unlicensed:** This project is a personal project. It is not open source, is not licensed for use, and is not in the public domain. Viewing is permitted, but no permissions are granted for using, modifying, distributing, or incorporating this code into other projects.

For personal reference only. Please contact the copyright holder for any permissions beyond viewing.

## Credits
This project interfaces with the [Auto Editor CLI](https://github.com/WyattBlue/auto-editor), which is in the public domain under The Unlicense. Full license details for Auto Editor can be found [here](https://github.com/WyattBlue/auto-editor?tab=Unlicense-1-ov-file#readme).
Special thanks to the Auto Editor team for making their tool publicly available.

This project also utilizes the Qt libraries under the LGPL (Lesser General Public License). No modifications have been made to the Qt libraries, and they are dynamically linked within this project, in accordance with LGPL requirements. This project itself is non-open source, is not being distributed commercially, and complies with LGPL requirements.

### Note
1. For some reason, I cannot resolve an error from Auto-Editor that I have not seen anyone else have with the most updated version. An av error appears for videos using the hevc video encoder, but Auto-Editor works fine for h264 videos. This might be happening only to my personal version of auto-editor, despite being the latest version.
2. Auto-Editor seems to have issues with videos that have variable frame rate. A few others have found their programs have incorrect cuts here and there. I personally get black frames randomly and extremely frequently. Please use Handbrake or another application to change the video from vfr to cfr (constant frame rate) if you have the same issues.
