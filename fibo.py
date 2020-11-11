'''
Fibonacci Series


#pesudo code
1. Initilized the counter package
2. Taking input form user stored in variable t
3. for t in range 
4. input Initilized variable s
5. sort the given list in asscending oreder
6. Initilized res variable to show result
7. if hthe lenght of d is greater than equal to 4 and d[3] is not qeual to 
    d[2]+d[1] then compare d[1],d[0] is equal to d[0],d[1]
End of step 7 if 
8. for i in rage of 2, lenght of d.
9. if d[i] is not equal to d[i-1]+d[i-2] then res= not 
end of step 9 if
end of step 8 for loop
print res 
end of step 3 for loop 


'''
#initilizing the counter package 

from collections import Counter
#getting input from user and store into t variable how many test cases 
t=int(input())
for _ in range(t):
    #taking the the test cases form the user 
    s=input()
    #sorting the list from the counter into asscending oreder 
    d=sorted(list(Counter(s).values()))
    res="Dynamic"
    if len(d)>=4 and d[3]!=d[2]+d[1]:
        #comparimg the array of 0th and 1st element 
        d[1],d[0]=d[0],d[1]
        #using for loop to satisfy the condition 
    for i in range(2,len(d)):
        #checking if the element is not eqaual to 
        if d[i]!=d[i-1]+d[i-2]:
            #then print the result as a "not"
            res="Not"
            break
            #print the result is it "Dynamic" or "not"
    print(res)

