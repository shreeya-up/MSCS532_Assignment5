import random

from quick_sorts import det_quick_sort, ran_quick_sort

def test_quick_sorts(sort_func, name, test_cases = 100, max_len = 25, max_val = 20):
    """COmpares sort_func against Python's sorted() on edge cases and random arrays"""
    edge_cases = [
        [],
        [2],
        [1,2],                                 
        [3,1],
        [10,10,10,10,10],
        list(range(20)),
        list(range(15, 0, -1))
    ]                                         # Edge cases to test the sorting function against

    random_cases = [
        [random.randint(1, max_val) for _ in range(random.randint(0, max_len))] for _ in range(test_cases)
    ]                                         # Random test cases to test the sorting function against

    for case in edge_cases + random_cases:
        sorted_case = sorted(case)
        sort_func(case)
        if case != sorted_case:
            print(f"Test failed for {name}: {case} != {sorted_case}") # Print a message if the test fails
        else:
            print(f"Test passed for {name}: {case}") # Print a message if the test passes


if __name__ == "__main__":
    test_quick_sorts(ran_quick_sort, "Randomized quick Sort")
    test_quick_sorts(det_quick_sort, "Deterministic quick Sort")  # Tested the deterministic and randomized quicksort implementation