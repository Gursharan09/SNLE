import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from graph import Graph, Package
from hashmap import HashMap
from trie import Trie
from heap import MaxHeap


def load(path):
    g = Graph()
    hm = HashMap()
    t = Trie()
    q = MaxHeap()
    section = None

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line in ("NODES", "EDGES", "PACKAGES"):
                section = line
                continue
            if section == "NODES":
                for name in line.split():
                    g.add_node(name)
                    hm.insert(name, {"loc": "Zone-" + name[-1], "cap": 200, "active": True})
                    t.insert(name)
            elif section == "EDGES":
                a, b, w = line.split()
                g.add_edge(a, b, float(w))
            elif section == "PACKAGES":
                pid, pri, dest, kg = line.split()
                q.push(Package(pid, pri, dest, kg))

    return g, hm, t, q