# music-stems-cli
command line interface version to split any song into stems

```
        ███████╗████████╗███████╗███╗   ███╗███████╗
        ██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝
        ███████╗   ██║   █████╗  ██╔████╔██║███████╗
        ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║
        ███████║   ██║   ███████╗██║ ╚═╝ ██║███████║
        ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝
```

## requirements
- python 3.10+
- ffmpeg — `brew install ffmpeg` (mac) · `sudo apt install ffmpeg` (linux)

## install
```bash
git clone https://github.com/yourname/music-stems-cli
cd music-stems-cli
pip install -e .
```

## usage
```bash
music-stems                           # home screen
```

## credits
audio is split into stems via [demucs](https://github.com/facebookresearch/demucs) from Meta Research