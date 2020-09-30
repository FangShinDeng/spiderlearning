# 爬蟲學習之旅
## 安裝內容
    1. 安裝 requests: pip install requests
    官方文獻: https://pypi.org/project/requests/
    2. 安裝 beautiful soup: pip install beautifulsoup4 
    官方文獻: https://pypi.org/project/beautifulsoup4/
    3. 安裝 pandas: pip install pandas
    官方文獻: https://pypi.org/project/pandas/
    4. 安裝 lxml: pip install lxml
    官方文獻: https://pypi.org/project/lxml/
    5. 安裝 html5lib: pip install html5lib
    官方文獻: https://pypi.org/project/html5lib/
    6. 安裝 pandasgui: pip install pandasgui
    官方文獻: https://pypi.org/project/pandasgui/
    7. 安裝 wheel: pip install wheel
    官方文獻: https://pypi.org/project/wheel/

## request pylint 錯誤提示修正
    只要在vscode的setting.json裡面加上，"python.linting.pylintArgs" : ["--generate-members"]就可以不報錯誤了！
    參考連結: https://www.jianshu.com/p/ab72e830b2a9

## pip無法使用時
    如果是安裝python3以上的，都會有內建pip套件了，可以使用指令pip list來查看目前安裝的所有套件，若無法使用或是報錯，可能是環境變數部分，沒找到pip的執行檔案路徑，可以到系統>進階系統設定>環境變數, 添加pip執行檔的路徑C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\Scripts

## Visual Studio IntelliCode 自動補齊安裝
    教學參考文獻: https://blog.csdn.net/weixin_40922744/article/details/103216982
    安裝連結: https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode

## Python unresolved import issue
    若有遇到黃色底線pandasgui警告的部分，請參考文檔在vscode/json檔案裡面將特定行註解
    參考文獻: https://www.mmbyte.com/article/6574.html

# 爬蟲實戰 - 蝦匹商品列表
    連上蝦匹，並依照關鍵字去爬出對應的商品列表，儲存在檔案裏面展示出來
    參考文獻: https://freelancerlife.info/zh/blog/python-web-scraping-user-agent-for-shopee/
    參考文獻: https://shopee.tw/robots.txt
    python 字符串前面加 f, 參考文獻: https://blog.csdn.net/LuohenYJ/article/details/106817999