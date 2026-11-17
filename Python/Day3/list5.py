students = [("tapu", 88), ("sonu", 95), ("goli", 72), ("pinku", 78)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Students sorted by marks (highest to lowest):")
print(sorted_students)