
import requests
import time
from bs4 import BeautifulSoup

base_url = "https://techacademy.jp/magazine/"
page_no = 23500
counter = 1
error_page = 0
ok_page = 0
noTagURL_page = 0 # https://techacademy.jp/magazine/23289/programmer-and-coder-working-in-the-development-environment-programmers-workplace-2
noTag_page = 0  # https://techacademy.jp/magazine/222

while counter < page_no:
    print("検索回数:  " + str(counter))
    search_url = base_url + str(counter)
    print("確認するURL:  " + search_url)
    try:
        page_response = requests.get(search_url)
        post_src = page_response.content
        soup = BeautifulSoup(post_src, "lxml")
        page_tag = soup.findAll("div", {"class": "post-category"})
        try:
            tag_link = page_tag[0].select("a")
            tag_link_url = tag_link[0]["href"]
            if tag_link_url == "":
                print("タグ情報ないね")
                noTagURL_page = noTagURL_page + 1
                counter = counter + 1
                time.sleep(0.1)
            else:
                print("タグ情報あるね")
                ok_page =ok_page + 1
                counter = counter + 1
                time.sleep(0.1)
        except:
            print("page_tag がないね")
            noTag_page = noTag_page + 1
            counter = counter + 1
            time.sleep(0.1)

    except:
        print("tryのアクセスエラー発生")
        error_page = error_page + 1
        counter = counter + 1
        time.sleep(0.1)

print("ブログ数: " + str(ok_page))
print("タグのURLないページ数: " + str(noTagURL_page))
print("タグがないページ数: " + str(noTag_page))
print("エラー回数: " + str(error_page))
