import networkx as net
import matplotlib.pyplot as plt

from src.graph import create_graph1, create_graph2
from src.basic_sim_rank import basic_sim_rank

graph1 = create_graph1()
graph2 = create_graph2()

print(basic_sim_rank(graph1, 0.8))

# net.draw(graph2, pos=net.spring_layout(graph2), with_labels=True)
# plt.show()
