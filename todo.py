#! /usr/bin/env python3

import sys
import datetime

#print(sys.argv)
try:
	if sys.argv[1] == "add":

		try:
			try:
				if (sys.argv[3]) and (sys.argv[1] == "add"):
					for i in range(2,len(sys.argv)):
						with open("todo.txt", "a") as myfile:
							myfile.write(str(sys.argv[i])+'\n')
						print(f"Added todo: \"{sys.argv[i]}\"")
				
			except:
				if sys.argv[1] == "add":
					try:
						with open("todo.txt", "a") as myfile:
							myfile.write(str(sys.argv[2])+'\n')
						print(f"Added todo: \"{sys.argv[2]}\"")
	
					except:
						print("Error: Missing todo string. Nothing added!")

			
		except:
			pass



	if sys.argv[1] == "help":
		a='Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'
		print(a)



	if sys.argv[1] == "ls":
		try:
			with open('todo.txt') as t:
				count = sum(1 for _ in t)
				#print(count)
			
			if count == 0:
				print("There are no pending todos!")
			else:
				myfile = open("todo.txt")
				lines = myfile.readlines()
				for pos,i in enumerate(reversed(lines)):
					print("["+str(count-pos)+"]",i, end="")
				myfile.close()
		except:
			print("There are no pending todos!")

	if sys.argv[1] == "del":
		try:
			with open("todo.txt", "r") as myfile:
				lines = myfile.readlines()

			with open("todo.txt" , "w") as f:
				for pos, line in enumerate(lines):
					if pos!=(int(sys.argv[2])-1):
						#print(type(pos), type(sys.argv[2]))
						#print(pos, sys.argv[2])
						f.write(line)
					else:
						print(f"Deleted todo #{pos+1}")
				#print(pos)
				if (int(sys.argv[2]) > pos+1) or (int(sys.argv[2])<1) :
					print(f"Error: todo #{sys.argv[2]} does not exist. Nothing deleted.")
		except:
			print("Error: Missing NUMBER for deleting todo.")


	if sys.argv[1] == "done":
		try:
			with open("todo.txt", "r") as myfile:
				lines = myfile.readlines()

			with open("todo.txt" , "w") as f:
				for pos, line in enumerate(lines):
					if pos!=(int(sys.argv[2])-1):
						#print(type(pos), type(sys.argv[2]))
						#print(pos, sys.argv[2])
						f.write(line)
					else:
						print(f"Marked todo #{pos+1} as done.")
						timenow = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
						with open("done.txt" , "a") as d:
							my_str = 'x  ' +f"{timenow}  "+line
							d.write(my_str)
						
				if (int(sys.argv[2]) > pos+1) or (int(sys.argv[2])<1) :
					print(f"Error: todo #{sys.argv[2]} does not exist.")
		except:
			print("Error: Missing NUMBER for marking todo as done.")

	if sys.argv[1] == "report":
		try: 
			with open('todo.txt') as rem:
				count1 = sum(1 for _ in rem)
		except:
			count1 = 0
		try:
			with open('done.txt') as com:
				count2 = sum(1 for _ in com)
		except:
			count2 =0
		timestat = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
		print(f"{timestat} Pending : {count1} Completed : {count2}")


except:
	a='Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'
	print(a)

