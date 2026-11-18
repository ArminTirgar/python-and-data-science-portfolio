if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    sorted_grades = sorted(set(student[1] for student in students))
    second_lowest_students=[]
    
    for student in students:
        if student[1]==sorted_grades[1]:
            second_lowest_students.append(student[0])
    
    second_lowest_students = sorted(second_lowest_students)
    
    for student in second_lowest_students:
        print(student)
    
    
        
        
        
    