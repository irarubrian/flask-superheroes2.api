//GRADE.js
getGrade(marks)
This function receives the marks as input and returns a grade based on the provided range:

Marks > 79 -> Grade "A"
Marks between 60 and 79 -> Grade "B"
Marks between 50 and 59 -> Grade "C"
Marks between 40 and 49 -> Grade "D"
Marks < 40 -> Grade "E"
promptForMarks()
This function prompts the user to enter a number between 0 and 100. If the input is invalid (not a number or out of range), it will ask the user to try again. Once a valid input is entered, it calculates and displays the grade.


//SALARY.js
calculateNetSalary(basicSalary, benefits)
This function calculates the net salary based on the following steps:

Gross Salary: It is the sum of basic salary and benefits.
Tax Deduction: Tax is calculated at a rate of 20% of the gross salary.
NHIF Deduction: NHIF is calculated at a rate of 10% of the gross salary.
NSSF Deduction: NSSF is calculated at a rate of 20% of the gross salary.
Net Salary: The net salary is calculated by subtracting the total deductions (tax, NHIF, and NSSF) from the gross salary.
The function returns an object containing:

grossSalary: The sum of basic salary and benefits.
tax: The tax deduction.
nhif: The NHIF deduction.
nssf: The NSSF deduction.
netSalary: The final net salary after deductions.

SPEED.js

The program first takes the speed of the car as input using prompt-sync.
It then calculates the demerit points by subtracting 70 from the speed and dividing the result by 5.
If the speed is below 70, it prints "Ok".
If the speed exceeds 70, it prints the number of demerit points.
If the points exceed 12, it prints "License suspended".


