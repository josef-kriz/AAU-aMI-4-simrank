import networkx as net
import matplotlib.pyplot as plt
import time

from src.graph import create_graph1, create_graph2, create_users_graph
from src.basic_sim_rank import basic_sim_rank, jaccard_similarity, print_table

def run_test(graph, do_print=False):
    start = time.time()
    jacc = jaccard_similarity(graph)
    end = time.time()
    if do_print:
        print_table(graph, jacc)
    print("Jaccard similarity took", round((end - start) * 1000, 3), 'ms')

    start = time.time()
    sim = basic_sim_rank(graph, 0.8)
    end = time.time()
    if do_print:
        print_table(graph, sim)
    print("Basic SimRank took", round((end - start) * 1000, 3), 'ms')

    similar = sorted(jacc['abagael'].items(), key=lambda p: p[1], reverse=True)
    cnt = 0
    for f in similar:
        if cnt == 20:
            break
        cnt = cnt + 1
        print(f)

graph1 = create_graph1()
graph2 = create_graph2()
users = create_users_graph(20000000000)

net.draw(users, pos=net.spring_layout(users), with_labels=True)
plt.show()

run_test(users, False)


