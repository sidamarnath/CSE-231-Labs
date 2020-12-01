###########################################################
# Computer Lab #6
# Algorithm
# Asks user to input a file 
# Reads the file
# Displays averages for each student and each exam
###########################################################
# Opens the file and reads the file
fp =open("scores.txt", "r")
# student_list set to an empty list
student_list = []
# Setting exam values to 0
exam_1 = 0 
exam_2 = 0
exam_3 = 0
exam_4 = 0
# For loop to loop through each line in the list
for line in fp:
    # Converts the list to a tuple
    student_data = tuple(line.split())
    first_exam = int(student_data[2])
    second_exam = int(student_data[3])
    third_exam = int(student_data[4])
    fourth_exam = int(student_data[5])
    
    # Calculating averages for each student exam scores
    student_exam_total = (first_exam + second_exam + third_exam + fourth_exam) 
    student_exam_avg = student_exam_total / 4
    # Converts data back to a list
    info_list = list(student_data)
    # Putting student exam average into the list
    info_list.append(student_exam_avg)
    # Converting list back into a tuple
    student_data = tuple(info_list) 
    
    student_list.append(student_data)
    # Sorting the list alphabetically
    student_list.sort()
    # Adding all the exam 1, exam 2, exam 3, exam 4 values and computes avg
    exam_1 += int(student_data[2])
    exam_2 += int(student_data[3])
    exam_3 += int(student_data[4])
    exam_4 += int(student_data[5])
exam_1_avg = exam_1 / 5
exam_2_avg = exam_2 / 5
exam_3_avg = exam_3 / 5
exam_4_avg = exam_4 / 5
 
#Displays results   
print("{:20s}{:6s}{:6s}{:6s}{:6s}{:6s}".format("Name", " Exam1", " Exam2", " Exam3", " Exam4", "     Mean"))
for data in student_list:
    l_name = data[0]
    f_name = data[1]
    name = l_name + " " + f_name
    
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}".format(name, int(data[2]), int(data[3]), int(data[4]), int(data[5]), float(data[6])))  
# Displays exam averages    
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}".format("Exam Mean",exam_1_avg, exam_2_avg, exam_3_avg, exam_4_avg))
# Closes the file pointer (fp)
fp.close()         

        
    


   
