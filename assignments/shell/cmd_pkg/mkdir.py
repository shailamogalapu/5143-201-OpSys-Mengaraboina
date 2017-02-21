def mkdir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("directory has been created")
	else:
	        print("directory already exists")