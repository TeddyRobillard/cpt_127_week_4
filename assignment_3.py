'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
#%%
with open('student_grades.csv', 'r') as f:

    # collect all lines from the file
    lines = f.readlines()


    # validate file has data
    if len(lines) > 0:
        grades = []

    
    
        # split the line into a list (i.e. columns)
        for line in lines[1:]:
         
            row = line.split(',')
     
            # convert the grade to a float and add it to the list
            grade = float(row[3].replace('\n',''))
            grades.append(grade)
        avg = sum(grades) / len(grades)

        
       #% %
    
    #%%
    with open('student_grade_differences.csv', 'a') as out_f:
        for line in lines[1:]:
            row = line.split(',')
            grade = float(row[3].replace('\n', ''))
            
            # calculate the difference from the average
            gradediff = grade - avg
            gradediff = str
            out_f.write(f"{row[0]},{row[1]},{row[2]},{gradediff}\n")