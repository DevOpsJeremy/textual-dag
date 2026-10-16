from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Markdown
from textual.containers import Vertical, Horizontal

from rich.console import Console
from rich.table import Table
from rich.padding import Padding
from rich.text import Text

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

        table = Table(box=None, padding=0)

        table.add_column("")
        table.add_column("")
        table.add_column("")
        table.add_column("")
        table.add_column("")
        table.add_column("")

        node_a_name = "node_cdefg"
        node_b_name = "node_b"


        table.add_row("", "", " ╭─●", Padding(f"{node_b_name} ".ljust(len(node_a_name) + 1, "─"), (0,0,0,1)), Padding("─╮", 0), "")
        table.add_row(Text("●", style=f"bold green"), Padding("node_a", (0,1,0,1)), "─┤", "", " ├─●", Padding("node_d", (0,1,0,1)))
        table.add_row("", "", " ╰─●", Padding(node_a_name, (0,1,0,1)), "─╯", "")

        yield Static(table)

        yield Footer()

#
#    def action_refresh(self) -> None:
#        """Refresh the display."""
#        self.refresh()
#
#
