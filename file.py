import requests


def file_read_and_save(url,path):
    r=requests.get(url)
    with open(path, "a+", encoding="utf-8") as f:
        print('read from existing')
        f.write(r.text)  # If the file exists, it will be opened for appending
    
url='https://timesofindia.indiatimes.com/'
store_path="data/times.html"
file_read_and_save(url,store_path)