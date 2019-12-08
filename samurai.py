import requests
import time
from bs4 import BeautifulSoup

base_url = "https://www.sejuku.net/blog/"
page_no = 113920
counter = 1
error_page = 0
ok_page = 0

while counter < page_no:
    print("検索回数:  " + str(counter))
    search_url = base_url + str(counter)
    print("確認するURL:  " + search_url)
    try:
        page_response = requests.get(search_url)
        post_src = page_response.content
        soup = BeautifulSoup(post_src, "lxml")
        page_info = soup.title.string
        if page_info == "Nothing found for  Blog " + str(counter):
            print("404 error:  " + page_info)
            error_page = error_page + 1
            counter = counter + 1
            time.sleep(0.1)
        else:
            print("ok")
            ok_page = ok_page + 1
            counter = counter + 1
            time.sleep(0.1)
    except:
        print("tryのアクセスエラー発生")
        counter = counter + 1
        time.sleep(0.1)
    
print("ブログ数: " + str(ok_page))