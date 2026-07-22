from pathlib import Path
from rich.text import Text
from rich.table import Table
from textual.screen import Screen
from textual.widgets import Static
from textual.containers import Center, Middle

ASSETS = Path(__file__).parent / "assets"

with open(ASSETS / "title.txt", "r", encoding="ascii") as f:
    TITLE = f.read()

with open(ASSETS / "ace_of_spades.txt", "r", encoding="utf-8") as f:
    ACE_OF_SPADES = f.read()


class SplashScreen(Screen):
    """A bare screen shown briefly on startup, no header/footer."""

    CSS = """
    #splash-content {
        width: auto;
    }
    """

    def compose(self):
        with Middle():
            with Center():
                yield Static(self.build_splash(), id="splash-content")

    def on_mount(self) -> None:
        self.set_timer(4.0, self.dismiss_splash)

    def dismiss_splash(self) -> None:
        self.app.pop_screen()

    @staticmethod
    def build_splash():
        ace_of_spades = Text(ACE_OF_SPADES, style="bold white")
        title = Text(TITLE, style="bold cyan")

        grid = Table.grid(padding=(0, 4))
        grid.add_column(justify="left", vertical="middle")
        grid.add_column(justify="left", vertical="middle")
        grid.add_row(ace_of_spades, title)
        return grid