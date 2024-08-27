#!/usr/bin/env python3
""" 12log stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_c = client.logs.nginx

    print(f'{nginx_c.count_documents({})} logs')
    print('Methods:')
    for x in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f'\tmethod {x}: {nginx_c.count_documents({"method": x})}')
    print(nginx_c.count_documents({"method": "GET", "path": "/status"}),
          "status check")
    print('IPs:')
    sorted_ips = nginx_c.aggregate(
        [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
         {"$sort": {"count": -1}}])
    i = 0
    for s in sorted_ips:
        if i == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        i += 1
