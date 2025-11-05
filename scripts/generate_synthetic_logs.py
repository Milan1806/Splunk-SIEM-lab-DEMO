#!/usr/bin/env python3
"""Generate synthetic auth logs (CSV) for demo purposes."""
import csv, random, datetime, uuid
first_names = ['Aarav','Ishaan','Saanvi','Ananya','Rohan','Priya','Arjun','Kavya','Vihaan','Sneha']
last_names = ['Sharma','Patel','Singh','Reddy','Iyer','Kumar','Khan']
hosts = ['web01','app02','db01','auth01','vm-ubuntu-1']
users = [f"{fn.lower()}.{ln.lower()}" for fn in first_names for ln in last_names]
start = datetime.datetime.now() - datetime.timedelta(days=7)

with open('../data/auth_logs.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=['event_id','timestamp','host','user','event_type','result','src_ip','details'])
    w.writeheader()
    for i in range(1500):
        ts = start + datetime.timedelta(seconds=random.randint(0,7*24*3600))
        host = random.choice(hosts)
        user = random.choice(users)
        if random.random() < 0.08:
            # cluster of failed logins (brute-like)
            result = random.choice(['failure']*3 + ['failure']*3 + ['success'])
            event_type = 'authentication'
            src_ip = f"192.168.{random.randint(1,254)}.{random.randint(1,254)}" if random.random() < 0.9 else f"203.0.113.{random.randint(1,254)}"
        else:
            result = random.choice(['success']*8 + ['failure'])
            event_type = 'authentication'
            src_ip = f"10.0.{random.randint(1,254)}.{random.randint(1,254)}"
        # occasional sudo events
        if random.random() < 0.02:
            event_type = 'sudo'
            result = 'success'
            details = 'command=apt update'
        else:
            details = ''
        w.writerow({'event_id': str(uuid.uuid4()), 'timestamp': ts.isoformat(), 'host': host, 'user': user, 'event_type': event_type, 'result': result, 'src_ip': src_ip, 'details': details})
print('Wrote ../data/auth_logs.csv')