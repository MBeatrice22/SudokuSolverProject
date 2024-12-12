score = int(input("Enter the student's score: "))
if 0 <= score <=100: #ne asigura ca punctajul este intre 0 si 100
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'

    print(f"The student's grade is: {grade}")
else:
    print("Invalid score. Please enter a score between 0 and 100")