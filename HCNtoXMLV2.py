import re


inputFile = 'PATIENTS.IN'
outputFile = 'YMCPhoneV6.xml'

#inputData = open(inputFile,"r")

outputData = open(outputFile,"w+")
outputData.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")


outputData.write('<PhoneBook>' + "\n")

with open(inputFile) as inputData:
   for counter, line in enumerate(inputData):
       #Strip Data From Input
       fName = re.sub(r"\s+$", "", line[44:74]).title()
       sName = re.sub(r"\s+$", "", line[14:44]).title()
       homePh = re.sub('\D', '', line[194:220])
       mobilePh = re.sub('\D', '', line[491:505])

       #Strip Data From Input

       outputData.write('<DirectoryEntry>' + "\n")
       outputData.write("    <Name>{} {}</Name>\n".format(fName, sName))
       outputData.write("    <Telephone>{}</Telephone>\n".format(homePh))
       outputData.write("    <Mobile>{}</Mobile>\n".format(mobilePh))
       outputData.write('    <Ring>0</Ring>' + '\n')
       outputData.write('</DirectoryEntry>' + "\n")
       print(counter)



outputData.write('</PhoneBook>' + "\n")
outputData.close()
