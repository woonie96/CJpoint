import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_bs4():
    Login_info ={
        'mbr_id': 'woonstar2004',
        'pwd_in': 'Star*9388'
    }

    url = "https://www.cjone.com/cjmweb/login.do?return_url=https%3A%2F%2Fwww.cjone.com%2Fcjmweb%2Fmy-one%2Fpoint.do%3Frnd%3D"
    base_url = "https://www.cjone.com/"
    with requests.Session() as s:

        html = urllib.request.urlopen(url)

        source = html.read()

        soup = BeautifulSoup(source, "html.parser")
        # print(soup.find(class_="input_capcha"))
        # print(soup.find_all("img"))

        for img in soup.find_all("img"):
            #print(img)
            img = soup.find("img")
            img_src = img.get("src")
            img_url = base_url + img_src
            img_name = img_src.replace("/","")
            print(type(img_url))
            # urllib.request.urlretrieve((img_url,"image/"+img_name))


def sel_test():
    driver = webdriver.Chrome('chromedriver.exe')
    url = "https://www.cjone.com/cjmweb/login.do?return_url=https%3A%2F%2Fwww.cjone.com%2Fcjmweb%2Fmy-one%2Fpoint.do%3Frnd%3D"
    driver.get(url)


    elem_css = driver.find_element_by_css_selector("#imageCatpcha > img")
    img = elem_css.get_attribute("src")

    print(img)



    img_name = "capcha.png"


    urllib.request.urlretrieve(img,"image/"+img_name)
    

    driver.close()



def main():
    print("main")
if __name__ == "__main__":
    sel_test()
    #test_bs4()
