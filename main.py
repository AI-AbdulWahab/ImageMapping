import cv2
import csv
ID = input("Please enter patient ID: ")
print("Patient ",ID)
path1 = "pexels-eberhard-grossgasteiger-443446.jpg"
image = cv2.imread(path1)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
path2 = "2.png"
image2 = cv2.imread(path2)
image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
header = ['Patient ID', 'Image 1', 'Image 2']

data = [ID, path1, path2]
filename = 'Patient.csv'
with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
file.close()
# with open(filename, 'w') as file:
#     for header in header:
#         file.write(str(header)+', ')
#     file.write('n')
#     for row in data:
#         for x in row:
#             file.write(str(x)+', ')
#         file.write('n')

