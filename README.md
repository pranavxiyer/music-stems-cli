# music-stems-cli
command line interface version to split any song into stems

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
music-stems <track>
music-stems <track> --mp3
music-stems <track> -d cpu -o ~/Desktop
```

## options
| flag | description | default |
|------|-------------|---------|
| `-d, --device` | `mps`, `cpu`, or `cuda` | `mps` |
| `-o, --output` | output directory | `./separated` |
| `--mp3` | save as mp3 instead of wav | off |

## credits
stems uses [demucs](https://github.com/facebookresearch/demucs) by Meta Research