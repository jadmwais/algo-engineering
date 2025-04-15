# Radix Sort Algorithm – LSD and MSD Variants

import random

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits at current place value (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count to store actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy sorted values back to original array
    for i in range(n):
        arr[i] = output[i]

def lsd_radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def msd_radix_sort(arr):
    max_num = max(arr)
    max_digits = len(str(max_num))

    def msd_radix_helper(arr, digit_place):
        if len(arr) <= 1 or digit_place < 0:
            return arr

        # Create buckets for each digit
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // (10 ** digit_place)) % 10
            buckets[digit].append(num)

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(msd_radix_helper(bucket, digit_place - 1))
        return sorted_arr

    return msd_radix_helper(arr, max_digits - 1)

# --- Main Program ---
if __name__ == "__main__":
    num_elements = int(input("Enter the number of elements: "))
    random_list = [random.randint(10, 9999) for _ in range(num_elements)]

    print("\nOriginal Array:", random_list)

    # LSD Radix Sort
    lsd_sorted = random_list.copy()
    lsd_radix_sort(lsd_sorted)
    print("\nSorted using LSD Radix Sort:", lsd_sorted)

    # MSD Radix Sort
    msd_sorted = msd_radix_sort(random_list.copy())
    print("\nSorted using MSD Radix Sort:", msd_sorted)
