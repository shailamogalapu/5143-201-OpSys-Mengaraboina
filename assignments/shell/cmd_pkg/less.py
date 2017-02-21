def less(filename):
	if os.path.exists(filename):                                           
		f = open(filename, "r")
		text = f.readline()
		lines=0
		for line in f:
			if lines==20:	
				user = raw_input("type in yes to continue ")
				if user == "yes":
					lines = 0
					continue
				else:	
					break
			else :
				print line
				lines=lines+1
	else:
		print("file doesnt exists")