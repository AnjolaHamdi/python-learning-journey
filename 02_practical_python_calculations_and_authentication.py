price = int(input("Price Of Goods"))
quantity = int(input("How Many Are You Buying"))
cost = price * quantity
if cost >= 10000:
  print ("You Have Gotten A 10% Discount")
  discount = price * 0.10
  cost = cost - discount
  print (f"Final Cost: {cost}")
else: 
  print (cost)
  
pin = 1234
attempts = 0
maximum_attempts = 3
transaction_approved = False

while attempts < maximum_attempts:
    enter_pin = int(input("Enter Your Pin"))

    if enter_pin == pin:
        print("Approved")
        transaction_approved = True
        break

    else:
        attempts = attempts + 1
        attempts_left = maximum_attempts - attempts

        if attempts_left == 1:
            print("⚠️ Final attempt! Enter the correct PIN or your account will be locked.")
        else:
            print(f"{attempts_left} Attempts Left")

if not transaction_approved:
    print("Account Locked")