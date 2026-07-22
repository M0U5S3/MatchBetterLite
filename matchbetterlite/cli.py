from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from matchbetterlite.splash import SplashScreen

class MainScreen:
    """Placeholder for now — replace with your real screen class later."""
    pass

class MatchBetterLiteApp(App):
    TITLE = "Spades Client"
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Lorum Ipsum")
        yield Footer()

    def on_mount(self) -> None:
        self.push_screen(SplashScreen())
