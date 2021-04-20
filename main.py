from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from cut_pic import *
# ChromeDriver 89.0.4389.23
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('.\chromedriver.exe', options=options)

url = "https://www.geologycloud.tw/map/liquefaction/zh-tw"
addkey = input("輸入完整地址:")
driver.get(url)
# print(driver.title)
driver.set_window_size(1920, 1080)
# driver.fullscreen_window()
click = driver.find_element_by_id('btn_Soillique_OK')
click.click()
# 地址輸入框
addinput = driver.find_element_by_xpath('//*[@id="map-geocoding-input"]/input')
addinput.send_keys(addkey)
# 地址輸入框_搜尋
add_btn = driver.find_element_by_xpath('//*[@id="map-geocoding-input"]/span[3]')
add_btn.click()
time.sleep(3)
add_list_element = driver.find_element_by_xpath('//*[@id="map-geocoding-listw"]')
add_list = add_list_element.text.split()
# print(add_list)
if len(add_list) == 0 or add_list[0] == '內政部門牌地址定位服務目前查無此地址':
    print('address error!')
    driver.close()
# elif len(add_list) == 1:
#     add_select = driver.find_element_by_xpath('//*[@id="map-geocoding-list"]/a/i')
#     add_select.click()
# else:
#     c = 0
#     for i in add_list:
#         print(str(c)+' '+i)
#         c = c+1
else:
    add_select = driver.find_element_by_xpath('//*[@id="map-geocoding-list"]/a/i')
    add_select.click()
# 印出搜尋結果
# time.sleep(1)
    WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located
                                        ((By.XPATH, '//*[@id="map"]/div[1]/div[2]/div[4]/div/div[1]/div')))
    add_info = driver.find_element_by_xpath('//*[@id="map"]/div[1]/div[2]/div[4]/div/div[1]/div').text
    add_result = add_info.split()[1]
    print("查詢結果: "+add_result)
    # 新增縮放，防止圖片失真
    driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[1]/div[1]/div[1]/button/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="map"]/div[2]/div[1]/div[1]/div[2]/button/i').click()
    time.sleep(1)
# 點選'地質圖'
    map_tab = driver.find_element_by_id('map_tab_geo')
    map_tab.click()
    time.sleep(1)
    map_tab_geo = driver.find_element_by_xpath('//*[@id="map-geoLayer-panel"]/div[1]/div[2]/div/div[1]/div')
    map_tab_geo.click()
    time.sleep(2)
# 截圖存放
    pickpath = '.\\' + time.strftime('%Y%m%d%H%M%S') + '.png'
# print(pickpath)
    driver.get_screenshot_as_file(pickpath)

    time.sleep(1)
    driver.close()

    crop_img(pickpath)
    # print(get_RGBColorCode('crop.jpg', 0, 0))
    liquefaction = get_RGBColorCode('crop.jpg', 5, 5)
    print(liquefaction)
    # 以RGB判斷液化範圍
    if liquefaction[0]<200 and liquefaction[1]>200 and liquefaction[2]<200:
        print('土壤液化低潛勢範圍')
    elif liquefaction[0]>200 and liquefaction[1]>200 and liquefaction[2]<200:
        print('土壤液化中潛勢範圍')
    elif liquefaction[0]>200 and liquefaction[1]<200 and liquefaction[2]<200:
        print('土壤液化高潛勢範圍')
    else:
        print('未調查區')

input("press any key to close...")
