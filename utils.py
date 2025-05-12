from bs4 import BeautifulSoup


def clean_trending_html(html_content: str):
    base_url = "https://www.github.com"
    soup = BeautifulSoup(html_content, 'html.parser')

    div_elements = soup.find_all("div", attrs={"data-hpc": True})
    
    links = []
    titles = []
    
    # 遍历每个符合条件的 <div>
    for div in div_elements:
        # 在 <div> 内查找所有 <h2 class="h3 lh-condensed"> 中的 <a>
        h2_tags = div.find_all("h2", class_="h3 lh-condensed")
        for h2 in h2_tags:
            a_tag = h2.find("a")
            if a_tag and a_tag.get("href"):
                titles.append(a_tag["href"].rsplit("/", 1)[-1])
                links.append(base_url + a_tag["href"])
    
    return [{"title": title, "link": link} for title, link in zip(titles, links)]



def clean_content_html(html_content: str):
    soup = BeautifulSoup(html_content, "html.parser")
    # 提取 <article class="markdown-body entry-content container-lg">
    article_content = soup.find("article", class_="markdown-body entry-content container-lg").get_text(strip=True)

    # 提取 <p class="f4 my-3">
    p_content = soup.find("p", class_="f4 my-3").get_text(strip=True)
    
    return f"""description: {p_content} \n\n documents: {article_content}"""
    

