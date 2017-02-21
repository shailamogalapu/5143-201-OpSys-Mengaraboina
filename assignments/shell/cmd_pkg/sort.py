def sort(file):
	 if os.path.exists(file):
		with open(file) as f:
			for line in sorted(f):
        			print (line)
	 else:
		print("file doesnt exist")