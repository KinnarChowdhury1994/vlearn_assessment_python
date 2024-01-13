"""
Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.   
"""     
from utils import (checkPasswordUtility)     

def main():
    try:
        while (True):
            print("""
Password Criteria
○       The password should be at least 8 characters long.
○       Contains both uppercase and lowercase letters.
○       Contains at least one digit (0-9).
○       Contains at least one special character (e.g., !, @, #, $, %).

Note: Press Ctrl+C to Exit The Terminal
                  """)
            pwd_inp = str(input("Enter Your Password Here :-> "))
            cls_ins = checkPasswordUtility()
            resp,strength = cls_ins.checkPasswordStrength(password=pwd_inp)
            if resp:
                print(f'\nPassword strength is {strength}.')
                break
            elif not resp:
                print(f'\nPassword must {strength}.')
            else:
                break
    except KeyboardInterrupt:
        print('User Interrupted')
    except Exception as e:
        print(e)
    finally:
        print("Thank You")
        

if __name__ == "__main__":
    main()