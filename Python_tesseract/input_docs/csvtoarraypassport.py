import numpy as np
import pandas as pd
import  re
import sys
import csv
import os.path
from os import path
from openpyxl import load_workbook


#transfer excel sheet contents to an array using pandas for specific field extraction
df=pd.read_csv(sys.argv[1],header=None,encoding ='unicode_escape',engine='python',error_bad_lines=False)

arr=np.array(df)
char_list=['\[','\]','\*','\'','\_']
Passport_Number=re.sub("|".join(char_list),"",str(arr[0])).strip()
#DOB=re.sub("|".join(char_list),"",str(arr[2])).lstrip()
#Pan_Num=re.sub("|".join(char_list),"",str(arr[4])).lstrip()
#Father_Name=re.sub("|".join(char_list),"",str(arr[1])).rstrip('\~')
First_Name=re.sub("|".join(char_list),"",str(arr[2])).rstrip('\~')
Last_Name=re.sub("|".join(char_list),"",str(arr[1])).rstrip('\~')

print("First Name: "+First_Name)
print("Last Name: "+Last_Name)
#print("Father Name: "+Father_Name)
#print("Date Of Birth: "+DOB)
print("Passport Number: "+Passport_Number)


df2 = pd.DataFrame({'First Name':[First_Name],'Last Name':[Last_Name],'Passport Number':[Passport_Number]}) 
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
    print(path.exists(sys.argv[2]))
    df2.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    writer.close()



#Writing to a CSV File 

#csvData = [['First Name', 'Last Name''Passport Number'], [First_Name,Last_Name,Passport_Number]]
#with open(sys.argv[2], 'w') as csvFile:
#    writer = csv.writer(csvFile)
#    writer.writerows(csvData)
#csvFile.close()
