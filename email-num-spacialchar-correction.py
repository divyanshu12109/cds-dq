pip install email_validator


# Python program to check if 
# given mobile number is valid
import re

def is_num(s):

    
    # 1) Then contains 6,7 or 8 or 9.
    # 2) Then contains 9 digits
    Pattern = re.compile("[6-9][0-9]{9}")
    


    if re.match(Pattern, s): 
        print (s)
    else :
        print ('0000000000') 


# This code is contributed by divyanshu_gadhwal



from email_validator import validate_email, EmailNotValidError

def is_email(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v["email"]
        print(email)
    except EmailNotValidError as e:
        # email is not valid, exception message is INCORRECT
        print("INCORRECT")
        
        
        
        
        
# Python3 code to demonstrate
# removal of special_chars
import string
def remove_spacial_char(test):
    specil_chars = []
    t1 = string.punctuation

    specil_chars = []
    for i in t1:
        specil_chars.append(i)

    s=""
    for i in test:
        if i not in specil_chars:
            s+=i

    print (str(s))


