import networkx as net
import matplotlib.pyplot as plt
import time
from src.graph import create_graph1, create_graph2, create_users_graph
from src.basic_sim_rank import basic_sim_rank, jaccard_similarity, print_table

# NOTES
# - many ways to assess similarity in graphs
# - vertex similarity - number of shared neighbors
# - jaccard similarity - number of shared neighbors divided by number of all neighbors
# - does not really tell a lot about the overall structure of the graph
# - similarity can be also measured according to node properties
# - structural context = similar objects are related to similar objects
# - presumption is that maximum similarity has an object with itself = 1
# - SimRank uses similarity of in-neighbors
# - there is the C constant that decays the similarity with each step from the node
# - decreasing C means we care less about nodes further away
# - bipartite - we might prefer nodes from one partition
# - minmax - do not use all neighbors but just the best (most similar)
# - computed by means of iteration to the fixed point
# - iteration converges quite quickly
# - more advanced approach uses random surfers and asks "how fast do they meet"

# PROBLEMS:
# - problem with the selected dataset is that we were not able to experiment on small portion of data
# - there is lot of friends connections so it made it impossible to somehow verify the results
# - we verified the correctness on small graphs from the lecture

# FINDINGS:
# - it is really computationaly extensive
# - 3500 friends took about 10 minutes
# - jaccard similarity was much faster but it only takes into account the closest neighbors

def run_test(graph, do_print=False):
    start = time.time()
    jacc = jaccard_similarity(graph)
    end = time.time()
    if do_print:
        print_table(graph, jacc)
    print("Jaccard similarity took", round((end - start) * 1000, 3), 'ms')

    similar = sorted(jacc['abagael'].items(), key=lambda p: p[1], reverse=True)
    cnt = 0
    for f in similar:
        if cnt == 20:
            break
        cnt = cnt + 1
        print(f)

    start = time.time()
    sim = basic_sim_rank(graph, 0.8, 5)
    end = time.time()
    if do_print:
        print_table(graph, sim)
    print("Basic SimRank took", round((end - start) * 1000, 3), 'ms')

    similar = sorted(sim['abagael'].items(), key=lambda p: p[1], reverse=True)
    cnt = 0
    for f in similar:
        if cnt == 20:
            break
        cnt = cnt + 1
        print(f)

graph1 = create_graph1()
graph2 = create_graph2()
users = create_users_graph(1000)

print(len(users.nodes))

# net.draw(users, pos=net.spring_layout(users), with_labels=True)
# plt.show()

run_test(users, False)


