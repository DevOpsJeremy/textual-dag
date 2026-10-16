from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Markdown
from textual.containers import Vertical, Horizontal

from rich.console import Console
from rich.table import Table
from rich.padding import Padding
from rich.text import Text

import networkx as nx

class NodeStatus(Enum):
    """Node execution status."""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"

STATUS_COLORS = {
    NodeStatus.PENDING: "white",
    NodeStatus.RUNNING: "blue",
    NodeStatus.SUCCESS: "green",
    NodeStatus.FAILED: "red",
    NodeStatus.SKIPPED: "yellow",
}

STATUS_SYMBOLS = {
    NodeStatus.PENDING: "○",
    NodeStatus.RUNNING: "◐",
    NodeStatus.SUCCESS: "●",
    NodeStatus.FAILED: "✕",
    NodeStatus.SKIPPED: "⊘",
}

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
    def generate_table(self, dag: nx.DiGraph):
        pass

    def new_digraph(self):
        """Populate nodes and edges from the configured ``Plan``.

        Validates that every declared dependency exists and that the graph has
        no cycles; raises on error.
        """
        dg = nx.DiGraph
        dg.add_node('node_a', status=NodeStatus.SUCCESS)
        dg.add_node('node_bcdefg', status=NodeStatus.FAILED)
        dg.add_node('node_c', status=NodeStatus.RUNNING)
        dg.add_node('node_d', status=NodeStatus.PENDING)

        dg.add_edge('node_a', 'node_bcdefg')
        dg.add_edge('node_a', 'node_c')
        dg.add_edge('node_bcdefg', 'node_d')
        dg.add_edge('node_c', 'node_d')

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


        STATUS_SYMBOLS = {
            "PENDING": "[yellow]○[/yellow]",
            "RUNNING": "[blue]◐[/blue]",
            "SUCCESS": "[green]●[/green]",
            "FAILED": "[red]✕[/red]",
            "SKIPPED": "⊘",
        }

        #table, title="[bold green]Status Overview[/bold green]", expand=True)
        table.add_row("", "", f" ╭─{STATUS_SYMBOLS['SUCCESS']}", Padding(f"{node_b_name} ".ljust(len(node_a_name) + 1, "─"), (0,0,0,1)), Padding("─╮", 0), "")
        table.add_row(STATUS_SYMBOLS['SUCCESS'], Padding("node_a", (0,1,0,1)), "─┤", "", f" ├─{STATUS_SYMBOLS['PENDING']}", Padding("node_d", (0,1,0,1)))
        table.add_row("", "", f" ╰─{STATUS_SYMBOLS['FAILED']}", Padding(node_a_name, (0,1,0,1)), "─╯", "")

        yield Static(table)

        yield Footer()

#
#    def action_refresh(self) -> None:
#        """Refresh the display."""
#        self.refresh()
#
#
