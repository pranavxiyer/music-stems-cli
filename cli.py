import time
import argparse
from pathlib import Path
from rich.console import Console
from rich.align import Align
import demucs.separate
import warnings
warnings.filterwarnings("ignore")

console = Console()
valid_extensions = {".mp3", ".wav"}

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
    console.print("  [dim]how to use:[/dim]  just enter your [magenta]input audio path[/magenta] and [magenta]desired save directory[/magenta]!")
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

def run_demucs(track, output, mp3=False):
    demucs_args = ["-n", "htdemucs", "-o", output]
    if mp3:
        demucs_args.append("--mp3")
    
    demucs_args.append(track)
    demucs.separate.main(demucs_args)
    console.print("[bold green]complete![/bold green]")


def main():
    intro()
    try:
        while True:
            while True:
                track = input("enter your audio file path: ").strip()
                track_path = Path(track)
                if not track_path.exists():
                    console.print(f"[red]file not found: {track}[/red]")
                elif track_path.suffix.lower() not in valid_extensions:
                    console.print(f"[red]unsupported file type '{track_path.suffix}', use: {', '.join(valid_extensions)}[/red]")
                else:
                    break
            
            while True:
                output = input("enter your desired output directory (defaults to current directory): ").strip()
                output_path = Path(output).expanduser().resolve()
                if not output_path.exists():
                    create = input(f"  path '{output}' doesn't exist, create it? (y/n): ").strip().lower()
                    if create == "y":
                        output_path.mkdir(parents=True)
                        break
                else:
                    break
            
            mp3 = input("save as mp3? (y/n, default: n): ").strip().lower() == "y"
            run_demucs(str(track_path), str(output_path), mp3)
            
            again = input("separate another track? (y/n): ").strip().lower()
            
            if again != "y":
                console.print("[dim]goodbye![/dim]")
                break

    except KeyboardInterrupt:
        console.print("\n[dim]goodbye![/dim]")