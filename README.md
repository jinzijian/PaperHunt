# PaperHunt

## 项目简介 | Project Introduction

**PaperHunt** 是一个基于 Python 和 OpenAI API 的自动化工具，旨在每日监测特定作者的新发表论文，判断其与您的研究领域的相关性，并生成分类和摘要，最终汇总成每日报告发送给您。

**PaperHunt** is an automated tool based on Python and the OpenAI API. It aims to monitor newly published papers by specific authors daily, determine their relevance to your research field, categorize and summarize them, and finally compile them into a daily report sent to you.

## 功能特性 | Features

- **自动检索**：每日自动获取指定作者的新论文。

  **Automatic Retrieval**: Automatically fetch new papers from specified authors daily.

- **智能分析**：利用 OpenAI 的 GPT 模型，判断论文与您的研究兴趣的相关性。

  **Intelligent Analysis**: Use OpenAI's GPT model to assess the relevance of papers to your research interests.

- **分类与摘要**：对相关论文进行主题分类，并生成简明摘要。

  **Categorization and Summarization**: Categorize relevant papers and generate concise summaries.

- **报告生成**：将分析结果整理成易于阅读的每日报告。

  **Report Generation**: Organize analysis results into an easy-to-read daily report.

- **邮件通知**：自动发送报告到您的邮箱，方便快捷。

  **Email Notification**: Automatically send the report to your email for convenience.

## 安装与使用 | Installation and Usage

### 环境要求 | Prerequisites

- Python 3.7 或更高版本

  Python 3.7 or higher

- 依赖库详见 `requirements.txt`

  Dependencies listed in `requirements.txt`

### 安装步骤 | Installation Steps

1. **克隆仓库**

   **Clone the repository**

   ```bash
   git clone https://github.com/your_username/PaperHunt.git
   cd PaperHunt

配置 config.py 文件

在项目目录下，创建 config.py 文件并按照以下示例进行配置。你可以根据你的需求自定义作者和研究兴趣列表：

Create the config.py file

In the project directory, create a config.py file and configure it as follows. Customize the author and interest lists according to your needs:

python
复制代码
# config.py

# 指定要监控的作者列表
author_list = [
    "Bowen Zhao",
    "Yann LeCun",
    "Jacob Steinhardt",
    "Dawn Song"
]

# 指定研究兴趣列表，供相关性分析使用
interest_list = [
    'llm和强化学习结合,比如dpo ppo rlhf mcts等',
    'llm和code结合',
    'llm reasoning能力',
    '多模态大模型'
]
配置 .env 文件

在项目目录下，创建 .env 文件以包含敏感信息，如 OpenAI API 密钥和电子邮件配置：

Create the .env file

In the project directory, create a .env file to store sensitive information, such as the OpenAI API key and email configuration:

makefile
复制代码
# .env 文件示例

OPENAI_API_KEY=your_openai_api_key_here

# 电子邮件设置
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_google_app_specific_password_here  # 将 Google 应用专用密码粘贴在这里
TO_EMAIL=recipient_email@example.com

# 邮件服务器配置
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
安装依赖

执行以下命令安装所需的依赖库：

Install dependencies:

bash
复制代码
pip install -r requirements.txt
运行 PaperHunt

完成配置后，运行以下命令启动 PaperHunt：

Run PaperHunt:

bash
复制代码
python paperhunt.py
配置说明 | Configuration Notes
author_list: 包含您希望 PaperHunt 监控的作者姓名。
interest_list: 包含与您的研究相关的主题或关键词，用于判断论文的相关性。
.env 文件中的 EMAIL_USER 和 EMAIL_PASSWORD 是用于发送每日报告的电子邮件凭据。
常见问题 | FAQ
1. 如何生成 Google 应用专用密码？
您可以通过以下步骤生成 Google 应用专用密码：

访问 Google 应用密码页面。
登录您的 Google 帐户。
根据提示创建一个应用密码，并将其复制到 .env 文件中的 EMAIL_PASSWORD 字段。
