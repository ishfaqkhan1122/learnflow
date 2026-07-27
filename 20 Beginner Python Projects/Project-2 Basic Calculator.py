#Basic Calculator
while True:
 def add(a,b):
    answer=a+b
    print(str(a)+"+"+str(b)+"="+str(answer))
    print("="*35)
    

 def sub(a,b):
    answer=a-b
    print(str(a)+"-"+str(b)+"="+str(answer))
    print("="*35)
    

 def mul(a,b):
    answer=a*b
    print(str(a)+"*"+str(b)+"="+str(answer))
    print("="*35)
    

 def div(a,b):
    answer=a/b
    print(str(a)+"/"+str(b)+"="+str(answer))
    print("="*35)

 
 print("---------<<OPERATIONS>>-------")
 print("1. Addition")
 print("2. Sub")
 print("3. Mult")
 print("4. Div")
 print("5. Exit")

 choice=int(input("Enter Your choice in numbers:").strip())
 print("="*35)
 

 match choice:
  case 1:
     print("-----<<Your choice is Addition>>---")
     a=int(input("Enter First number:"))
     b=int(input("Enter Second number:"))
     add(a,b)
  case 2:
     print("-----<<Your choice is Substraction>>---")
     a=int(input("Enter First number:"))
     b=int(input("Enter Second number:"))
     sub(a,b)
  case 3:
     print("-----<<Your choice is Multiplication>>---")
     a=int(input("Enter First number:"))
     b=int(input("Enter Second number:"))
     mul(a,b)
  case 4:
     print("-----<<Your choice is Division>>---")
     a=int(input("Enter First number:"))
     b=int(input("Enter Second number:"))
     div(a,b)
  case 5:
     print("Program Ended!")
     print("="*35)
     break
 
     
      


