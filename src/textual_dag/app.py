from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Markdown
from textual.containers import Vertical, Horizontal

class DAGApp(App):
    """Textualize app for DAG visualization"""
#
#    CSS = """
#    Screen {
#        layout: vertical;
#    }
#
#    #dag_container {
#        height: 60%;
#        width: 100%;
#    }
#
#    #status_container {
#        height: 40%;
#        width: 100%;
#    }
#
#    DAGRenderer {
#        overflow: auto;
#    }
#
#    DAGStatusTable {
#        overflow: auto;
#    }
#    """
#
#    BINDINGS = [
#        ("q", "quit", "Quit"),
#        ("r", "refresh", "Refresh"),
#    ]
#
#
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

        with Horizontal():
            with Vertical(id="dag_container"):
                yield Markdown("hello") # print("Hello") # yield DAGRenderer(self.dag, self.initial_statuses)

            with Vertical(id="status_container"):
                print("Goodbye") # yield DAGStatusTable(self.initial_statuses)

        yield Footer()
#
#    def action_refresh(self) -> None:
#        """Refresh the display."""
#        self.refresh()
#
#
