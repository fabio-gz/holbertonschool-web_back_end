#!/usr/bin/env python3
"""Log Stats """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx
    logs = collection.count_documents({})
    print(f"{logs} logs")

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for i in method:
        count = collection.count_documents({"method": i})
        print(f"\tmethod {i}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
