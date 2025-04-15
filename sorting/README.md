# Sorting Algorithms

This folder contains Python implementations of classic sorting algorithms. These are fundamental in both theoretical computer science and real-world applications, helping build a solid understanding of algorithmic efficiency, comparisons, and data manipulation.

---

## 🔗 Algorithms Included

---

### 🔁 Bubble Sort

A simple comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order. It's not the most efficient, but great for understanding basic algorithm mechanics.

**File:** `bubble_sort.py`  
**Concepts:** Adjacent comparison, nested loops  
**Time Complexity:** O(n²)  
**Use Case:** Educational and small datasets

---

### ⚡ Merge Sort

A divide-and-conquer algorithm that splits arrays into halves, recursively sorts them, and then merges the results into a single sorted array.

**File:** `merge_sort.py`  
**Concepts:** Recursion, merging  
**Time Complexity:** O(n log n)  
**Use Case:** Efficient and stable sorting of large datasets

---

### ✍️ Insertion Sort

Builds the final sorted array one item at a time. Great for small or partially sorted datasets.

**File:** `insertion_sort.py`  
**Concepts:** In-place, comparison-based sorting  
**Time Complexity:** O(n²)  
**Use Case:** Efficient on small datasets, commonly used in practice where input is almost sorted

---

### 🔽 Selection Sort

Divides the list into a sorted and unsorted part and repeatedly selects the smallest element from the unsorted part.

**File:** `selection_sort.py`  
**Concepts:** In-place, comparison, selection  
**Time Complexity:** O(n²)  
**Use Case:** Simple to implement but inefficient for large datasets

---

### 🚀 Quick Sort

A highly efficient divide-and-conquer sorting algorithm that picks a pivot and partitions the array into elements less than and greater than the pivot.

**File:** `quick_sort.py`  
**Concepts:** Recursion, partitioning, pivot logic  
**Time Complexity:** Average: O(n log n), Worst: O(n²)  
**Use Case:** Fast, widely used in production environments

---

### 🧮 Radix Sort

A non-comparison-based sorting algorithm that processes individual digits. Useful for sorting large numbers of integers with fixed length.

**File:** `radix_sort.py`  
**Concepts:** Bucketing, digit place sorting  
**Time Complexity:** O(nk), where *k* is the number of digits  
**Use Case:** Sorting large sets of integers efficiently

---

## 💡 Usage

To run any sorting algorithm:

```bash
python filename.py
