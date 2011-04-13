import os

text = "Numele meu este MERGE1. Prenumele meu este MERGE2"
print "Before : "+text
dict = {'MERGE1': 'Dragos', 'MERGE2': 'Dimitriu'}
for key in dict:
	text = text.replace(key, dict[key])
print "After : "+text

print os.path.abspath('')

	

