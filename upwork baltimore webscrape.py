import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


link = 'https://baltimorecity.marylandtaxsale.com/index.cfm?folder=previewitems'
driver = webdriver.Chrome(r"\chromedriver_win32\chromedriver.exe")
driver.get(link)
driver.maximize_window()

printcounter = 0
i = 1
a,p,f,s=[],[],[],[]

for j in range(3356547,3378648):
    driver.find_element_by_xpath(f'//*[@id="gotoPageNum"]/option[{i}]').click()
    if (printcounter == 50):
        printcounter = 0
        i = i+1
        driver.find_element_by_xpath(f'//*[@id="gotoPageNum"]/option[{i}]').click()
        a.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[1]').text)
        p.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[2]').text)
        f.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[3]').text)
        s.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[4]').text)
        printcounter += 1
        print(printcounter,driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[1]').text,j)
    else:
        a.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[1]').text)
        p.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[2]').text)
        f.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[3]').text)
        s.append(driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[4]').text)
        printcounter += 1
        print(printcounter,driver.find_element_by_xpath(f'//*[@id="cert{j}"]/td[1]').text,j)
print(i)

df = pd.DataFrame({'ADV NUM':a, 'Parcel ID':p,'Face Amount':f,'Status':s})

df.to_excel(r"Output.xlsx",index=False)

