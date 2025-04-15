import time

def bubble_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if students[j][1] > students[j + 1][1]:  # Compare by score
                students[j], students[j + 1] = students[j + 1], students[j]

# --- User Input ---
num_students = int(input("Enter number of students: "))
students = []

for _ in range(num_students):
    name = input("Enter student name: ")
    score = int(input(f"Enter {name}'s score: "))
    students.append((name, score))  # Tuple format: (name, score)

# --- Execution & Output ---
start_time = time.time()
bubble_sort(students)
end_time = time.time()

print("\nSorted students by score:")
for name, score in students:
    print(f"{name}: {score}")

print(f"\nExecution time: {end_time - start_time:.6f} seconds")
