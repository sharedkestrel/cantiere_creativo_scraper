import requests
from bs4 import BeautifulSoup

url = "https://www.cantierecreativo.net/portfolio/"
portfolio = requests.get(url)
html = portfolio.text
soup = BeautifulSoup(html, "html.parser")
proj_links = soup.find_all("a", class_="works-list__item__link")
p = open('projects.csv', 'w')
p.write("Commissioner (Description)")
for a_link in proj_links:
    link = a_link.get('href')
    full_link = "https://www.cantierecreativo.net" + link
    proj_page = requests.get(full_link)
    proj_html = proj_page.text
    proj_soup = BeautifulSoup(proj_html, "html.parser")
    head_soup = proj_soup.find("h1", class_="hero__heading")
    head = head_soup.get_text()
    if ";" in head:
        head = head.replace(";", "")
    desc_soup = proj_soup.find("h2", class_="hero__text")
    desc = desc_soup.get_text()
    data = "\n" + head + " (" + desc + ")"
    p.write(data)
p.close()
