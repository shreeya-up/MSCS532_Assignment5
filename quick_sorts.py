import random

# Code for Quicksort
def partition(a, lo, hi, p_index):
    """Decides on the pivot index based on the p_index parameter and partitions the array."""
    if p_index == "random":
        m = random.randint(lo, hi)      # Choose a random pivot index
    elif p_index == "first":
        m = lo                          # Choose the first element as the pivot
    else:
        m = hi                          # Choose the last element as the pivot
    a[m], a[hi] = a[hi], a[m]       #Moving chosen pivot to the end
    x = a[hi]
    i = lo - 1                      #boundary index
    for j in range(lo, hi):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]     # Swap elements to ensure elements <= pivot are on the left
    a[i + 1], a[hi] = a[hi], a[i + 1]   # Place the pivot in its final position
    return i + 1                        # Return the index of the pivot after partitioning

def quick_sort(a, p_index):
    """Sorts the array in place using the quicksort algorithm."""
    def sort(lo, hi):
        while lo<hi:
            q = partition(a, lo, hi, p_index)
            if q - lo < hi - q:         # Choose the smaller partition to sort first
                sort(lo, q - 1)         # Recursively sort the left partition
                lo = q + 1
            else:
                sort(q + 1, hi)           # Recursively sort the right partition
                hi = q - 1
    sort(0, len(a) - 1)                 # Start the sorting process from the full array range

def det_quick_sort(a):
       """Sorts the array in place using the deterministic quicksort algorithm."""
       quick_sort(a, "first")           # Use the first element as the pivot for deterministic quicksort

def ran_quick_sort(a):
    """Sorts the array in place using the randomized quicksort algorithm."""
    quick_sort(a, "random")           # Use a random element as the pivot for randomized quicksort