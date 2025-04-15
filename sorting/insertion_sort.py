# Insertion Sort Algorithm – Sorting Playing Cards

import time

def insertion_sort(cards):
    for i in range(1, len(cards)):
        key = cards[i]
        j = i - 1
        while j >= 0 and key < cards[j]:
            cards[j + 1] = cards[j]
            j -= 1
        cards[j + 1] = key

# --- User Input ---
cards = list(map(int, input("Enter card numbers separated by spaces: ").split()))

# --- Execution & Output ---
start_time = time.time()
insertion_sort(cards)
end_time = time.time()

print("\nSorted cards:", cards)
print(f"Execution time: {end_time - start_time:.6f} seconds")
