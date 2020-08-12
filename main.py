import sys

sys.path.append('/Users/mkabsta/.pyenv/versions/3.6.5/lib/python3.6/site-packages')
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
import time

def get_text(url, xpath):
    driver.get(url)
    abst = driver.find_element_by_xpath(xpath).text
    pyperclip.copy(abst)
    return abst



def translate():
    driver.get("https://www.deepl.com/translator")
    driver.find_element_by_xpath("//*[@id='dl_translator']/div[1]/div[3]/div[2]/div/textarea").send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(10)
    text_en = driver.find_element_by_xpath("//*[@id='dl_translator']/div[1]/div[4]/div[3]/div[1]/textarea").get_attribute('value')
    return text_en



if __name__ == "__main__":
    """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/mkabsta/Documents/programming/python/Selenium/chromedriver', options=options)
    """
    driver = webdriver.Chrome('/Users/mkabsta/Documents/programming/python/Selenium/chromedriver')
    paper_url = "https://www.sciencedirect.com/science/article/abs/pii/S0376042119300302"
    abst_xpath = '//*[@id="abspara0010"]'
    get_text(paper_url, abst_xpath)
    abst_text_en = translate()
    print(abst_text_en)
