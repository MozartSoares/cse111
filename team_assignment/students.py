import csv
from pprint import pprint
def main():
    filepath = 'students.csv'
    students_map = read_dictionary(filepath)
    
    number = input("Insert an I-Number to find the student: ")
    try:
        student = students_map[number]
        print(student)
    except:
        print('No such student')
        main()


def read_dictionary(filepath):
    with open(filepath,'r') as file:
        reader = csv.reader(file)
        next(reader)
        students_list = {}
        
        for row in reader:
            if len(row) != 0 : 
                number = row[0]
                student = row[1]
                students_list[number] = student
    return students_list


if __name__ == "__main__":
    main()
# STUDENTS = {
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
#   'i_number': 'student_name'
# } 

