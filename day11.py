if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    grades = sorted(set([student[1] for student in students]))
    second_lowest_grade = grades[1]

    # Find the students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    second_lowest_students.sort()  # Sort the names alphabetically

    # Print the names of the students with the second lowest grade
    for student in second_lowest_students:
        print(student)