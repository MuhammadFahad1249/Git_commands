print("choose the number: \n 1. 0 \n 2. 4")

x = int(input("Enter the number : "))
match x:
    case 0 :
        print("the number is Zero")
    
    case 4:
        print("the number is 4")

    case _ if x!=0 and x!=4:
        print(x ,"is not lying under the folowing condition")
     
    case _:     # default case , same as else statment
        print( x ,"number is invalid")