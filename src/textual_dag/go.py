import networkx as nx
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from widget import DAG, NodeStatus


class DAGApp(App):
    def new_digraph(self):
        dg = nx.DiGraph()
        dg.add_node("node_a", status=NodeStatus.SUCCESS)
        dg.add_node("node_b", status=NodeStatus.FAILED)
        dg.add_node("node_c", status=NodeStatus.RUNNING)
        dg.add_node("node_d", status=NodeStatus.PENDING)
        dg.add_node("node_e", status=NodeStatus.PENDING)
        dg.add_node("node_f", status=NodeStatus.PENDING)
        dg.add_node("node_g", status=NodeStatus.PENDING)
        dg.add_node("node_h", status=NodeStatus.PENDING)
        dg.add_node("node_i", status=NodeStatus.PENDING)
        dg.add_node("node_j", status=NodeStatus.PENDING)
        dg.add_node("node_k", status=NodeStatus.PENDING)
        dg.add_node("node_l", status=NodeStatus.PENDING)

        dg.add_edge("node_a", "node_b")
        dg.add_edge("node_a", "node_c")
        dg.add_edge("node_a", "node_h")
        dg.add_edge("node_a", "node_f")
        dg.add_edge("node_a", "node_i")
        dg.add_edge("node_i", "node_l")
        dg.add_edge("node_b", "node_e")
        dg.add_edge("node_b", "node_d")
        dg.add_edge("node_c", "node_e")
        dg.add_edge("node_c", "node_d")
        dg.add_edge("node_h", "node_e")
        dg.add_edge("node_h", "node_d")
        dg.add_edge("node_e", "node_g")
        dg.add_edge("node_e", "node_m")
        dg.add_edge("node_f", "node_g")
        dg.add_edge("node_f", "node_m")
        dg.add_edge("node_j", "node_k")
        return dg

    def compose(self) -> ComposeResult:
        yield Header()
        dag = self.new_digraph()
        yield DAG(digraph=dag)
        yield Footer()


app = DAGApp()
app.run()
