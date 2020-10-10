# Paul Caulfield, 2020
import csv
# import csv package

employee_file = open('employee_file.csv', mode='w') 
# open file and name it 'employee.csv and set the file mode = w for write - to create blank csv file
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# make virable called employee.writer which uses csv writer to write to (filename,delimite and other paramters)

employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# to write row, pass list
employee_writer.writerow(['Erica Meyers, what', 'IT', 'March'])
# write another row
employee_file.close()
# close file