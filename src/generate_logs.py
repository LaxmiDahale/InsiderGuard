import pandas as pd
import random
from datetime import datetime, timedelta

users = [
    "user01",
    "user02",
    "user03",
    "user04",
    "user05"
]

records = []

for i in range(1000):

    user = random.choice(users)

    login_hour = random.randint(8, 18)

    failed_logins = random.randint(0, 2)

    files_accessed = random.randint(5, 30)

    download_mb = random.randint(0, 100)

    new_ip = random.choice([0, 0, 0, 1])

    records.append({
        "timestamp": (
            datetime.now()
            - timedelta(minutes=i)
        ),
        "username": user,
        "login_hour": login_hour,
        "failed_logins": failed_logins,
        "files_accessed": files_accessed,
        "download_mb": download_mb,
        "new_ip": new_ip
    })


# Add suspicious activity

records.append({
    "timestamp": datetime.now(),
    "username": "user03",
    "login_hour": 2,
    "failed_logins": 12,
    "files_accessed": 700,
    "download_mb": 5000,
    "new_ip": 1
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_normal",
    "login_hour": 10,
    "failed_logins": 0,
    "files_accessed": 15,
    "download_mb": 20,
    "new_ip": 0
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_night_login",
    "login_hour": 2,
    "failed_logins": 0,
    "files_accessed": 15,
    "download_mb": 20,
    "new_ip": 0
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_failed_logins",
    "login_hour": 10,
    "failed_logins": 10,
    "files_accessed": 15,
    "download_mb": 20,
    "new_ip": 0
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_file_access",
    "login_hour": 11,
    "failed_logins": 0,
    "files_accessed": 500,
    "download_mb": 20,
    "new_ip": 0
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_large_download",
    "login_hour": 11,
    "failed_logins": 0,
    "files_accessed": 20,
    "download_mb": 5000,
    "new_ip": 0
})
records.append({
    "timestamp": datetime.now(),
    "username": "test_critical",
    "login_hour": 2,
    "failed_logins": 12,
    "files_accessed": 700,
    "download_mb": 5000,
    "new_ip": 1
})

df = pd.DataFrame(records)

df.to_csv(
    "data/user_activity.csv",
    index=False
)

print("Security logs generated successfully.")