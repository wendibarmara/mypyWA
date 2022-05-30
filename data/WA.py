from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r"C:\mypyWA\chromedriver.exe")
driver.get(r"https://web.whatsapp.com")

print('Masukkan nomor HP ')
no_hp = input("No HP: ")
print(no_hp)
pesan = input("Isi pesan WA :")

inputno = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
inputno.send_keys(no_hp)
time.sleep(20)
try:
    driver.find_element(By.XPATH, "//div[@aria-label='Search results.']")
    driver.find_element(By.XPATH, "//div[@title='Search input textbox']").clear()
    inputno1 = driver.find_element(By.XPATH, "//div[@title='Search input textbox']")
    inputno1.send_keys(no_hp, Keys.ENTER)
    inputpesan = driver.find_element(By.XPATH, "//div[@title='Type a message']")
    inputpesan.send_keys(pesan, Keys.ENTER)
    #display all message by contact
    print([my_elem.text for my_elem in
           driver.find_elements(By.XPATH, "//div[@class='_3K4-L']//*[contains(@class,'_2wUmf')]//descendant::div["
                                          "@class='_22Msk']")])

    # print("HTML code:\n", code)
    print("berhasil")

    inputno1 = None
    inputpesan = None
except NoSuchElementException:
    print("Nomor HP tidak terdaftar di contact")
    print("gagal")

driver.close
