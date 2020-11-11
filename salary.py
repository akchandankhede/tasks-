'''
Gross Salary 

Pesudo Code 
1. for user input in range 
2. sal= user input 
3. if sal<1500
	then print sal+((10*sal)/100)+((90*sal)/100)
4. else 
	print sal+500+((sal*98)/100)
end of step 3 if 
end of step 1 for 
'''

#getting integer input form user as no test cases 
for _ in range(int(input())):
	#salary as an input stored in s variable 
	sal=int(input())
	# sal is less than 1500
	if sal<1500:
		# print gross salary 
		print(sal+((10*sal)/100)+((90*sal)/100))
	else:
		# if salary is greater than 1500 then print the following gross salary 
		print(sal+500+((sal*98)/100))