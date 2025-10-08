import random
import time

# If your file name is algorithms.py, change the import accordingly.
from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search,
)

# ---------------------------
# Part 1 – Small deterministic tests
# ---------------------------
def run_part1():
    print("=" * 72)
    print("PART 1 – Small Test with Present and Absent Targets")
    print("=" * 72)

    arr = [3, 5, 8, 12, 14, 18, 21]
    arr.sort()

    target_present = 12
    target_absent = 9

    # Recursive Binary Search
    idx = recursive_binary_search(arr, target_present, 0, len(arr) - 1)
    print(f"Recursive BS: {target_present} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    idx = recursive_binary_search(arr, target_absent, 0, len(arr) - 1)
    print(f"Recursive BS: {target_absent} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    # Iterative Binary Search
    idx = iterative_binary_search(arr, target_present)
    print(f"Iterative BS: {target_present} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    idx = iterative_binary_search(arr, target_absent)
    print(f"Iterative BS: {target_absent} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    # Sequential Search
    idx = sequential_search(arr, target_present)
    print(f"Sequential : {target_present} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    idx = sequential_search(arr, target_absent)
    print(f"Sequential : {target_absent} -> "
          f"{'found at index ' + str(idx) if idx != -1 else 'not found'}")

    print()  # spacing


# ---------------------------
# Part 2 – Random numbers (small N) with success/failure cases
# ---------------------------
def run_part2(seed: int = 1337):
    print("=" * 72)
    print("PART 2 – Random Numbers (Small N)")
    print("=" * 72)

    random.seed(seed)

    # Example with ~20 numbers; sorted for binary search correctness
    arr = [random.randint(1, 100) for _ in range(20)]
    arr_sorted = sorted(arr)

    # 50% chance of choosing a present element; otherwise pick 999 (not present)
    target = random.choice(arr_sorted) if random.random() < 0.5 else 999

    print(f"Array (sorted): {arr_sorted}")
    print(f"Target: {target}")

    # Run all searches
    idx_r = recursive_binary_search(arr_sorted, target, 0, len(arr_sorted) - 1)
    idx_i = iterative_binary_search(arr_sorted, target)
    idx_s = sequential_search(arr_sorted, target)

    print(f"Recursive BS -> {'index ' + str(idx_r) if idx_r != -1 else 'not found'}")
    print(f"Iterative BS -> {'index ' + str(idx_i) if idx_i != -1 else 'not found'}")
    print(f"Sequential   -> {'index ' + str(idx_s) if idx_s != -1 else 'not found'}")
    print()  # spacing


# ---------------------------
# Part 3 – Measure and compare runtime growth (averages over 10 runs)
# ---------------------------
def time_call_us(func, *args, **kwargs) -> float:
    """Return elapsed time in microseconds for a single function call."""
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) * 1_000_000.0  # microseconds


def run_part3(seed: int = 4242):
    print("=" * 72)
    print("PART 3 – Average Runtime Growth (10 trials per N, microseconds)")
    print("=" * 72)

    random.seed(seed)
    # Data sizes as specified in the instructions
    data_sizes = [5000, 50000, 100000, 150000, 1_000_000]  #  [oai_citation:2‡Analyze Running Time of Search Algorithms.docx](sediment://file_00000000883461f79d3de5ebdda60ea0)

    # Table header
    print(f"{'N':>12} | {'Recursive BS (µs)':>20} | {'Iterative BS (µs)':>18} | {'Sequential (µs)':>16}")
    print("-" * 72)

    for N in data_sizes:
        sum_rbs = 0.0
        sum_ibs = 0.0
        sum_seq = 0.0

        # 10 experimental runs for each N
        for _ in range(10):
            # Sorted array of N random integers in [1, 1_000_000]
            arr = sorted(random.randint(1, 1_000_000) for _ in range(N))
            # Random target (not guaranteed to be present)
            target = random.randint(1, 1_000_000)

            # Recursive Binary Search timing
            sum_rbs += time_call_us(recursive_binary_search, arr, target, 0, len(arr) - 1)

            # Iterative Binary Search timing
            sum_ibs += time_call_us(iterative_binary_search, arr, target)

            # Sequential Search timing
            sum_seq += time_call_us(sequential_search, arr, target)

        avg_rbs = sum_rbs / 10.0
        avg_ibs = sum_ibs / 10.0
        avg_seq = sum_seq / 10.0

        print(f"{N:12d} | {avg_rbs:20.2f} | {avg_ibs:18.2f} | {avg_seq:16.2f}")

    print()  # spacing
    print("Note: microsecond (µs) averages printed for each N (10 trials per size).")
    print()


def main():
    # Part 1
    run_part1()

    # Part 2
    run_part2()

    # Part 3
    run_part3()


if __name__ == "__main__":
    main()