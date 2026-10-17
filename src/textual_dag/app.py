from enum import Enum

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


    def generate_table(self, dag: nx.DiGraph):
        # topological layers (generations)
        gens = list(nx.topological_generations(dag))
        layers = [sorted(list(g)) for g in gens]
        if not layers:
            return Table(box=None)

        # columns: layer columns separated by connector columns
        n_layers = len(layers)
        n_cols = n_layers * 2 - 1
        table = Table(box=None, padding=0)
        for _ in range(n_cols):
            table.add_column("")
        max_rows = max(len(layer) for layer in layers)

        # grid of cells
        grid = [["" for _ in range(n_cols)] for _ in range(max_rows)]
        positions = {}
        # place nodes in even columns (0,2,4,...)
        for li, layer in enumerate(layers):
            col = li * 2
            for ri, node in enumerate(layer):
                positions[node] = (col, ri)
                status = dag.nodes[node].get("status", NodeStatus.PENDING)
                color = STATUS_COLORS.get(status, "white")
                symbol = STATUS_SYMBOLS.get(status, "○")
                # color the symbol; keep name at right
                grid[ri][col] = Padding(f"[{color}]{symbol}[/]{' '}{node}", (0,1,0,1))

        # draw simple connectors for edges that go to a later layer
        for u, v in dag.edges():
            if u not in positions or v not in positions:
                continue
            cu, ru = positions[u]
            cv, rv = positions[v]
            # draw horizontal across connector columns between cu and cv on row ru
            step = 1 if cu < cv else -1
            for c in range(cu + step, cv, step):
                # only draw on connector columns (odd indexes)
                if grid[ru][c] == "":
                    grid[ru][c] = "─"
            # mark a junction at the cell immediately left of the target node
            junction_col = cv - 1 if cu < cv else cv + 1
            if ru == rv:
                grid[ru][junction_col] = "─┤" if cu < cv else "├─"
            else:
                # simple vertical routing down/up from source row to target row in that junction column
                rstart, rend = (ru, rv) if ru < rv else (rv, ru)
                for r in range(rstart, rend + 1):
                    if grid[r][junction_col] == "":
                        grid[r][junction_col] = "│"
                # decorate endpoints
                grid[ru][junction_col] = "┌" if ru < rv else "└"
                grid[rv][junction_col] = "┴"

        # add rows to table
        for r in range(max_rows):
            row_cells = []
            for c in range(n_cols):
                cell = grid[r][c]
                row_cells.append(cell if cell != "" else "")
            table.add_row(*row_cells)
        return table

    def new_digraph(self):
        """Populate nodes and edges from the configured ``Plan``.

        Validates that every declared dependency exists and that the graph has
        no cycles; raises on error.
        """
        dg = nx.DiGraph()
        dg.add_node('node_a', status=NodeStatus.SUCCESS)
        dg.add_node('node_bcdefg', status=NodeStatus.FAILED)
        dg.add_node('node_c', status=NodeStatus.RUNNING)
        dg.add_node('node_d', status=NodeStatus.PENDING)

        dg.add_edge('node_a', 'node_bcdefg')
        dg.add_edge('node_a', 'node_c')
        dg.add_edge('node_bcdefg', 'node_d')
        dg.add_edge('node_c', 'node_d')
        dg.add_edge('node_a', 'node_d')
        return dg

    def compose(self) -> ComposeResult:
        yield Header()
        dg = self.new_digraph()
        table = self.generate_table(dg)
        yield Static(table)
        yield Footer()

    def old_compose(self) -> ComposeResult:
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

