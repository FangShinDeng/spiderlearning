# 爬蟲學習之旅
## 安裝內容
    1. 用pip安裝 requests: pip install requests
    官方文獻: https://pypi.org/project/requests/
    2. 用pip安裝 beautiful soup: pip install beautifulsoup4 
    官方文獻: https://pypi.org/project/beautifulsoup4/
    
## request pylint 錯誤提示修正
    只要在vscode的setting.json裡面加上，"python.linting.pylintArgs" : ["--generate-members"]就可以不報錯誤了！
    參考連結: https://www.jianshu.com/p/ab72e830b2a9

## pip無法使用時
    如果是安裝python3以上的，都會有內建pip套件了，可以使用指令pip list來查看目前安裝的所有套件，若無法使用或是報錯，可能是環境變數部分，沒找到pip的執行檔案路徑，可以到系統>進階系統設定>環境變數, 添加pip執行檔的路徑C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\Scripts