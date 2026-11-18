blocked_ips = ["192.168.1.10", "192.168.1.15", "192.168.1.20"]
blocked_ips.append("192.168.1.25")
print(blocked_ips)
print(len(blocked_ips))


blocked_users = ["admin", "guest", "root", "hacker", "tester"]
blocked_users.remove("hacker")
blocked_users.remove("guest")
print(blocked_users)
print(len(blocked_users))


failed_logins = ["user1", "user2", "user3", "user4", "user5"]
removed_user = failed_logins.pop(2)
print(removed_user)
print(failed_logins)

failed_logins.pop()
print(failed_logins)


suspicious_users = ["admin", "guest", "root", "tester"]
suspicious_users.insert(1, "hacker")
suspicious_users.insert(3, "unknown")
print(suspicious_users)
print(len(suspicious_users))


failed_attempts = [9, 3, 7, 1, 5, 8, 14, 67]
failed_attempts.sort()
print(failed_attempts)

failed_attempts.sort(reverse=True)
print(failed_attempts)


login_attempts = [5, 2, 8, 1, 9, 3]
login_attempts.reverse()
print(login_attempts)


suspicious_ips = [
    "192.168.1.10",
    "10.0.0.8",
    "172.16.0.5"
]

if "192.168.1.10" in suspicious_ips:
    print("IP found")
else:
    print("IP not found")


new_ip = "192.168.1.10"

if new_ip not in suspicious_ips:
    suspicious_ips.append(new_ip)
else:
    print("IP already exists")

print(suspicious_ips)


print(suspicious_ips[0])
print(suspicious_ips[-1])
print(len(suspicious_ips))