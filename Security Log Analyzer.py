def is_suspicious(attempts):
    if attempts >= 5:
        return True
    else:
        return False
suspicious_accounts = []
suspicious_accounts_count = 0
total_failed_logs = sum(login_attempt.values())
most_attacked_account = 0
most_attacked_account_count = ""
for key, value in login_attempt.items():
  if value > most_attacked_account:
    most_attacked_account = value
    most_attacked_account_count = key
  if is_suspicious(value):
    suspicious_accounts_count = suspicious_accounts_count + 1
    suspicious_accounts.append(key)
print ("Total Failed Account:", suspicious_accounts_count)
print("Total Failed Logins:", total_failed_logs)
print("Most Attacked Account:", most_attacked_account)
print("Most Attacked Account Count:", most_attacked_account_count)