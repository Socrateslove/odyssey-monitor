import requests
from datetime import datetime

# 这里不要直接写token
# 下一步我们会用GitHub Secrets安全保存
TOKEN = "YOUR_TOKEN_HERE"


def send_wechat(message):
    url = "https://www.pushplus.plus/send"

    data = {
        "token": TOKEN,
        "title": "🎬 奥德赛排片雷达测试",
        "content": message,
        "template": "html"
    }

    try:
        r = requests.post(url, json=data)
        print(r.text)

    except Exception as e:
        print("发送失败:", e)


def check_movie():

    keywords = [
        "奥德赛",
        "The Odyssey",
        "诺兰",
        "Christopher Nolan",
        "IMAX",
        "巨幕"
    ]

    # 测试消息
    message = f"""
<h3>🎬 奥德赛排片雷达启动</h3>

<p>监控状态：正常运行</p>

<p>检测时间：
{datetime.now()}</p>

<p>关键词：
{', '.join(keywords)}</p>

<p>后续将接入中国电影博物馆和淘票票排片。</p>
"""

    send_wechat(message)


if __name__ == "__main__":
    check_movie()
