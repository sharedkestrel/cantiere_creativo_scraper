import requests
from bs4 import BeautifulSoup

#sets the url to open, then opens it
url = "https://www.cantierecreativo.net/portfolio/"
portfolio = requests.get(url)
#turns the returned object into text so that BeautifulSoup can process it
html = portfolio.text
soup = BeautifulSoup(html, "html.parser")
#finds every <a> tag with the works-list__item__link class, since they contain the "href"s to the projects
proj_links = soup.find_all("a", class_="works-list__item__link")
#creates the csv file and writes the first line
p = open('projects.csv', 'w')
p.write("Commissioner (Description)")
#for every matching <a> tag, extracts the links and then parses each page
for a_link in proj_links:
    link = a_link.get('href')
    #creates a full link since the site contains local links
    full_link = "https://www.cantierecreativo.net" + link
    proj_page = requests.get(full_link)
    proj_html = proj_page.text
    proj_soup = BeautifulSoup(proj_html, "html.parser")
    #finds the tag containing the project name and strips out the HTML
    head_soup = proj_soup.find("h1", class_="hero__heading")
    head = head_soup.get_text()
    if ";" in head:
        head = head.replace(";", "")
    #finds the tag containing the project description and strips out the HTML
    desc_soup = proj_soup.find("h2", class_="hero__text")
    desc = desc_soup.get_text()
    #joins the two found strings and adds them to a new line in the csv file
    data = "\n" + head + " (" + desc + ")"
    p.write(data)
p.close()
