 #nested Loops problems 
#Problem1  find all prime number less than the entered number 
num=int(input("Enter a number: "))
if num>2:
    print(2,end=" ")
for i in range(3,num):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
        else:
            flag=True
    if flag:
        print(i,end=" ")


#Problem2  find  the total profit/loss of each trader working in a trading firm .information regarding number of trader and number of transactions is unknown . 
empID=input("Enter the employee ID: ")
while empID!="":
    trade=int(input("Enter the trade amount: "))
    profit_loss=0
    while trade!=0:
        trade=int(input("Enter the trade amount: "))
        profit_loss=profit_loss+trade
    print("The total profit/loss of the employee is: ",profit_loss)
    empID=input("Enter the employee ID: ")


# find the day wise total rainfall for the entered duration of time eg.  week month etc
days=int(input("Enter the number of days: "))
for i in range(1,days+1):
    rainfall=int(input("Enter the rainfall for day "+str(i)+": "))
    total=0
    while rainfall!=-1:
        total=total+rainfall
        rainfall=int(input("Enter the rainfall for day "+str(i)+": "))

    print("The total rainfall for day "+str(i)+" is: ",total)


    #find the lenght of longest word from the set of words entered by the user 
    word=int(input("Enter the number of words: "))
    maxlen=0
    while word!=-1:
        count=0
        for letter in word:
            count=count+1
        if count>maxlen:
            maxlen=count
        word=int(input("Enter the number of words: "))
    print("The length of longest word is: ",maxlen)