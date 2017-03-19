## What's this

This is a simple python 3 script that parses all the project links on *[https://www.cantierecreativo.net/portfolio/](https://www.cantierecreativo.net/portfolio/)*, then scrapes the project name and the brief description.
The information is then stored in a .csv file, in the format *"Name (Description)"*.

This script uses the libraries **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup)** and **[requests](http://docs.python-requests.org)**, which can be installed via pip
    
    pip install beautifulsoup4
    pip install requests
    
or using

    pip install -r requirements.txt

Click [here](https://www.python.org/ftp/python/3.6.0/python-3.6.0.exe) to download Python 3.6.
pip is already bundled with the Python package since 2.7.9+ or 3.4+, so there's no need to install it. Still, to make sure you have the last version, you can run

    pip install -U pip
    
on macOS/Linux, or

    python -m pip install -U pip
    
on Windows.
