#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_c = client.logs.nginx

print(f'{nginx_c.count_documents({})} logs')
print('Methods:')
for x in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print(f'\tmethod {x}: {nginx_c.count_documents({"method": x})}')
print(nginx_c.count_documents({"method": "GET", "path": "/status"}),
      "status check")
