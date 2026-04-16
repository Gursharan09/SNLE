import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from utils import load

FILE = os.path.join(os.path.dirname(__file__), '..', 'DATA', 'Network.txt')


def main():
    g, hm, t, q = load(FILE)
    print(f"Loaded {len(g.nodes)} nodes and {len(g.edges)} edges.\n")

    while True:
        print("===== Smart Network Logistics Engine =====")
        print("1. Display Network Summary")
        print("2. Find Shortest Path")
        print("3. Detect Cycles")
        print("4. Dispatch Highest-Priority Package")
        print("5. Search Depot by Name")
        print("6. Autocomplete Depot Name")
        print("7. Bellman-Ford")
        print("8. Exit")
        choice = input("Choice: ").strip()

        if choice == '1':
            g.summary()

        elif choice == '2':
            print("Nodes:", ", ".join(sorted(g.nodes)))
            src = input("From: ")
            dst = input("To: ")
            if src not in g.adj or dst not in g.adj:
                print("Node not found.")
                continue
            cost, path = g.dijkstra(src, dst)
            if not path:
                print("No path.")
            else:
                print("Path:", " -> ".join(path))
                print("Cost:", cost)

        elif choice == '3':
            found, nodes = g.has_cycle()
            if found:
                print("Cycle found! Nodes:", ", ".join(nodes))
            else:
                print("No cycle found.")

        elif choice == '4':
            if q.empty():
                print("No packages.")
            else:
                pkg = q.pop()
                print(f"Dispatched: {pkg.package_id} | dest: {pkg.destination} | priority: {pkg.priority} | {pkg.weight_kg}kg")
                print(f"Remaining: {q.size()}")

        elif choice == '5':
            name = input("Depot name: ")
            info = hm.get(name)
            if info:
                print(f"Name: {name}, Location: {info['loc']}, Capacity: {info['cap']}, Active: {info['active']}")
            else:
                print("Not found.")

        elif choice == '6':
            prefix = input("Prefix: ")
            matches = t.autocomplete(prefix)
            if matches:
                for m in matches:
                    print(" -", m)
            else:
                print("No matches.")

        elif choice == '7':
            print("Nodes:", ", ".join(sorted(g.nodes)))
            src = input("From: ")
            if src not in g.adj:
                print("Node not found.")
                continue
            dist, neg = g.bellman_ford(src)
            if neg:
                print("Warning: negative cycle!")
            for n in sorted(dist):
                print(f"  {n}: {dist[n] if dist[n] != float('inf') else 'unreachable'}")

        elif choice == '8':
            print("Exiting.")
            break

        else:
            print("Invalid option.")
        print()


if __name__ == '__main__':
    main()