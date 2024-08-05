import threading
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

# List of URLs to download
urls = [
    ("https://example.com/file1.zip", "file1.zip"),
    ("https://example.com/file2.zip", "file2.zip"),
    ("https://example.com/file3.zip", "file3.zip"),
]

# Create and start a thread for each file download
threads = []
for url, filename in urls:
    thread = threading.Thread(target=download_file, args=(url, filename))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All downloads completed!")
