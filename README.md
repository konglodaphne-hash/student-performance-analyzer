# student-performance-analyzer
A program that asks a student for his subject grades and displays the result using functions
A simple Python  application that collects student academic marks across 5 subjects, calculates the average score, assigns a letter grade, and outputs a formatted performance summary.

WHAT THE PROGRAM DOES
First it prompts for the student's name.

Iteratively requests 5 subject names and their corresponding numerical scores.

Computes the total and average score across all subjects.

Evaluates the average to assign a letter grade (GRADE A through GRADE F).

Determines academic outcome (PASS or FAIL based on a score threshold of 50).

Prints an organized summary report in the terminal.

FUNCTIONS IN THE PROGRAM AND THEIR CORRESPONDING USE
get_student_name()     -     Prompts the user for the student's name and returns it as a string.

get_score(subject)     -     Accepts a subject name parameter, prompts for the score, and returns it as a float.

calculate_average(scores)  - Takes the list of numerical scores, computes the sum, and returns the average score.

determine_grade(average)  -  Accepts the calculated average and returns the matching grade (GRADE A to GRADE F).

determine_status(average) -  Evaluates the average against the passing score (50) and returns "PASS" or "FAIL".

display_report(name, subjects, scores, avg, grade, status)  -  Takes all gathered data and formats it into a clean, readable summary table.

main()        -          Controls the primary program execution flow, orchestrating function calls in order.

How to Run the Program
Save the Script: Save your Python script as student_analyzer.py.
Open Terminal and run program.
