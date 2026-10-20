```python
networkx.topological_generations(networkx.DiGraph)
# [['node_a'], ['node_b', 'node_c'], ['node_d']]
#
# ● node_a ─┬───────────┬─● node_e ─┬─● node_f
#           ├─● node_b ─┤           │
#           ├─● node_c ─╯           │
#           ╰─● node_d ─────────────╯
#
#           ╭─● node_b ─╮ ╭─● node_e ─┬─● node_g
#           ├─● node_c ─┼─┴─● node_d  ├─● node_m
# ● node_a ─┼─● node_h ─╯             │
#           ├─● node_f ───────────────╯
#           ╰─● node_i ─────● node_l
# ● node_j ───● node_k
#
# ├ ┤ ┴ ┬ ┼ │ ─ ╭ ╮ ╯ ╰
#
# ╭──┬──╮
# │  │  │
# ├──┼──┤
# │  │  │
# ╰──┴──╯
#
        #table, title="[bold green]Status Overview[/bold green]", expand=True)
        table.add_row("", "", f" ╭─{STATUS_SYMBOLS['SUCCESS']}", Padding(f"{node_b_name} ".ljust(len(node_a_name) + 1, "─"), (0,0,0,1)), Padding("─╮", 0), "")
        table.add_row(STATUS_SYMBOLS['SUCCESS'], Padding("node_a", (0,1,0,1)), "─┤", "", f" ├─{STATUS_SYMBOLS['PENDING']}", Padding("node_d", (0,1,0,1)))
table.add_row("", "", f" ╰─{STATUS_SYMBOLS['FAILED']}", Padding(node_a_name, (0,1,0,1)), "─╯", "")
```


        STATUS_SYMBOLS = {
            "PENDING": "[yellow]○[/yellow]",
            "RUNNING": "[blue]◐[/blue]",
            "SUCCESS": "[green]●[/green]",
            "FAILED": "[red]✕[/red]",
            "SKIPPED": "⊘",
        }


