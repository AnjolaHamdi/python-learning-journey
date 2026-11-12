traffic_logs = [
    " HTTP, 192.168.1.10, 450, ALLOWED ",
    " SSH, 192.168.1.11, 120, BLOCKED ",
    " FTP, 192.168.1.12, 800, BLOCKED ",
    " HTTP, 192.168.1.13, 300, ALLOWED ",
    " SSH, 192.168.1.14, 950, BLOCKED "
]

def analyse_traffic(raw_data):
    result = raw_data.strip().split(",")
    return result
cleaned_traffic_logs = []
allowed_count = 0
blocked_count = 0
high_traffic_count = 0
for log in traffic_logs:
    result = analyse_traffic(log)
    formatted_traffic_logs = []
    for items in result:
        formatted = items.strip()
        formatted_traffic_logs.append(formatted)

    cleaned_traffic_logs.append(formatted_traffic_logs)

    if "ALLOWED" in formatted_traffic_logs:
        allowed_count += 1
    elif "BLOCKED" in formatted_traffic_logs:
        blocked_count += 1

    if int(formatted_traffic_logs[2]) > 500:
        high_traffic_count += 1

print("ALL CLEANED TRAFFIC RECORD:", cleaned_traffic_logs)
print("ALLOWED CONNECTIONS:", allowed_count)
print("BLOCKED CONNECTIONS:", blocked_count)
print("HIGH TRAFFIC CONNECTIONS:", high_traffic_count)