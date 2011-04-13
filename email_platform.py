import fileinput
import os
import csv

def getNume(id):
	return id.split('.')[1].upper()

def getPrenume(id):
	return id.split('.')[0].upper()
	
DIR='emails/Stei'
if not os.path.exists(DIR):
	os.makedirs(DIR)


student_info = csv.reader(open('stei.csv', 'rb'), delimiter=',', quotechar='"')
for row in student_info:
	dict = {}
	studentId = row[0]
	studentName = getNume(studentId)
	studentSurname = getPrenume(studentId)
	studentEmail = row[3]
	studentGroup = row[4]
	studentPassword = row[5]
	
	dict['MERGE1'] = studentName
	dict['MERGE2'] = studentSurname
	dict['MERGE3'] = studentId
	dict['MERGE4'] = studentPassword
	
	filename = studentId.replace('.','') + '.html'	
	filename_full_path = DIR+'/'+ filename
	
	outFile = open(filename_full_path, 'w')
	inFile = open('email_platform.html', 'r')
	
	line_out=''
	for line in inFile:
		line_out = line
		for key in dict:
			if line_out == '':
				line_out = line.replace(key,dict[key])
			else:
				line_out = line_out.replace(key,dict[key])
		outFile.write(line_out)
		line_out=''
	
	#Create general index.html
	filename_index_part = DIR + '/' +'index.html'
	index_part = open(filename_index_part,'a')
	link_html = "<a href=\""+filename+"\">" + "Email trimis cursantului la data de 04.04.2011" + "</a>"
	data = studentName+'&nbsp;'+studentSurname+'&nbsp;'+link_html+'<br/>'
	index_part.write(data)
	index_part.close()
	inFile.close()
	outFile.close()










