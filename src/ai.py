import openai

from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中获取 API 密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

def is_relevant(summary, interest_description):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个科研助手，帮助判断论文摘要与特定研究领域的相关性。"},
            {"role": "user", "content": f"我的研究兴趣是：{interest_description}\n以下是论文摘要：{summary}\n请判断这篇论文是否与我的研究领域相关，回答“是”或“否”。"}
        ]
    )
    result = response.choices[0].message.content
    return '是' in result

def generate_summary(summary):
    response = openai.chat.completions.create(
       model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "你是一个智能助手，擅长翻译学术论文。"},
            {"role": "user", "content": f"请翻译该论文摘要到中文：{summary}"}
        ]
    )
    result = response.choices[0].message.content
    return result

if __name__ == '__main__':
    # 测试数据
    test_summary = (
        "本文提出了一种新的深度学习模型，用于图像识别，"
        "实验结果表明该模型在多个数据集上取得了领先的性能。"
    )
    interest_description = "我的研究兴趣是计算机视觉和深度学习，特别是图像识别方面的技术。"

    # 测试相关性判断函数
    relevance = is_relevant(test_summary, interest_description)
    print(f"论文是否与您的研究领域相关：{'是' if relevance else '否'}")

    # 如果相关，生成摘要
    if relevance:
        summary = generate_summary(test_summary)
        print("生成的摘要：")
        print(summary)