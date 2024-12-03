# autoeditgui

## Project Purpose
This project aims to provide a user-friendly GUI for the Auto-Editor CLI but with a few more added features. This GUI is designed for personal use.
Added features include: audio analysis summary, serving to allow users to make educated decisions on auto-cutting their video.

## Copyright Notice
© [2024] [Rina Yoo]. All rights reserved.

---

## License
**Unlicensed:** This project is a personal project. It is not open source, is not licensed for use, and is not in the public domain. Viewing is permitted, but no permissions are granted for using, modifying, distributing, or incorporating this code into other projects.

For personal reference only. Please contact the copyright holder for any permissions beyond viewing.

---

## Credits

This project utilizes the following third-party libraries:

### Auto-Editor CLI
This project is a GUI for the [Auto Editor CLI](https://github.com/WyattBlue/auto-editor), which is in the public domain under **The Unlicense**.  
Full license details for Auto Editor can be found [here](https://github.com/WyattBlue/auto-editor?tab=Unlicense-1-ov-file#readme).  
Special thanks to the Auto Editor team for making their tool publicly available.

### ffmpeg-progress-yield
This project uses the [ffmpeg-progress-yield](https://github.com/slhck/ffmpeg-progress-yield?tab=readme-ov-file) library, which is licensed under the **MIT License**.

#### Full License Text:
The MIT License (MIT)

Copyright (c) 2021-2023 Werner Robitza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Special thanks to Werner Robitza and the contributors of ffmpeg-progress-yield for providing this tool to the community.

### Qt Libraries
This project utilizes the **Qt libraries**, licensed under the **Lesser General Public License (LGPL)**.  
- The Qt libraries are dynamically linked to this project, and no modifications have been made to the original Qt libraries.  
- This project itself is **non-open source**, is not distributed commercially, and complies with LGPL requirements.

Full license details for Qt can be viewed [here](https://doc.qt.io/qt-6/lgpl.html).  
Special thanks to the Qt Project for their invaluable contributions to the development community.

---

### Note
1. For some reason, I cannot resolve an error from Auto-Editor that I have not seen anyone else have with the most updated version. An av error appears for videos using the hevc video encoder, but Auto-Editor works fine for h264 videos. This might be happening only to my personal version of auto-editor, despite being the latest version.
2. Auto-Editor seems to have issues with videos that have variable frame rate. A few others have found their auto-editor creates incorrect cuts due to this issue. I personally get black frames randomly and extremely frequently throughout my videos, and the rendering itself takes much longer than it should. Please use Handbrake or another application to change the video from vfr to cfr (constant frame rate) if you have the same issues.
