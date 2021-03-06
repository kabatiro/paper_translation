import sys

sys.path.append('/Users/mkabsta/.pyenv/versions/3.6.5/lib/python3.6/site-packages')
from selenium import webdriver
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def get_text(url, xpath):
    driver.get(url)
    driver.implicitly_wait(10)
    abst = driver.find_element_by_xpath(xpath).text + "\nポテトト"
    pyperclip.copy(abst)
    return abst

def get_h2(url):
    driver.get(url)
    wait = WebDriverWait(driver, 100)
    wait.until(EC.visibility_of_element_located((By.ID, "body")))
    time.sleep(5)
    h2_list = driver.find_elements_by_tag_name("h2")
    h2_list_text = []
    for h2_item in h2_list:
        h2_list_text.append(h2_item.text)
    return h2_list_text


def translate():
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.deepl.com/translator")
    driver.find_element_by_xpath("//*[@id='dl_translator']/div[1]/div[3]/div[2]/div/textarea").send_keys(Keys.SHIFT, Keys.INSERT)
    text_en = driver.find_element_by_xpath("//*[@id='dl_translator']/div[1]/div[4]/div[3]/div[1]/textarea").get_attribute('value')
    t0 = time.time()
    for i in range(100):
        text_en = driver.find_element_by_xpath(
            "//*[@id='dl_translator']/div[1]/div[4]/div[3]/div[1]/textarea").get_attribute('value')
        if text_en[-4:-1]=='ポテト':
            break
        time.sleep(1)
    translate_time = time.time() - t0
    print('翻訳時間は{}秒'.format(round(translate_time, 1)))
    text_en = text_en.rstrip('ポテト').rstrip()
    return repr(text_en)



if __name__ == "__main__":
    """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('/Users/mkabsta/Documents/programming/python/Selenium/chromedriver', options=options)
    """
    driver = webdriver.Chrome('/Users/mkabsta/Documents/programming/python/Selenium/chromedriver')
    paper_url = "https://www.sciencedirect.com/science/article/pii/S0376042114000347"
    abst_xpath = '//*[@id="abspara0010"]'
    #print(get_text(paper_url, abst_xpath))
    #abst_text_en = translate()
    #print(abst_text_en)
    print(get_h2(paper_url))
