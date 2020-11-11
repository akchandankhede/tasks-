'''
Two Number 

Pesudo Code 
1. initilize the variable n 
2. for i in rage of n 
3. initilize variable a,b,t
4. getting ittrable integer value from user 
5. if t % 2 is not equal to 0 
	then 
	print max(a*2,b) compare with min(a * 2,b) print the answer 
6. else 
	print max(a,b) compare min(a,b) print the answer 
end of step 5 if 
end of sttep 2 for loop. 
'''



# take an input value in n 
n = int(input())
# i variable to initilized counter upto n 
for i in range(n) :
	#taking 3 input from user 
    a,b,t = map(int,input())
    # if satisfy the condition t%2!=0
    if t % 2 != 0 :
    	# comparing min and max and print the answer 
        print((max(a * 2,b)) // min(a * 2,b))
    else :
        print(max(a,b) // min(a,b))