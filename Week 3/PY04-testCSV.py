############################

import csv
employee_file = open('c:/Users/Eimear/Documents/GitHub/Sem_4_DataRepresentation_Assignments/employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',',quotechar ='"', quoting=csv.QUOTE_MINIMAL)
employee_writer.writerow(['John smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Myers', 'IT', 'March'])
employee_file.close()

employee_file = open('c:/Users/Eimear/Documents/GitHub/Sem_4_DataRepresentation_Assignments/employee_.csv', mode='w')

