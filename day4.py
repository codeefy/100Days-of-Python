#find the digit of a number using while loop 

num=abs(int(input()))
digit=1 # it cover all the digit from -9 to 9 it means we have already count single digit number now we have to count number >9
while(num>9):
    num=num//10 #  it gives only integer part and  it devied the number greater than 10 untill the number comes less than 9 
    digit=digit+1
print(digit)
#num=1234
#more than 9
#it divide 1234//10 =123
#digit becomes  2
#still 123 >9 further devies 12
#digit becomes 3 
# still 12 >9 then again devied and gives intergral part 1 
# and the digit becomes 4 finally 
# now the while loop end ! 