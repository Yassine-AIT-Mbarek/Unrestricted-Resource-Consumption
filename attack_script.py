import requests
import time
import threading

url = "http://192.168.110.131/virus.iso"
#url = "http://192.168.110.131/test_file.txt"

# Set the number of requests to send
num_requests = 1000

# Define a function to download the file
def download_file():
    response = requests.get(url)

    if response.status_code!= 200:
        print(f"Failed to download file: {response.status_code}")
    else:
        print(f"Downloaded file: {len(response.content)} bytes")

# Create and threads
threads = []
for i in range(num_requests):
    thread = threading.Thread(target=download_file)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()