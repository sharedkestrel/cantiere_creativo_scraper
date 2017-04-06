import requests
from bs4 import BeautifulSoup
import os.path


def open_csv(path):
    try:
        p = open(os.path.join(path, 'projects.csv'), 'w')
    except FileNotFoundError:
        raise FileNotFoundError("The %s folder does not exist." % path)
    except PermissionError:
        raise PermissionError("The script doesn't have permission to write in %s" % path)
    p.write("Commissioner, Description")
    return p


def soupify(site):
    attempts = 0
    # give five attempts to connect to the site, else raise an exception
    while attempts < 5:
        # tries to open the given url, then prepares the HTML to get parsed
        try:
            print("Connecting to %s..." % site)
            page = requests.get(site, timeout=30)
            html = page.text
            fsoup = BeautifulSoup(html, "html.parser")
            return fsoup
        except TimeoutError:
            print("Connection failed, trying again...")
            attempts += 1
        except ConnectionError:
            print("Connection failed, trying again...")
            attempts += 1
    raise ConnectionError("Connection failed")


def find_elements(soup, tag, clss):
    elements = soup.find_all(tag, class_=clss)
    return elements


def get_full_link(link):
    link = link.get('href')
    full_link = "https://www.cantierecreativo.net" + link
    return full_link


def get__text(tag):
    tag = tag.get_text()
    if ";" in tag:
        tag = tag.replace(";", "")
    return tag


def write_data(p, head, desc):
    data = "\n %s (%s)" % (head, desc)
    print("Writing data to csv...\n")
    p.write(data)


p = open_csv(input("Insert the path for the csv file: (if none is inserted, the working directory will be used)\n"))
soup = soupify("https://www.cantierecreativo.net/portfolio/")
elements = find_elements(soup, "a", "works-list__item__link")
for link in elements:
    full_link = get_full_link(link)
    proj_soup = soupify(full_link)
    proj_name = find_elements(proj_soup, "h1", "hero__heading")
    head = proj_name.get__text()
    proj_desc = find_elements(proj_soup, "h2", "hero__text")
    desc = proj_desc.get__text()
    write_data(p, head, desc)
p.close()
print("Process complete!")
