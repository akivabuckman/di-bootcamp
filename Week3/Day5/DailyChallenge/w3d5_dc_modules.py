import requests
import time


def check_time(address):
    start_time = time.time()
    requests.get(url=f"http://{address}")
    end_time = time.time()
    return end_time - start_time


check_time(input("webpage: "))