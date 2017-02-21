def rmdir(directory):
	if not os.path.exists(directory):
		print("directory is not present")
	else:
		shutil.rmtree(directory)
		print(" directory has been removed")