import math 
def advanced_calculator():
    print("***Avanced calculator***")
    
    print("operator") 
    
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    print("5. power")
    print("6. modular")
    print("7. square")
    print("8. sin")
    print("9. cos")
    print("10.tan")
    print("11.logarithmic functions")
    
    choice = input("Enter your choice between 1 to 11:  ")
    
    if choice in ['1','2','3','4','5','6']:
        
        num1 = float(input("Enter num1:"))
        num2 = float(input("Enter num2:"))
        
        if choice == '1':
            print(f"result of {num1 + num2}")
                
        elif choice == '2':
            print(f"result of {num1 - num2}")
            
        elif choice == '3':
            print(f"result of {num1 * num2}")
            
        elif choice == '4':
            if num2 == 0:
                print("zero division error")
            else:    
                print(f"result of {num1 / num2}")
                
        elif choice == '5':
            print(f"result of {num1 ** num2}")
         
        elif choice == '6':
            print(f"result of {num1 % num2}")
            
    elif choice == '7':
        num = float(input("Enter num"))
        
        if num>=0:
            print(f"square is {math.sqrt(num)}")
        else:
            print("square impossible") 
                  
    elif choice in ['8','9','10']:
        
        angle = float(input("Enter angle:"))
        
        radians = math.radians(angle)    
         
        if choice == '8':
            print(f"result: {math.sin(radians)}")
            
        elif choice == '9':
            print(f"result: {math.cos(radians)}")
            
        elif choice == '10':
            print(f"result: {math.tan(radians)}")
            
    elif choice == '11':
        num = float(input("Enter a num:"))
        if num>0:
            print(f"result: {math.log10(num)}") 
        else:
            print("Error: logarithmic undefined non positive num") 
             
    else: 
        print("Invalid input")        
        
advanced_calculator()