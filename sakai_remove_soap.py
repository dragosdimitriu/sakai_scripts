import os
import sys
from SOAPpy import WSDL
import csv

loginsoap = WSDL.SOAPProxy("http://portal.cpaddd.ro/sakai-axis/SakaiLogin.jws?wsdl")
scriptsoap = WSDL.SOAPProxy("http://portal.cpaddd.ro/sakai-axis/SakaiScript.jws?wsdl")

sessionid = loginsoap.login("admin", "admin@sakai#cpaddd2011")
print "Session ID : ", sessionid

student_info = csv.reader(open('students.csv', 'rb'), delimiter=',', quotechar='"')
for row in student_info:
	print 'Student_ID : ',row[0]
	studentId = row[0]
	print 'Nume : ',row[1]
	studentName = row[1]
	print 'Prenume : ',row[2]
	studentSurname = row[2]
	print 'Email : ',row[3]
	studentEmail = row[3]
	print 'Grup : ',row[4]
	studentGroup = row[4]
	print 'Parola : ',row[5]
	studentPassword = row[5]
	print 'Curs : ',row[6]
	courseID = row[6]
	if (scriptsoap.checkForUser(sessionid, studentId)):
		#if exists remove user
		codeRemove = scriptsoap.removeUser(sessionid,studentId)
		if (codeRemove == 'success'):
			print '[OK][User removed] Username: ',studentId
		else:
			print '[ERROR][User removed] Username: ',studentId
	print '-----------------------------------------------------------------'