def gradeStudents(grades): 
    for i in range(len(grades)):
        if(grades[i]>37):
            if((grades[i]%5)!=0):
                if(5-(grades[i]%5)<3):
                    grades[i]+=5-(grades[i]%5)
    print (grades)




n=int(input())   #number of students
grades=[]
for i in range(n):
    enter_grade=int(input().strip())
    grades.append(enter_grade)
result=gradeStudents(grades)