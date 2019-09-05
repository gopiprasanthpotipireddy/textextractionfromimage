import numpy as np
import pandas as pd
import  re
import sys
import csv
import os.path
from os import path
from openpyxl import load_workbook


#transfer excel sheet contents to an array using pandas for specific field extraction
df=pd.read_csv(sys.argv[1],header=0,encoding='unicode_escape',engine='python'
, error_bad_lines=False)
applicant_name=(str(sys.argv[1])).split("_")[0]
arr=np.array(df)
arr2=[]
arrx=[]

#fetching only valid lines to an array using regex
regex = re.compile('[@_!#$%^&*()<>?\|}.{~:-]') 
for a in arr:
      if(regex.search(str(a)) == None): 
           arr2.append(str(a))
      else:
           str2=re.sub(regex,'',str(a))
           arrx.append(str2)
      
           
           

arr3=[]





char_list=['\[','\]','\*','\'','\_','~','-']
#Name=re.sub("|".join(char_list),"",str(arr2[0]))
#DOB=re.sub("|".join(char_list),"",str(arr2[2])).strip()
#Pan_Num=re.sub("|".join(char_list),"",str(arr2[4]))

#First_Name=(Name.split(" ",1))[1]
#Last_Name=Name.split(" ",1)[0]
#First_Name_Validated= re.match('([A-Za-z]{2,25})*([\\s*][A-Za-z]{2,25})*',First_Name)
#Last_Name_Validated=re.match('([A-Za-z]{2,25})*([\\s*][A-Za-z]{2,25})*',Last_Name)

#DOB_Validated=re.match('([\d]{1,2}/[\d]{1,2}/[\d]{4})',DOB)
#Pan_Num_Validated=re.match('([^a-zA-Z0-9]*)(\\s*)([a-zA-Z0-9]+)(\.*)',Pan_Num)
#LastName=Last_Name_Validated.group(0)
#FirstName=First_Name_Validated.group(0)
#for a in arr2:
#   if LastName in a:
#           arr3.append(str(a))
    
FatherName="xyz" 
DOB=""
nm=""
for a in arr:
     stt1=re.sub("|".join(char_list),' ',str(a))
     stt2=re.search(applicant_name.lower(),stt1.lower())
     if(stt2 is not None):
       nm=stt1.strip()
#print(nm)
name=re.sub("|".join(char_list),' ',nm)
ln=(nm.strip().split(" ",1))[0]
fn=(nm.strip().split(" ",1))[1]
    
Pan_Num_Validated="" 
for a in arr:
    
     stt1=re.sub("|".join(char_list),' ',str(a))
     #print(stt1)
     str2=re.search(ln,stt1)
     if(str2 is not None):
       FatherName=stt1
     z=re.search('([A-Z]{5}[0-9]{4}[A-Z])',stt1)
     if(z is not None):
         Pan_Num_Validated=stt1
     str3=re.search('([\d]{1,2}/[\d]{1,2}/[\d]{4})',stt1)
     if(str3 is not None):
         DOB = str3
     

     
         
          
     
     

Father_Name_Validated=re.sub("|".join(char_list),"",FatherName)
#Father_Name_Validated=re.match('([A-Za-z]{2,25})*([\\s*][A-Za-z]{2,25})*',FatherName)
print("Name: "+name)
#print("Last Name: "+ln)
#print("Father Name: "+Father_Name_Validated)
print("Date Of Birth: "+DOB.group(0))
print("Pan Number: "+Pan_Num_Validated)






FName=fn
LName=ln
FathName=Father_Name_Validated
Dtofbirth=DOB.group(0)
PnNum=re.sub("|".join(char_list),"",Pan_Num_Validated)

#Writing to a CSV File
df2 = pd.DataFrame({'Name':[name],'DOB':[Dtofbirth],'Pan Number':[PnNum]}) 
writer = pd.ExcelWriter(sys.argv[2], engine='openpyxl')
#writer.book = book
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







