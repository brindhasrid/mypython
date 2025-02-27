def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("Please Seect the Option -\n" \
      "1.Add\n"\
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Divide\n" )
Select=int(input("Select operation from i,2,3,4"))
number_1=int(input("Enter the first mumber:"))
number_2=int(input("Enter Second Number:"))

if Select==1:
    print(number_1,"+",number_2 ,"=", add(number_1,number_2))

elif Select==2:
    print(number_1,"-",number_2 ,"=", subtract(number_1,number_2))

elif Select==3:
    print(number_1,"*",number_2, "=", multiply(number_1,number_2))  
elif Select==4:
    print(number_1,"/",number_2, "=",divide(number_1,number_2))