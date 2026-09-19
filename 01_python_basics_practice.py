# Python Fundamentals & Security Practice
age = "19"
name = "Alhaji"
print ("My Name is", name)
print ("My Age is", age)

new_age = 19
next_year = new_age + 1
next_5_years = new_age + 5
next_10_years = new_age + 10 
print (next_year)
print (next_5_years)
print (next_10_years)

a = 47
b = 39
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b)
print (a % b)

user_age = int(input("Enter Your Age"))
user_name = input("Enter Your Name")
age = 19
if user_age >= age:
  print ("Access Granted")
else:
  print ("Access Denied")
number = int(input("Enter A Number"))
if number > 0:
  print ("Positive")
elif number < 0:
  print ("Negative")
else:
  print ("Zero")
  
new_number = int(input("Enter Number"))
if new_number > 50:
  print ("Number is Greater Than 50")
elif new_number < 50:
  print ("Number is Lesser Than 50")
else: 
  print ("Number is Equal To 50")
  
has_id = True
verified = True
minimum_age = 18
user_input = int(input("Enter Your Age"))
if user_input >= minimum_age and has_id and verified:
  print ("Successful")
else: 
  print ("Not Successful")
  
for number in range (1, 21):
  print (number)
for number in range (2, 21):
    vv = number % 2 == 0
    if vv:
        print (number)
  
for number in range (1, 31):
  if number % 2 == 0:
    print (f"{number} is even")
  else:
    print (f"{number} is odd")
    
count = 0
while count <= 9:
  count = count + 1
  print (count)
  
user = int(input("Enter A Unit"))
while user != 5:
  print ("Incorrect")
  user = int(input("Enter A Unit"))
print ("Correct")
  
failed_logins = [2, 6, 3, 8, 9, 7, 1, 4, 10, 3, 6]
for logs in failed_logins:
  if logs > 5:
    print (f"{logs} is suspicious")
  else:
    print (f"{logs} is normal")
    
normal = 0
suspicious = 0
total_attempts = 0
failed_attempts = [5, 10, 14, 5, 3, 7, 17, 3, 18, 9]
for attempts in failed_attempts:
    total_attempts = total_attempts + attempts
    if attempts > 5:
        suspicious = suspicious + 1
    else:
        normal = normal + 1
print(f"Suspicious: {suspicious}")
print(f"Normal: {normal}")
print(f"Total_Attempts: {total_attempts}")

failed_entry = [2, 4, 6, 8, 12, 9, 4, 3, 17]
good = 0
bad = 0
for entries in failed_entry:
  if entries > 5:
    bad = bad + 1
  else:
    good = good + 1
print (f"Good Users: {good}")
print (f"Bad Users: {bad}")