
#!/usr/bin/env python
import cmd_pkg
from cmd_pkg import commands
import threading
import os
import sys
import stat
import time
import shutil
import subprocess

command_history = []
command_new=[]

if __name__=="__main__":
	number_commands = 0
	while True:
		parts = []
		x=[]
		cmd = raw_input("% " )
		parts=cmd.split(" ")
		command_history.append(cmd)
		command_new.append(parts[0])
		x=list(parts[0])
		if parts[0]=='rm':
				if(len(parts)==1) | (len(parts)>2):
					print("invalid rm command")
                elif(len(parts)==2):
					files=parts[1]
					c=threading.Thread(target=commands.rm.rm,args=(files,))
					c.start()
					c.join()
		elif parts[0] == 'pwd':
			c = threading.Thread(target=commands.pwd.pwd)
			c.start()
			c.join()
		elif parts[0] == 'mv':
			file1 = parts[1]
			file2 = parts[2]
			c = threading.Thread(target=commands.mv.mv, args=(file1, file2,))
			c.start()
			c.join()
		elif parts[0]=='tail':
			c=threading.Thread(target=commands.tail.tail,args=(parts[1],))
			c.start()
			c.join()
		elif parts[0]=='grep':
			c=threading.Thread(target=grep,args=(parts[2],parts[1],))
			c.start()
			c.join()
		elif x[0]=='!':
			c=threading.Thread(target=previoushistory,args=(parts[0],))
			c.start()
			c.join()
		elif parts[1]=='>':
			output=subprocess.check_output(parts[0],parts[2])
			print output
			c=threading.Thread(target=parts[0])
			c.start()
			c.join()
			c=threading.Thread(target=commads.redirect.redirect,args=(parts[2],))
			c.start()
			c.join()

		elif parts[0]=='less':
			c=threading.Thread(target=commands.less.less,args=(parts[1],))
			c.start()
			c.join()

		elif parts[0]=='ls':
				if(len(parts)==1):
					c=threading.Thread(target=ls)
					c.start()
					c.join()
		                elif len(parts)==2:
					files=parts[1]
					c=threading.Thread(target=commands.lsfun.lsfun,args=(files,))
					c.start()
					c.join()
                		else:
					files=parts[2]
					c=threading.Thread(target=redirect,args=(files,))
					c.start()
					c.join()
		elif parts[0]=='history':
				if len(parts)==1:
					c=threading.Thread(target=history)
					c.start()
					c.join()
				else:
					print("Needs only 1 arguments")
		elif parts[0] == 'who':
			c = threading.Thread(target=who)
			c.start()
			c.join()
		elif parts[0]=='cd':
			if (len(parts)==1) | (len(parts)>2):
				print("invalid cd command")
			elif(len(parts)==2):
				files=parts[1]
				c=threading.Thread(target=cd,args=(files,))
				c.start()
				c.join()
		elif parts[0] == 'cat':
			if (len(parts)==2):
				file = parts[1]
				c = threading.Thread(target=cat, args=(file,))
				c.start()
				c.join()
			elif (len(parts)==5):
				file1=parts[1]
				file2=parts[2]
				file3=parts[4]
				c=threading.Thread(target=cat1,args=(file1,file2,file3,))
				c.start()
				c.join()
		elif parts[0] == 'chmod':
			flag1 = parts[1]
			flag2 = parts[2]
			c = threading.Thread(target=chmod, args=(flag1, flag2,))
			c.start()
			c.join()			
		elif parts[0] == 'cp':
			file1 =parts[1]
			file2 = parts[2]
			c = threading.Thread(target=cp, args=(file1,file2,))
			c.start()
			c.join()
		elif parts[0]=='wc':
				if(len(parts)==1) | (len(parts)>2):
					print("invalid wc command")
                elif(len(parts)==2):
					files=parts[1]
					c=threading.Thread(target=wc,args=(files,))
					c.start()
					c.join()
		elif parts[0]=='sort':
			files=parts[1]
			c=threading.Thread(target=sort,args=(files,))
			c.start()
			c.join()
		elif parts[0]=='head':
			files=parts[1]
			c=threading.Thread(target=head,args=(files,))
			c.start()
			c.join()
		elif parts[0] == 'mkdir':
			files = parts[1]
			c = threading.Thread(target=mkdir,args=(files,))
			c.start()
			c.join()
		elif parts[0]=='rmdir':
			files=parts[1]
			c=threading.Thread(target=rmdir,args=(files,))
			c.start()
			c.join()
		elif parts[0]=='exit()':
			print "Exiting shell"
			raise SystemExit    
		else:
			print("ERROR: Command not found")
