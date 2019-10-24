#	Lab Test 1
#	Date: 24 October 2019
# 	Time Start: 14:10
#	DeadLine: 16:20

#	Program Code: DT211c/2
#	Name: Yutaphong Gitchamnan
#	Student Number: c18437284


#	Task: make pascal's triangle with user input height. 
#		Part 1a: have a function call make_new_row that uses old row to 
#					make new pascal line.
#		Part 1b: handle special cases
#		Part 2: prompt user for height for the triangle
#		Part 3: display whole list of without triangle and with triangle
#		Part 4: center the triangle using ''.join([str(i) for i in List])

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
import string

#pascal rows limites up to 12 lines
def make_new_row(old_row):
	#line 1
	if old_row is []:
		return [1]
	#line 2	
	elif old_row is [1]:
		return [1,1]
	#line 3
	elif old_row is [1,1]:
		return [1,2,1]
	#line 4
	elif old_row is [1,2,1]:
		return [1,3,3,1]
	#line 5	
	elif old_row is [1,3,3,1]:
		return [1,4,6,4,1]
	#line 6
	elif old_row is [1,4,6,4,1]:
		return [1,5,10,10,5,1]
	#line 7	
	elif old_row is [1,5,10,10,5,1]:
		return [1,6,15,20,15,6,1]
	#line 8
	elif old_row is [1,6,15,20,15,6,1]:
		return [1,7,21,35,35,21,7,1]
	#line 9
	elif old_row is [1,7,21,35,35,21,7,1]:
		return [1,8,28,56,70,56,28,8,1]
	#line 10
	elif old_row is [1,8,28,56,70,56,28,8,1]:
		return [1,9,36,84,126,126,84,36,9,1]
	#line 11
	elif old_row is [1,9,36,84,126,126,84,36,9,1]:
		return [1,10,45,120,210,252,210,120,10,1]
	#ine 12
	elif old_row is [1,10,45,120,210,252,210,120,10,1]:
		return [1,11,55,165,330,462,462,330,165,55,11,1]
	#line 13
	elif old_row is [1,11,55,165,330,462,462,330,165,55,11,1]:
		return [1,12,66,220,495,792,922,792,495,220,12,1]
	#line 14
	else old_row is [1,12,66,220,495,792,922,792,495,220,12,1]
		return [1,13,78,286,715,1714,1714,286,78,13,1]

def main()
	
	print("1: display as one single line\n")
	print("1: display as triangle\n")
	n = input("Choose display type: \n")
	#ask user for input height
	n_int = input("Enter height of pascal's triangle: \r\n")
	
	#just single line
	case '1':
		#set limits on height
		if n_int < 14:
			#loop
			for i is < n_int:
				#display the line
				print(make_new_row)	
				#get the line
				old_row = make_new_row
		#when it over limits
		else
			#display
			print("Number is too Large.\n\n")
			
		break
	
	#triangle not center
	case '2':
		#set limits on height
		if n_int < 14:
			#loop
			for i is < n_int:
				#display the line
				print(make_new_row "\n")	
				#get the line
				old_row = make_new_row
		#when it over limits
		else
			#display
			print("Number is too Large.\n\n")
			
		break
	
	#display in center
	case '3':
		#set limits on height
		if n_int < 14:
			#loop
			for i is < n_int:
				#display the line
				' '.join([str(i)for i in List])
				print(make_new_row)	
				#get the line
				old_row = make_new_row
		#when it over limits
		else
			#display
			print("Number is too Large.\n\n")
			
		break
return 0: