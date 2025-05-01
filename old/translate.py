import openai
from bs4 import BeautifulSoup

# 設定 OpenAI API 金鑰
openai.api_key = "sk-5678ijklmnopabcd5678ijklmnopabcd5678ijkl"

def translate_text(text, target_language):
    response = openai.Completion.create(
        engine="davinci-002",  # 使用最新的模型
        prompt=f"Translate the following text into {target_language}: {text}\n",
        max_tokens=1000,  # 根據需要調整最大字數
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# 讀取原始 HTML 文件
with open("novel_content.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有包含日文的 div 元素
novel_text_div = soup.find("div", class_="js-novel-text p-novel__text")

if novel_text_div:
    # 獲取文本並翻譯
    original_text = novel_text_div.get_text()
    translated_text = translate_text(original_text, "Chinese")
    
    # 用翻譯後的文本替換原始文本
    novel_text_div.string = translated_text

# 將翻譯後的內容寫入新的 HTML 文件
with open("translated_novel_content.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("翻譯完成，已生成新的 HTML 文件：translated_novel_content.html")