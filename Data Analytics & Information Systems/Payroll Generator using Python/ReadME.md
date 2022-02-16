- To design a python program to process departmental payroll. The 
program will read payroll-related data from a CSV-formatted input file (payroll_input.csv) and 
write the output to the console as well as to a CSV-formatted output file named
(payroll_output.csv).

**Program Requirements:**
- 1. The department hires only hourly employees. 
- 2. The ‘payroll_input.csv’ data file includes employee’s name, weekly hours worked, and 
regular hourly pay rate. The file contains three lines of payroll data for each 
employee. The first line is employee name, the second lists the weekly hours worked, 
and the third line includes the employee's hourly pay rate. Thus, each group of three 
lines represents one employee's payroll record. The input file also uses a special 
sentinel record (last record that is different from all other records in the file) to indicate 
the end of file. When the program reads a line with the word 'EOF', it indicates that 
there are no more employee records left to be read and processed. Thus, 'EOF' in the 
input file is used to indicate the end of input file or no more records to process. 
- 3. For each hourly employee included in the input CSV data file:

-  a. Normal or regular weekly hours cannot exceed 40.00 hours. Any hours over 40.00
are to be paid at an overtime pay rate. The multiplier for overtime pay is 1.5, 
meaning 1.5 times the regular hourly pay rate. 
-  b. An employee is paid at regular hourly pay rate when the employee has worked less 
than or equal to 40.00 hours a week (regular weekly hours). Maximum regular 
hours per week is to be defined as a constant of 40.00.
-  c. Regular Gross Pay = regular weekly hours worked * regular hourly pay rate 
-  d. When an employee has worked overtime (weekly hours worked > maximum regular 
hours), the employee is paid at the regular hourly pay rate for the first 40.00 hours. 
Overtime is paid at 1.5 times the regular hourly pay rate per hour of overtime. 
Overtime hours are hours worked in excess of maximum regular hours.
-  e. Overtime Gross Pay = overtime hours worked * overtime multiplier * regular hourly 
rate
-  f. Total Gross Pay is the sum of Regular Gross Pay and Overtime Gross Pay. 
-  g. Tax to withhold = Total Gross Pay * (Tax Rate/100), where Tax Rate % is 
determined by the following table (Note: tax rates and thresholds for each tax 
bracket must be declared as constants e.g. TAX_THRESHOLD_LOW = 12.00, 
TAX_RATE_BELOW_12 = 10, etc.)
-  h. Deduction to withhold = Total Gross Pay * (Deduction Rate/100), where the 
Deduction Rate % is determined by the following rule. (Deduction threshold and 
Deduction Rates must be declared as constants, e.g. DEDUCTION_THRESHOLD
= 800.00, DEDUCTION_RATE_LOW = 2, DEDUCTION_RATE_HIGH = 5
-  i. Net pay = Total Gross Pay – Tax to Withhold – Deduction to withhold
-  j. Display results on console in the following sequence. All data must be properly 
formatted. All currency values must be displayed with $ sign and to 2 decimal 
places. All floating point, non-currency, numeric values must be rounded to 2 
decimal places. All numeric values must be aligned on the decimal point.
      a. employee’s name,
      b. regular hours worked,
      c. regular hourly pay rate,
      d. regular Gross Pay,
      e. overtime hours worked (would be zero if no overtime was worked)
      f. overtime hourly pay rate, (Overtime pay rate will be displayed even when no 
      overtime was worked)
      g. overtime gross pay
      h. total gross pay, 
      i. taxes withheld, 
      j. deductions withheld, and the
      k. net pay 
- k. In addition to displaying each employee’s results on console, write these results to a 
CSV-formatted output file named (payroll_output.csv). So, each line in the output 
will include employee name, regular hours worked, regular hourly pay rate, regular 
gross pay, overtime hours worked, overtime hourly pay rate, overtime gross pay, 
total gross pay, taxes withheld, deductions withheld, and net pay. There will be 
one line per employee in the output file. Each value will be separated from the 
next with a comma. All numeric values are to be rounded to 2 decimal places. 
Currency values will be also be rounded to 2 decimal places. Since this CSV output 
file will be used as an input file in another application, no formatting should be 
applied to the data written to this CSV output file.
- 4. Print the end of program execution informative message that indicates the number of 
employee records processed for payroll to the console (see sample console output
above).
- 5. The program should be designed to process any number employee records, not 
just the seven included in the input file for testing your program. 
- 6. A sample of two employee records in the payroll_output file to check your output 
against. Because you are not formatting data, it is possible that numeric values may 
show only 1 decimal place if values in both decimal places are zero (it may show 
40.00 as 40.0 or 0.00 as 0.0 or 639.10 as 639.1).
