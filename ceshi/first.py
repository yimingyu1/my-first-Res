from selenium import webdriver
import time
#profile_directory='/Users/yimingyu/Library/ApplicationSupport/Firefox/Profiles/le9ixg1d.default'
from selenium.webdriver import ActionChains

driver=webdriver.Firefox()
driver.get('https://www.baidu.com')
#driver.implicitly_wait(20)
js='''
    $('input#search-key').val('selenium');
    $('input.btn-engine').click();
    '''
driver.execute_script(js)
time.sleep(4)
driver.close()


