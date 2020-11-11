'''
Maximum And Minimum 

Pesudo Code 
1. for in range of input form user 
2. using int convert into integer value
3. initilize n variable store the value of input 
4. initilize a variable getting list in integer
5. print the n-1*min vlaue of a 
end of step 1 loop 
'''
# taking input form user 
for _ in range(int(input())):
	# convert user input into integer value
	n = int(input())
	#creating list of user no 
	a = list(map(int, input()))
	# print the maximum value 
	print((n-1)*min(a))