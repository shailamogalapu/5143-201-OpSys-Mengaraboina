def mv(filename1,filename2):
	 if(os.path.isfile(filename1)):
		cp(filename1,filename2)
        	rm(filename1)
       	        print "Moved the file"
	 else:
		print("files doesnt exist")