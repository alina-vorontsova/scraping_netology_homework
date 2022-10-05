import bs4
import requests


def get_articles_list():
    text = requests.get(URL).text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")

    return articles

def get_links():
    articles = get_articles_list()
    links = [] 
    for article in articles: 
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        article_url = f'https://habr.com{href}'
        links.append(article_url)

    return links

def get_info():
    links = get_links()
    for link in links:
        text = requests.get(link).text
        soup = bs4.BeautifulSoup(text, features="html.parser")
        article_text = soup.find(class_="article-formatted-body").text.strip()

        for keyword in KEYWORDS:
            if keyword in article_text:
                date = soup.find("time").get("title") 
                title = soup.find("h1", class_="tm-article-snippet__title tm-article-snippet__title_h1").find("span").text
                print(f'{date} - {title} - {link}')
                break


if __name__ == "__main__":
    
    URL = "https://habr.com/ru/all/"
    KEYWORDS = ["дизайн", "фото", "web", "python"]

    get_info()