def main():

 print("=================================================")
 print("         STUDENT PERFORMANCE ANALYZER            ")
 print("=================================================")


 def get_student_name():
    name = input("Enter student name: ")
    return name
 student_name = get_student_name()
 print(f"STUDENT NAME: {student_name}")



 def get_score(subject):
    return float(input(f"Enter {subject} score: "))
 subject_name = []
 student_scores = []
 for i in range(1,6):
    sub_name = str(input(f"Enter subject {i}: "))
    scores = get_score(sub_name)
    student_scores.append(scores)
    subject_name.append(sub_name)


 def calculate_average(scores):
    total_score = 0
    subject_number = 0
    for scor in scores:
        total_score = total_score + scor
        subject_number = subject_number + 1
    return total_score / subject_number
    
 average = calculate_average(student_scores)
 print(f"AVERAGE SCORE: {average}")

 def determine_grade(average):
    if average >= 80:
        return  "GRADE A"
    elif average >= 70:
        return "GRADE B"
    elif average >= 60:
        return "GRADE C"
    elif average >= 50:
        return "GRADE D"
    else:
        return "GRADE F"
 student_grade = determine_grade(average)
 print(f"Your Grade is {student_grade}")


 def determine_status(average):
    if average >= 50:
        return "PASS"
    else:
        return "FAIL"

 status = determine_status(average)
 print(f"GRADE STATUS: {status}")


 def display_report(name, subjects, scores, avg,  grade, status):
    print("================")
    print("    PERFORMNCE REPORT     ")
    print("================")
    print(f"NAME: {name}")
    print("SUBJECTS: ")
    for indx in range(5):
        print(f"{subjects[indx]} : {scores[indx]}" )
    print(f"GRADES: {grade}")
    print(f"STATUS: {status}")

 display_report(student_name, subject_name, student_scores, average, student_grade, status)


main()