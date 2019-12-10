from selenium import webdriver
import os
import time
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

csvfile = "30_name.csv"

def create_30data():
    count = 1
    with open(csvfile, "r") as f:
        rows = csv.reader(f)
        for row in rows:
            print("30銘柄読み込み中... ループ回数: " + str(count))
            row_str = str("".join(row))
            blog_url = "https://www.google.com/search?q=" + row_str + "+blog"
            driver = webdriver.Chrome()
            driver.get(blog_url)

            with open("dow30_blog_url.csv", "a") as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([row_str, blog_url])

            count = count + 1
            time.sleep(1)


print("--- START ---")
create_30data()
print("--- FINISH ---")
