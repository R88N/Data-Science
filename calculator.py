
# set of functions to calulate two numbers

def add(num1, num2):
	return num1 + num2

def minus(num1, num2): 
	return num1 - num2

def multiply(num1, num2):
      return num1 * num2

def divide(num1, num2):
      return num1 / num2
 
print("To use this calculator,")

# This is the main function where the calculations will be made

def calc():
      while True:
            try:
                  user_num1 = float(input("Please enter the first number: "))
                  print("\n")
                  break
            
            # if the user enters an invalid entry like a string an error appears
            except ValueError:
                        print("Please enter a valid number.")
                        print("\n")
            
      while True: 
            try:  
                  user_num2 = float(input("Please enter your second number: "))
                  print("\n")
                  break

            # the same thing happens here
            except ValueError:
                  print("\n")
                  print("Please enter only a valid number.")

      while True:
            user_op = input("Please enter one of these 4 operators; '+', '-', 'x' and '/': ")

            # Input error correction - getting rid of possible blank spaces
            user_op = user_op.strip(" ")

            print("\n")

            # if the user selects anything but the 4 options an error will appear
            
            try:  
                  if user_op != "+" and user_op != "-" and user_op != "x" and user_op != "/":
                        raise ValueError
                  break
                        
            except ValueError:
                  print("Make sure you only choose from the 4 options: '+', '-', 'x' and '/' ")
                  print("\n")

      # Here we go through all the 4 options which decides what calculation will be made
      # depending on the operation 
           
      if user_op == "+":
                                    
            with open('new.txt','w') as file:

                  result = str(add(user_num1,user_num2))

                  # we turn the numbers into strings so that we can print them in the text file
                  user_num1_str = str(user_num1)
                  user_num2_str = str(user_num2)

                  # here we print the text file
                  file.write(f"{user_num1_str} + {user_num2_str} = {result}")

                  # The user is notifed that the calculation is printed on the text file
                  print("Your calculation is printed on the text file: 'new.txt'")    

      # These steps are repeated here and with the remaining two operations
      
      elif user_op == "-":
            with open('new.txt','w') as file:
                                    
                  result = str(minus(user_num1,user_num2))

                  user_num1_str = str(user_num1)
                  user_num2_str = str(user_num2)

                  file.write(f"{user_num1_str} - {user_num2_str} = {result}")

                  print("Your calculation is printed on the text file: 'new.txt'") 

      elif user_op == "x":
            with open('new.txt','w') as file:
                                                            
                  result = str(multiply(user_num1,user_num2))

                  user_num1_str = str(user_num1)
                  user_num2_str = str(user_num2)

                  file.write(f"{user_num1_str} x {user_num2_str} = {result}")
                                                
                  print("Your calculation is printed on the text file: 'new.txt'") 

      elif user_op == "/":
            try:
                  with open('new.txt','w') as file:

                        result = str(divide(user_num1,user_num2))

                        user_num1_str = str(user_num1)
                        user_num2_str = str(user_num2)

                        file.write(f"{user_num1_str} / {user_num2_str} = {result}")

                        print("Your calculation is printed on the text file: 'new.txt'") 

            # An error is generated if the user attempts to divide by zero
            # they must then repeat the step and choose a different set of numbers                                    
            
            except ZeroDivisionError:
                  print("You cannot divide by zero, please choose a different set of numbers.")

      # Once the user has completed the calculation they will be asked if they want to do this again
      print("\n")

      repeat = input("Would you like to try again? 'yes' or 'no' ").lower()
      if repeat == "yes":
            repeat = repeat.strip(" ")
            print("\n")
            calc()

      else:
            print("Thank you for using this calculator.")

      print("\n")

      # The user is given the option to print their own calculations from their file
      
      user_equations = input("Would you like to print the calculations on your file? ").lower()
      
      while True:
            if user_equations == "yes":
                  try:
                        user_file = str(input("What is the name of your file? "))

                        with open(user_file, "r") as file:
                              file_contents = file.readlines()

                        # The file is printed in a list form so the for loop below will print the values of the list instead

                        for contents in file_contents:
                              print("\nThe calculations in your file are:")
                              print(contents.strip("\n"))

                        break

                  # If the user doesnt provide a valid file name, an error message appears
                  # The error message captures both non-existent files and files that can't be found
                  
                  except FileExistsError:
                        print("This file doesn't exist, please re-enter the file name")
                  except FileNotFoundError:
                        print("This file cannot be found, please re-enter the file name")

            else:
                  print("The end")
                  break
calc()

