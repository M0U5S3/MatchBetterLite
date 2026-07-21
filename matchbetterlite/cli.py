from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MatchBetterLiteApp(App):
    """Super simple Textual app skeleton."""

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("MatchBetterLite is alive!", id="welcome")
        yield Footer()
