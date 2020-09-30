import requests
import lxml
from bs4 import BeautifulSoup

def shopeecrawler(keyword):
    # url = "https://shopee.tw/search?keyword=ps4%20pro%20%E4%B8%BB%E6%A9%9F"
    url = f"https://shopee.tw/search?keyword={keyword}"
    headers = {
    "User-Agent":"Googlebot",
    }
    res = requests.get(url, headers = headers, allow_redirects = True)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.find_all("div", class_="col-xs-2-4 shopee-search-item-result__item")
    titles = soup.find_all("div", class_="_1NoI8_ _16BAGk")
    prices = soup.find_all("span", class_="_341bF0")
    sales_nums = soup.find_all("div", class_="_18SLBt")
    
    # 儲存檔案
    f = open("index.html","w+", encoding= "UTF-8")
    
    for title, price, sales_num in zip(titles, prices, sales_nums):
        print(title)
        print(price)
        print(sales_num)
        f.write(format(title))
        pass
    
    f.close()
    
    pass
    

shopeecrawler('精油')
