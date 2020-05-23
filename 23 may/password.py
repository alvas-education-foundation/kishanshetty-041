attempts = 3 
while attempts !=0: #Check until attempts become equal to zero.
      user_name = input("Enter the user name:")
      user_password = input("Enter the user password:")
      
      if user_name == 'Micheal' and user_password == 'e3$WT89x': 
            print("You have successfully logged in!")
            flag = 1
            break
      else:
           attempts-=1 #Decrease number of attempts by 1. 
           if attempts !=0:
                  print("Invalid user name or password. Try again...")
           else:
                  print("You have exceeded the number of attempts.")
                  print("Account Locked!")
