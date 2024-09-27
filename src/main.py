from ai import *
from get_paper import get_papers_by_author
from send import send_email
from config import author_list, interest_list
def create_report(papers):
    report = "## 今日相关论文汇总\n\n"
    for paper in papers:
        report += f"### {paper['title']}\n"
        report += f"- **发表日期**: {paper['published']}\n"
        report += f"- **作者**: {', '.join(paper['authors'])}\n"
        report += f"- **匹配的研究兴趣**: {paper['matched_interest']}\n"
        # report += f"- **链接**: {paper['url']}\n"
        report += f"- **摘要**: {paper['summary']}\n\n"
    return report

def main():
    all_papers = []

    papers = get_papers_by_author(author_list)
    print(f"找到 {len(papers)} 篇论文。")
    for paper in papers:
        for interest in interest_list:
            if is_relevant(paper['summary'], interest):
                paper['matched_interest'] = interest
                paper['summary'] = generate_summary(paper['summary'])
                all_papers.append(paper)
                break

    if all_papers:
        report = create_report(all_papers)
        send_email(report)
    else:
        print("今日无相关论文。")

if __name__ == '__main__':
    main()