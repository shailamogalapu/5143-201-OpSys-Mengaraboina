def grep(filename,searchphrase):
	 if os.path.exists(filename):
	 	searchfile = open(filename)
		for line in searchfile:
   		 if searchphrase in line: 
			print line
		 else:
			print("keyword doesnt exist")
		searchfile.close()
	 else:
		print("file doesnot exist")