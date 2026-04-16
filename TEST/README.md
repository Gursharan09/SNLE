# SNLE - Smart Network Logistics Engine

Name: Gursharan Kaur  
Student ID: 300218151

---

## About

So basically this project simulates a delivery network for a city. Depots and zones are nodes, and the roads between them are weighted edges. I built all the data structures from scratch (no heapq or anything like that).

The program lets you find the shortest route between two places, check if theres any loops in the network, send out the most important package first, and search up depots by name.

---

## Running it

just run this from the main folder:

python src/main.py

you need python 3, thats it.

## Modules

**graph.py** - the main graph class. stores everything as an adjacency list. has dijkstras for shortest path, dfs for cycle detection and bellman ford as a bonus.

**heap.py** - i made a minheap and maxheap from scratch. minheap is used in dijkstras and maxheap is for the package queue.

**hashmap.py** - custom hashmap using open addressing. resizes itself when it gets too full. used for looking up depot info.

**trie.py** - trie for the autocomplete search feature. walks through characters to find matches.

**utils.py** - just reads the network.txt file and loads everything up.

**main.py** - the menu and all the user input stuff.



TIME COmPlEXITY 

| thing | time | space |
|---|---|---|
| dijkstras | O((V+E) log V) | O(V) |
| cycle detection | O(V+E) | O(V) |
| bellman ford | O(V x E) | O(V) |
| heap push pop | O(log n) | O(n) |
| hashmap get/insert | O(1) average | O(n) |
| trie insert/search | O(L) | O(n) |

---

SAMPLE RUN

Loaded 6 nodes and 6 edges.

---- Smart Network Logistics Engine ---
1. Display Network Summary
2. Find Shortest Path
3. Detect Cycles
4. Dispatch Highest-Priority Package
5. Search Depot by Name
6. Autocomplete Depot Name
7. Bellman-Ford
8. Exit

Choice: 2
From: DepotA
To: ZoneNorth
Path: DepotA -> WarehouseX -> ZoneSouth -> DepotC -> ZoneNorth
Cost: 8.0

Choice: 4
Dispatched: PKG003 | dest: DepotC | priority: 10 | 0.8kg
Remaining: 2

Choice: 6
Prefix: Dep
 - DepotA
 - DepotB
 - DepotC


## Bonus

did bellman ford (option 7) and wrote 16 unit tests in tests/test_snle.py