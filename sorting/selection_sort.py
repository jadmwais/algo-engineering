# Selection Sort Algorithm – Sorting Books by Publication Year

import time

def selection_sort(books):
    n = len(books)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if books[j][1] < books[min_index][1]:  # Compare by year
                min_index = j
        books[i], books[min_index] = books[min_index], books[i]

# --- User Input ---
num_books = int(input("Enter number of books: "))
books = []

for _ in range(num_books):
    title = input("Enter book title: ")
    year = int(input(f"Enter publication year for '{title}': "))
    books.append((title, year))

# --- Sort & Output ---
start_time = time.time()
selection_sort(books)
end_time = time.time()

print("\nBooks sorted by publication year:")
for title, year in books:
    print(f"{title} ({year})")

print(f"\nExecution time: {end_time - start_time:.6f} seconds")
