import time
import argparse
from pathlib import Path
from rich.console import Console
from rich.align import Align


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
    console.print("  [dim]music stem separator[/dim]")
    console.print()
    console.print("  takes any song and split it into stems: [cyan]vocals[/cyan], [cyan]drums[/cyan], [cyan]bass[/cyan], and [cyan]other[/cyan]")
    console.print()
    console.print("  [dim]how to use:[/dim]  music-stems [bold]<track>[/bold] [options]")
    console.print("  [dim]for help:[/dim]   music-stems [bold]--help[/bold]")
    console.print()

def main():
    parser = argparse.ArgumentParser(
        description="separate a music track into stems using Demucs"
    )
    args = parser.parse_args()
    intro()