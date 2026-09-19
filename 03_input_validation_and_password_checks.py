name  = input("Enter Your Name:")
if name.isalpha ():
  print ("Valid")
else:
  print ("Invalid")

age = input ("Enter Your Age")
if age.isdigit ():
  print ("Valid")
else:
  print ("Invalid")

age = input("Enter Your Age")
if age.isdigit () and int (age) >= 18:
  print ("Eligible")
else:
  print ("Not Eligible")

password = input ("Enter Password")
has_uppercase = False
for values in password:
  if values.isupper ():
    has_uppercase = True
if has_uppercase: 
  print ("Contains Uppercase")
else:
  print ("No Uppercase")

pin = input ("Enter Pin")
has_digit = False
for numbers in pin:
  if numbers.isdigit ():
    has_digit = True
    break
if has_digit:
  print ("Contains Digit")
else:
  print ("No Digits")

password = input ("Enter Password")
has_number = False
has_uppercase = False
has_lowercase = False
for characters in password:
  if characters.isupper ():
    has_uppercase = True
  if characters.islower ():
    has_lowercase = True
  if characters.isdigit ():
    has_number = True
if has_uppercase and has_lowercase and has_number:
  print ("Strong Password")
else:
  print ("Weak Password")

age = int(input("Enter Your Age"))
if age < 13:
  print ("Child")
elif age >= 13 and age <= 17:
  print ("Teenager")
elif age >= 18 and age <= 60:
  print ("Adult")
else:
  print ("Senior")

user_name = input ("Enter Username")
if user_name.lower () == "admin":
  password = input ("Enter Password")
  if password == "1234":
    print ("Login Successful")
  else:
    print ("Wrong Password")
else:
  print ("Unknown User")