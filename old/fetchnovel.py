import requests
from bs4 import BeautifulSoup

# 設定基本網址
base_url = "https://ncode.syosetu.com/n3900hn/"

# 設定 User-Agent 標頭
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 開啟一個文件來寫入所有頁面的內容
with open("novel_content.html", "w", encoding="utf-8") as file:
    for i in range(1, 101):
        # 生成完整的網址
        url = f"{base_url}{i}/"
        print(f"正在獲取: {url}")
        
        # 獲取網頁內容
        response = requests.get(url, headers=headers)
        
        # 檢查請求是否成功
        if response.status_code == 200:
            # 解析網頁內容
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 獲取小說文本的 div 元素
            novel_text = soup.find("div", class_="js-novel-text p-novel__text")
            
            if novel_text:
                # 將內容寫入文件
                file.write(f"<h1>第 {i} 章</h1>\n")
                file.write(str(novel_text))
                file.write("\n\n")
            else:
                print(f"在第 {i} 頁中未找到小說文本。")
        else:
            print(f"無法訪問 {url}，狀態碼: {response.status_code}")

print("所有頁面已成功下載到 novel_content.html。")