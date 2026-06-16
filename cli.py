import time
import argparse
from pathlib import Path
from rich.console import Console
from rich.align import Align
import demucs.separate
import warnings
warnings.filterwarnings("ignore")

console = Console()

def intro():
    time.sleep(0.3)
    console.print()

    logo = """
        ███████╗████████╗███████╗███╗   ███╗███████╗
        ██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝
        ███████╗   ██║   █████╗  ██╔████╔██║███████╗
        ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║
        ███████║   ██║   ███████╗██║ ╚═╝ ██║███████║
        ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝
    """

    lines = logo.split("\n")[1:-1]
    colors = ["bright_magenta", "magenta", "bright_cyan", "cyan", "bright_blue", "blue"]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        console.print(Align.left(f"[{color}]{line}[/{color}]"))
        time.sleep(0.07)
    
    console.print()
    console.print("  take any song and split it into stems: [cyan]vocals[/cyan], [cyan]drums[/cyan], [cyan]bass[/cyan], and [cyan]other[/cyan]")
    console.print()
    console.print("  [dim]how to use:[/dim]  music-stems [bold]<track>[/bold] [options]")
    console.print("  [dim]for detailed help:[/dim]   music-stems [bold]--help[/bold]")
    console.print()

def print_result(output_dir: str, model: str, track: str, mp3: bool):
    ext = "mp3" if mp3 else "wav"
    stems_dir = Path(output_dir) / model / Path(track).stem

    console.print()
    console.print("[bold green]✓ Done![/bold green] Stems saved to:")
    console.print()
    for f in sorted(stems_dir.glob(f"*.{ext}")):
        console.print(f"  [cyan]{f.name}[/cyan]  [dim]{f}[/dim]")
    console.print()

def main():
    parser = argparse.ArgumentParser(
        description="separate any song into their stems via demucs, a hybrid transformer model released by Meta"
    )
    parser.add_argument("-d", "--device", default="mps", choices=["mps", "cpu", "cuda"], help="choose your device (default: mps)")
    parser.add_argument("track", nargs="?", help="path to the audio file")
    parser.add_argument("-o", "--output", default="separated", help="output directory (default: ./separated)")
    parser.add_argument("--mp3", action="store_true", help="save output as mp3 instead of wav")
    
    args = parser.parse_args()

    if not args.track:
        intro()
    else:
        demucs_args = ["-n", "htdemucs", "--device", args.device, "-o", args.output]
        if args.mp3:
            demucs_args.append("--mp3")
        demucs_args.append(args.track)

        demucs.separate.main(demucs_args)