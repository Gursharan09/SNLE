import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from heap import MinHeap, MaxHeap
from hashmap import HashMap
from trie import Trie
from graph import Graph, Package


def test_min_heap():
    h = MinHeap()
    h.push(3, 'a')
    h.push(1, 'b')
    h.push(2, 'c')
    assert h.pop()[0] == 1
    assert h.pop()[0] == 2

def test_min_heap_empty():
    h = MinHeap()
    assert h.empty()

def test_max_heap():
    h = MaxHeap()
    h.push(Package('A', 3, 'X', 1))
    h.push(Package('B', 9, 'Y', 1))
    h.push(Package('C', 5, 'Z', 1))
    assert h.pop().package_id == 'B'

def test_max_heap_peek():
    h = MaxHeap()
    h.push(Package('X', 7, 'D', 1))
    assert h.peek().priority == 7

def test_hashmap_insert_get():
    m = HashMap()
    m.insert('A', 100)
    assert m.get('A') == 100

def test_hashmap_delete():
    m = HashMap()
    m.insert('B', 5)
    m.delete('B')
    assert m.get('B') is None

def test_hashmap_update():
    m = HashMap()
    m.insert('C', 1)
    m.insert('C', 2)
    assert m.get('C') == 2

def test_hashmap_missing():
    m = HashMap()
    assert m.get('nope') is None

def test_trie_basic():
    t = Trie()
    t.insert('DepotA')
    assert t.autocomplete('Dep') == ['depota']

def test_trie_multiple():
    t = Trie()
    for w in ['DepotA', 'DepotB', 'Zone1']:
        t.insert(w)
    assert len(t.autocomplete('depot')) == 2

def test_trie_no_match():
    t = Trie()
    t.insert('Alpha')
    assert t.autocomplete('Z') == []

def test_dijkstra():
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('B', 'C', 3)
    cost, path = g.dijkstra('A', 'C')
    assert cost == 5
    assert path == ['A', 'B', 'C']

def test_dijkstra_no_path():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_node('C')
    cost, path = g.dijkstra('A', 'C')
    assert cost is None

def test_cycle():
    g = Graph()
    g.add_edge('X', 'Y', 1)
    g.add_edge('Y', 'Z', 1)
    g.add_edge('Z', 'X', 1)
    found, _ = g.has_cycle()
    assert found

def test_no_cycle():
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 1)
    found, _ = g.has_cycle()
    assert not found

def test_bellman_ford():
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('C', 'B', 1)
    dist, neg = g.bellman_ford('A')
    assert dist['B'] == 3
    assert not neg