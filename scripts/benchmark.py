"""
benchmark.py

Performance benchmark for Dance of the Titans.

This script provides a lightweight benchmark framework for measuring
the execution time of computational tasks used in the simulation.
It serves as a foundation for future performance profiling and
optimization.

Author: Aiden Vihaan
Repository: https://github.com/Aiden-Vihaan/dance-of-the-titans
"""

import time


def benchmark(name, func, iterations=100):
    """Run a simple benchmark."""

    start = time.perf_counter()

    for _ in range(iterations):
        func()

    elapsed = time.perf_counter() - start

    print(f"{name}")
    print(f"Iterations : {iterations}")
    print(f"Total Time : {elapsed:.6f} seconds")
    print(f"Average    : {(elapsed/iterations)*1000:.4f} ms\n")


def particle_update():
    """Placeholder particle update workload."""
    total = 0
    for i in range(10000):
        total += i * i
    return total


def gravitational_force():
    """Placeholder gravity calculation workload."""
    G = 6.67430e-11
    m1 = 35
    m2 = 30
    r = 400

    return G * m1 * m2 / (r ** 2)


def main():
    print("=" * 60)
    print("Dance of the Titans Performance Benchmark")
    print("=" * 60)

    benchmark("Particle Update", particle_update)
    benchmark("Gravity Calculation", gravitational_force, 100000)


if __name__ == "__main__":
    main()
