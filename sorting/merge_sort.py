# Merge Sort Algorithm – Sorting a Randomly Generated Array

import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# --- Generate Random Array ---
num_elements = int(input("Enter the number of elements to generate: "))
arr = [random.randint(1, 100) for _ in range(num_elements)]
print(f"\nGenerated random array: {arr}")

# --- Confirm Execution ---
user_response = input("\nDo you want to run Merge Sort now? (Yes/No): ").strip().lower()

if user_response == 'yes':
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()

    print(f"\nSorted array: {arr}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")
