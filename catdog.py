'''
Cat and dog problem 


Pesudo Code 
1. initilize t variable for user input 
2. while t is greater than 0
3.intilize variable c,d,l 
4.map the value covert into int dat
5. initilize a is equal to c-2*d
6. initilize b is equal to a+d*4
7. if l%4 is not equal to 0 or l greater than c+d*4 or l less than 4*d or l less than b
	then 
	print no 
8 else print yes
end of step 7 if 
9. decrease the value of t by 1 
end of step2 while loop 
'''



# No of ittretion i.e how many test cases 
t=int(input())
# t must be greater than 0 
while t>0:
	# getting input no of cat , and no of dog and no of legs using map getting ittrable values of god cat and legs 
    c,d,l=map(int,input())
    a=(c-2*d)
    b=(a+d)*4
    #if the mod 4 legs is equal to 0 
    if((l%4)!=0 or l>((c+d)*4) or l<4*d or l<b):
    	# print no 
        print("no")
    else:
    	#elese print yes 
        print("yes")
        # decrease the t by 1 
    t-=1