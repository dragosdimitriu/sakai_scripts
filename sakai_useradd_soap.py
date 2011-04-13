import os
import sys
from SOAPpy import WSDL
import csv

def getNume(id):
	return id.split('.')[1].upper()

def getPrenume(id):
	return id.split('.')[0].upper()

courseDict = {'C1':'d846e113-2152-4de7-846a-870c61267029', 'C2' : 'ad5de95b-b2d7-4d17-a70e-89bd2ea0104c', 'C3':'02289385-e22c-4ab9-8fef-f17c4e112791', 'C4' : 'd23a74bf-51a4-48a3-bd29-ce1da6af1fe7', 'C5':'ab2306dc-2de5-4e84-9b74-e1a827ef6db8', 'C6':'c4a8e7b8-abde-4b55-a48f-8271817820b8', 'C7':'1fe6f29e-53cc-48f4-a175-8101a81ed18f', 'M1':'76a20ecd-1dd2-4240-9d1d-e336fd5f7807'}

loginsoap = WSDL.SOAPProxy("http://portal.cpaddd.ro/sakai-axis/SakaiLogin.jws?wsdl")
scriptsoap = WSDL.SOAPProxy("http://portal.cpaddd.ro/sakai-axis/SakaiScript.jws?wsdl")

sessionid = loginsoap.login("admin", "")
print "Session ID : ", sessionid

groupClujDict={}
for value in courseDict:
	siteid = courseDict[value]
	grouptitle = 'BAIA_MARE_S1_2011'
	groupdesc = 'Studeti Baia Mare - Seria 1 - an 2011'
	groupId = scriptsoap.addGroupToSite(sessionid, siteid, grouptitle, groupdesc)
	groupClujDict[value] = groupId
	print 'BAIA_MARE_S1_2011 added to site ',value
	
student_info = csv.reader(open('baia_mare.csv', 'rb'), delimiter=',', quotechar='"')
for row in student_info:
	print 'Student_ID : ',row[0]
	studentId = row[0]
	print 'Nume : ',getNume(studentId)
	studentName = getNume(studentId)
	print 'Prenume : ',getPrenume(studentId)
	studentSurname = getPrenume(studentId)
	print 'Email : ',row[3]
	studentEmail = row[3]
	print 'Grup : ',row[4]
	studentGroup = row[4]
	print 'Parola : ',row[5]
	studentPassword = row[5]
	print 'Curs : ',row[6]
	courseID = row[6]
	if (scriptsoap.checkForUser(sessionid, studentId)):
		#if exists add to Site
		codeAddtoSite = scriptsoap.addMemberToSiteWithRole(sessionid, courseDict[courseID], studentId, "Student")
		if (codeAddtoSite == 'success'):
			userId = scriptsoap.getUserId(sessionid, studentId)
			print '[OK][Add to Site] Username: ',studentId
		else:
			print '[ERROR][Add to site] Username: ',studentId
	else:
		#else add student first 
		codeCreate  = scriptsoap.addNewUser(sessionid, studentId, studentName, studentSurname, studentEmail, studentGroup, studentPassword )
		if (codeCreate == 'success'):
			userId = scriptsoap.getUserId(sessionid, studentId)
			print '[OK][User create] Username: ',studentId
		else:
			print '[ERROR][User create] Username: ',studentId
		#now add to Site
		codeAddtoSite = scriptsoap.addMemberToSiteWithRole(sessionid, courseDict[courseID], studentId, "Student")
		if (codeAddtoSite == 'success'):
			print '[OK][Add to Site] Username: ',studentId
		else:
			print '[ERROR][Add to site] Username: ',studentId
			
	ret = scriptsoap.addMemberToGroup(sessionid, courseDict[courseID], groupClujDict[courseID], userId)
	print '-----------------------------------------------------------------'
	




	
	