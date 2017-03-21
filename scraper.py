import requests
from bs4 import BeautifulSoup
import os.path


def soupify(site):
    attempts = 0
    #give five attempts to connect to the site, else raise an exception
    while attempts < 5:
        #tries to open the given url, then prepares the HTML to get parsed
        try:
            print("Connecting to %s..." % site)
            page = requests.get(site, timeout=30)
            html = page.text
            soup = BeautifulSoup(html, "html.parser")
            return soup
        except TimeoutError:
            print("Connection failed, trying again...")
            attempts += 1
        except ConnectionError:
            print("Connection failed, trying again...")
            attempts += 1
    raise ConnectionError("Connection failed")

#let the user input the file path
path = input("Insert the path for the csv file: (if none is inserted, the working directory will be used)\n")
# creates the csv file and writes the first line
try:
    p = open(os.path.join(path, 'projects.csv'), 'w')
except FileNotFoundError:
    raise FileNotFoundError("The %s folder does not exist." % path)
except PermissionError:
    raise PermissionError("The script doesn't have permission to write in %s" % path)
p.write("Commissioner (Description)")
url = "https://www.cantierecreativo.net/portfolio/"
soup = soupify(url)
# finds every <a> tag with the works-list__item__link class, since they contain the "href"s to the projects
proj_links = soup.find_all("a", class_="works-list__item__link")
# for every matching <a> tag, extracts the links and then parses each page
for a_link in proj_links:
    link = a_link.get('href')
    # creates a full link since the site contains local links
    full_link = "https://www.cantierecreativo.net" + link
    proj_soup = soupify(full_link)
    # finds the tag containing the project name and strips out the HTML
    head_soup = proj_soup.find("h1", class_="hero__heading")
    head = head_soup.get_text()
    if ";" in head:
        head = head.replace(";", "")
    # finds the tag containing the project description and strips out the HTML
    desc_soup = proj_soup.find("h2", class_="hero__text")
    desc = desc_soup.get_text()
    # joins the two found strings and adds them to a new line in the csv file
    data = "\n %s (%s)" % (head, desc)
    print("Writing data to csv...\n")
    p.write(data)
p.close()
print("Process complete!")
