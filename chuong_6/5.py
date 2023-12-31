import requests
import threading

def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"Đã tải xong {url}")
    except requests.exceptions.RequestException as e:
        print(e)

urls = [r"https://www.youtube.com/@zachstar", r"https://blog.medium.com/32-of-our-favorite-medium-stories-of-2023-1fb10ca34cd8", r"https://vnexpress.net/khoa-hoc/ai4vn-2023"]

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()