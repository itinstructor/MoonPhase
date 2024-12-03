"""
    Name: moon_phase_cli.py
    Author: William A Loring
    Created: 07-08-23
    Purpose: Python moon phase program using ephem library
    Display moon information at the current time and location
"""
import moon_class
# Windows: pip install rich
# Linux: pip3 install rich
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()


class MoonPhase:
    def __init__(self) -> None:
        # Print title for program
        console.print(
            Panel.fit(
                "     Moon Phase Calculator     ",
                style="bold green",
                subtitle="By William Loring")
        )

        # Create moonclass object to access methods and properties
        self.mc = moon_class.MoonClass()

        # Create observer
        self.mc.get_observer()

        # Display moon information
        console.print(f"[green]{self.mc.formatted_time}[/green]")
        console.print(f" [bold cyan]Distance from Earth to Moon[/bold cyan]")
        console.print(f"    AU: [cyan]{self.mc.earth_to_moon}[/cyan]")
        console.print(f"    KM: [cyan]{self.mc.km_to_moon:,.0f}[/cyan]")
        console.print(f" Miles: [cyan]{self.mc.miles_to_moon:,.0f}[/cyan]")

        console.print(
            f" Illumination: [bold green]{self.mc.illumination:.0f}%[/bold green]"
        )
        console.print(f" [bold green]{self.mc.phase_description}[/bold green]")

        print()
        input(" Enter to exit")


moon_phase = MoonPhase()
