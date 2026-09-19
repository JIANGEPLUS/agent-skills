"""Bounded, deterministic differential test demo; standard library only."""
import heapq
import math
import random


def dijkstra(n, edges, source):
    if n < 1 or not 0 <= source < n:
        raise ValueError("invalid graph size or source")
    adjacency = [[] for _ in range(n)]
    for u, v, weight in edges:
        if not 0 <= u < n or not 0 <= v < n or weight < 0:
            raise ValueError("expected valid endpoints and nonnegative weights")
        adjacency[u].append((v, weight))
    distances = [math.inf] * n
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        current, u = heapq.heappop(queue)
        if current != distances[u]:
            continue
        for v, weight in adjacency[u]:
            candidate = current + weight
            if candidate < distances[v]:
                distances[v] = candidate
                heapq.heappush(queue, (candidate, v))
    return distances


def bellman_ford_reference(n, edges, source):
    # Independent relaxation schedule; intended only for bounded demo graphs.
    distances = [math.inf] * n
    distances[source] = 0
    for _ in range(n - 1):
        previous = distances[:]
        for u, v, weight in edges:
            distances[v] = min(distances[v], previous[u] + weight)
        if previous == distances:
            break
    return distances


def check_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(
            f"{context}\nactual={actual!r}\nexpected={expected!r}"
        )


def main():
    fixed = [
        (1, [], 0, [0]),
        (3, [], 0, [0, math.inf, math.inf]),
        (3, [(0, 1, 0), (1, 2, 0), (2, 0, 0)], 0, [0, 0, 0]),
        (3, [(0, 1, 9), (0, 1, 2), (1, 2, 3)], 0, [0, 2, 5]),
        (2, [(0, 0, 0), (0, 1, 10**30)], 0, [0, 10**30]),
    ]
    for n, edges, source, expected in fixed:
        check_equal(dijkstra(n, edges, source), expected, "fixed case")
        check_equal(bellman_ford_reference(n, edges, source), expected,
                    "reference fixed case")
    try:
        dijkstra(2, [(0, 1, -1)], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("negative weight was accepted")
    seed = 20260907
    rng = random.Random(seed)
    comparisons = 0
    for case in range(300):
        n = rng.randint(1, 8)
        edges = [
            (rng.randrange(n), rng.randrange(n), rng.randint(0, 20))
            for _ in range(rng.randint(0, n * n))
        ]
        for source in range(n):
            check_equal(
                dijkstra(n, edges, source),
                bellman_ford_reference(n, edges, source),
                f"seed={seed}, case={case}, n={n}, source={source}, edges={edges!r}",
            )
            comparisons += 1
    print(f"DEMO=PASS; fixed={len(fixed)}; negative_rejection=1; "
          f"random_graphs=300; comparisons={comparisons}; seed={seed}")
    print("Scope: bounded nonnegative integer directed multigraphs; "
          "not a proof or a performance benchmark.")


if __name__ == "__main__":
    main()
