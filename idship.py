'''
ID and BattleShip

Pesudo Code 
1. Initilized for in range of no of test cases form user 
2. initilized s variable to take a character 
3. convert character into lower case 
4. if s==b
    then print BattleShip
5. else if s==c
    then print Cruiser
6. else if s==d
    then print Destroyer
7. else if s==f 
    then print Frigate
end of step 4 elif
'''
# enter no of test cases 
for i in range(int(input())):
    # enter character stores in s variable 
    s=input()
    # convert character into lower case 
    s=s.lower()
    # checking the character taken form user and print the result 
    if(s=='b'):
        print("BattleShip")
    elif(s=='c'):
        print("Cruiser")
    elif(s=='d'):
        print("Destroyer")
    elif(s=='f'):
        print("Frigate")