#!/usr/bin/env python
import os
import sys
import threading
def cat1(filename1,filename2,filedest):
     if os.path.exists(filename1):
	if os.path.exists(filename2):
		fread=open(filename1,'r')
        	content=fread.read()
        	fread1=open(filename2,'r')
		content1=fread1.read()
		fread2=open(filedest,'w')
      	        fread2.write(content)
         	fread2.write(content1)
                fread.close()
                fread1.close()
        	fread2.close()
        else:
        	print("file doesnt exist")
     else:
		print("file doesnt exist")
