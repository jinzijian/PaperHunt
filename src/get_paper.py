import requests
import xml.etree.ElementTree as ET
from datetime import date, timedelta

def get_papers_by_author(author_names):
    base_url = 'http://export.arxiv.org/api/query?'
    
    #构建查询参数
    end_date = date.today()
    start_date = end_date - timedelta(days=7)
    
    # 构建查询参数
    author_query = " OR ".join([f'au:"{name}"' for name in author_names])
    params = {
        'search_query': f'({author_query}) AND submittedDate:[{start_date.strftime("%Y%m%d")}0000 TO {end_date.strftime("%Y%m%d")}2359]',
        'start': 0,
        'max_results': 100,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }

    # # 构建查询参数
    # today =  date.today()
    # one_year_ago = today - timedelta(days=1)
    # author_query = " OR ".join([f'au:"{name}"' for name in author_names])
    # params = {
    #     'search_query': f'({author_query}) AND submittedDate:[{one_year_ago}0000 TO {today}2359]',
    #     'start': 0,
    #     'max_results': 100,
    #     'sortBy': 'submittedDate',
    #     'sortOrder': 'descending'
    # }
    
    # 发送请求
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # 解析XML响应
        root = ET.fromstring(response.content)
        
        # 提取文章信息
        articles = []
        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
            published = entry.find('{http://www.w3.org/2005/Atom}published').text
            authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
            
            articles.append({
                'title': title,
                'summary': summary,
                'published': published,
                'authors': authors
            })
        
        return articles
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

# 使用示例
if __name__ == "__main__":
    author_names = ["Bowen Zhao","Yoshua Bengio", "Geoffrey Hinton", "Yann LeCun"]  # 替换为您想搜索的作者名字列表
    results = get_papers_by_author(author_names)
    
    if results:
        print(f"Found {len(results)} articles by {', '.join(author_names)} submitted today:")
        for article in results:
            print(f"\nTitle: {article['title']}")
            print(f"Authors: {', '.join(article['authors'])}")
            print(f"Published: {article['published']}")
            print(f"Summary: {article['summary'][:200]}...")  # 只打印摘要的前200个字符
    else:
        print(f"No articles found for {', '.join(author_names)} today.")