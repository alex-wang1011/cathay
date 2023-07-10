from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

# 使用 Chrome 瀏覽器
chrome_options = Options()
#chrome_options.add_argument("--headless")  # 使用無介面模式

# 設定模擬手機環境
mobile_emulation = {
    "deviceName": "iPhone 6/7/8 Plus"
}

# 創建資料夾
path = 'C://自動化/自動化截圖/國泰'
if not os.path.isdir(path):
  os.makedirs(path)
#
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(30)


# 開啟國泰世華銀行官網
driver.get("https://www.cathaybk.com.tw/cathaybk/")
pic_path = "C://自動化/自動化截圖/國泰/自動化題目一.png"
driver.save_screenshot(pic_path)

# 點選左上角的選單
menu_button = driver.find_element(By.XPATH, "//div[1]/header/div/div[1]/a/img[2]")
menu_button.click()
time.sleep(2)

# 點選「產品介紹」
product_intro = driver.find_element(By.XPATH, "//div[contains(text(), '產品介紹')]")
product_intro.click()

# 點選「信用卡」
credit_card_list = driver.find_element(By.XPATH, "//div[contains(text(), '信用卡')]")
credit_card_list.click()
time.sleep(2)
pic_path = "C://自動化/自動化截圖/國泰/自動化題目二.png"
driver.save_screenshot(pic_path)

# 計算項目數量
credit_card_items = len(driver.find_elements(By.XPATH,("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")))
# 輸出結果
print(f"信用卡列表中有 {credit_card_items} 個項目")

#信用卡介紹
Card_introduction = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a[1]")
Card_introduction.click()
time.sleep(2)

# 停卡選單(進入信用卡列表選單後計算(停發)信用卡數量並截圖)
for i in range(1, 12):
    Stop_Card = driver.find_element(By.XPATH, "//div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[%s]" % i)
    Stop_Card.click()
    time.sleep(1)
    # 執行截圖
    pic_path = "C://自動化/自動化截圖/國泰/自動化題目三_%s.png" % str(i)
    driver.save_screenshot(pic_path)

# 計算停卡數量(比對計算(停發)信用卡數量與截圖數量相同)
echild_elements = len(driver.find_elements(By.XPATH,("/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span")))

# 輸出結果
print(f"(停發)信用卡列表中有 {echild_elements} 個項目")
time.sleep(2)

# 關閉瀏覽器
driver.quit()
