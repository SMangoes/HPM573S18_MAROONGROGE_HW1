# -*- coding: utf-8 -*-
"""
Sean Maroongroge
Modeling healthcare decisions
HW 1
"""

#Problem 1
#define all the variables and types
y1=17
y1=int (y1)

y2=17
y2=float (y2)

y3=17
y3=str (y3)

y4_var=17
y4=(y4_var==17)

#print the answer to part 1
print("y1:",type(y1), y1 , "y2:", type (y2), y2, "y3:", type (y3), y3, "y4:", type (y4), y4)

#print the answer to part 2
text="The value of x is " + str(y1) + "."
print(text)


#Problem 2
#define variables
str1="I"
str2="love"
str3="learning"
str4="to"
str5="code"
str6="!"

#concatenate
text=str1+" "+str2+" "+str3+" "+str4+" "+str5+str6

#print answer
print(text)

#Problem 3
#iterative solution

counter=int(0)
sum_total=0
n=input("Pick a positive integer n:")

for counter in range(0,int(n)+1):
	sum_total +=counter
print("The sum of all numbers from 1 to " + str(n) + " is " + str(sum_total) + ".") 


#recursive solution
n=input("Pick a positive integer n:")
def sum_function (n):
	if int(n)==1:
		return 1
	else:
		return int(n)+sum_function(int(n)-1)
print("The sum of all numbers from 1 to " + str(n) + " is "+ str(sum_function(n)) + ".") 

#Problem 4
yours=["Yale", "MIT", "Berkeley"]
mine=["School A", "School B", "School C"]
ours1=mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)

# part 1: ours1 is one long combined list, while ours2 is the two lists next to each other

yours[2] = "School D"
print(ours1)
print(ours2)

# part 2: ours1 and ours 2 differ because ours1 is a list that was assigned the value stored in lists “mine” and “yours”, 
# but ours2 references the lists stored in memory that ours1 and ours2 point to. 
# Therefore any mutations to the original lists will also appear in ours2 (because it still points to that referenced memory block) 
# and it will not appear in ours1 (because the values are still saved)

#Problem 5

problem_5_dict={}
month_name={1:"January",2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July" ,8:"August", 9:"September", 10:"October", 11:"November", 12:"December"} 
month_number={"January":1,"February":2, "March":3, "April":4, "May":5, "June":6, "July":7 ,"August":8, "September":9, "October":10, "November":11, "December":12}

print ("The sixth month is "+month_name[6]+".")
print("February is month " + str(month_number["February"])+".")