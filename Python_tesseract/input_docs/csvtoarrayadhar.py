import numpy as np
import pandas as pd
import  re
import sys
import csv
import os.path
from os import path
from openpyxl import load_workbook

#transfer excel sheet contents to an array using pandas for specific field extraction
df=pd.read_csv(sys.argv[1],header=0,encoding ='unicode_escape',engine='python')
applicant_name=str(sys.argv[1]).split("_")[0]
print(applicant_name)
arr=np.array(df)
char_list=['\[','\]','\*','\'','\_']
Name=re.sub("|".join(char_list),"",str(arr[2]))
#DOB=re.sub("|".join(char_list),"",str(arr[3])).split(":")[1].lstrip()


Adhar_Num=re.sub("|".join(char_list),"",str(arr[5]))
Name_Validated= re.match('([A-Za-z]{2,25})*([\\s*][A-Za-z]{2,25})*',Name)
#DOB_Validated=re.match('([\d]{1,2}/[\d]{1,2}/[\d]{4})',DOB)
Adhar_Num_Validated=re.match('([\d]{1,4}\\s+[\d]{1,4}\\s+[\d]{1,4})',Adhar_Num)
#print("Name: "+Name_Validated.group(0))
#print("Date Of Birth: "+DOB_Validated.group(0))
#print("Adhar Number: "+Adhar_Num_Validated.group(0))


#print(First_Name_Validated.group(0))
#print(First_Name)
#print((re.match('([A-Za-z]{2,25})*([\\s*][A-Za-z]{2,25})*',First_Name)))
#print(re.match('([^a-zA-Z0-9]*)(\\s*)([a-zA-Z0-9]+)(\.*)',Pan_Num))

m="Male"
f="Female"
gender=""
DOB_validated=""
adhar=""
adhar_name=""

for a in arr:
    
     stt1=re.sub("|".join(char_list),' ',str(a))
     #print(stt1)
     str2=re.search(m,stt1)
     if(str2 is not None):
       gender=m
     else:
       gender=f
     str3=re.search('([\d]{1,2}/[\d]{1,2}/[\d]{4})',stt1)
     str4=re.search('[\d]{4}\\s+[\d]{4}\\s+[\d]{4}',stt1)
     str5=re.search(applicant_name.lower(),stt1.lower())
     if(str3 is not None):
         DOB_Validated = str3
     if(str4 is not None):
         adhar=str4.group(0)
     if(str5 is not None):
         adhar_name=stt1
         
print("Date Of Birth: "+DOB_Validated.group(0))
print("Adhar Number: "+adhar)
print("name: "+adhar_name)




#Writing to a CSV File
df2 = pd.DataFrame({'Name':[adhar_name],'Adhar Number':[adhar],'Gender':[gender],'DOB':[DOB_Validated.group(0)]}) 

writer = pd.ExcelWriter(sys.argv[2], engine='openpyxl')
if path.exists(sys.argv[2]):
    book = load_workbook(sys.argv[2])
    writer.book = book
    
  
    xl = pd.ExcelFile(sys.argv[2])
    res = len(xl.sheet_names)
    df2.to_excel(writer, sheet_name='Sheet'+str(res+1))
    writer.save()
    writer.close()
else:
   
    df2.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    writer.close()


#Writing to a CSV File 

#csvData = [['Name','DOB','Adhar Number'], [Name_Validated.group(0),DOB_Validated.group(0),Adhar_Num_Validated.group(0)]]
#with open(sys.argv[2], 'w') as csvFile:
#    writer = csv.writer(csvFile)
#    writer.writerows(csvData)
#csvFile.close()
