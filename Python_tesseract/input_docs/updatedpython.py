import sys
import os
from PIL import Image
from wand.image import Image as Img
from pathlib import Path
import pytesseract
import argparse
import cv2
import os
import pandas
import numpy as np
import re
import subprocess

    
def loop_folder():
        output_dir='C://Users/jayachandrikam/Desktop/Python_tesseract/output_docs/'
        root_dir='C://Users/jayachandrikam/Desktop/Python_tesseract/input_docs/'
        for filename in os.listdir(root_dir):
             
             if(filename.endswith(".pdf")):
                    input_abs_file_path=str(filename).replace("\\","/")
                    fname=input_abs_file_path.split(".")[0]
                    output_image=root_dir+fname+".jpg"
                    output_cropped_image=root_dir+fname+"_cropped.jpg"
                    ocr_output=root_dir+fname+"_out.csv"
                   
                    print (input_abs_file_path)
                    print(fname)
                    subprocess.call(['python.exe','pdftoimage.py',input_abs_file_path,output_image])
                    #pdftoimage(input_abs_file_path,output_image)
                    subprocess.call(['python.exe','cropimage.py',output_image,output_cropped_image])

                    #cropimage(output_image,(1,1000,3000,2530),output_cropped_image)
                    subprocess.call(['python.exe','pancardocr.py',output_cropped_image,"blur"])
                    #ocr(output_cropped_image,"blur")
                    subprocess.call(['python.exe','removemptylines.py',ocr_output])
                    #remove_empty_lines(ocr_output)
        for filename in os.listdir(root_dir):
             if(filename.endswith(".csv")): 
                    print(filename)
                    category=filename.split("_")[1]
                    #print(category)
                    
                    if(category=="pan"):
                          final_output=output_dir+filename.split("_")[0]+"_Final_out.xlsx"
                    
                          subprocess.call(['python.exe','csvtoarray.py',filename,final_output])
                          #pancard_csvtoarray(filename)
                    elif(category=="adhar"):
                          final_output=output_dir+filename.split("_")[0]+"_Final_out.xlsx"
                          #print("category")
                          subprocess.call(['python.exe','csvtoarrayadhar.py',filename,final_output])
                          #adharcard_csvtoarray(filename)
                    else:
                          final_output=output_dir+filename.split("_")[0]+"_Final_out.xlsx"
                          subprocess.call(['python.exe','csvtoarraypassport.py',filename,final_output])
                        
                          

    
if __name__=="__main__":
	loop_folder()


      
	
 


