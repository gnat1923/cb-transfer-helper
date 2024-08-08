import sys
import os.path
import csv
import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#run script with file path as first arg, file name as second
x = sys.argv[1]
y = sys.argv[2]

file_dir = os.path.join(x, y)
print(str(file_dir))

master_list = []

with open(file_dir) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        master_list.append(row)

#break master list into chunks 15 units long
chunks = [master_list[i:i+15] for i in range(0, len(master_list),15)]

#initalise Selenium driver
driver.get("https://kunden.commerzbank.de/dailybanking/payments")
print(input("Please log in. Press enter to continue."))

#iterate over every list in chunks
transfer_count = 1
for chunk in chunks:
    total_transfer = 0
#iterate over every dict in chunk
    for dict in chunk:
        name = dict["Name"]
        iban = dict["Iban"]
        amount = dict["Amount"]
        ref = dict["Reference"]
#sum Amount2
        total_transfer += float(dict["Amount2"])
#paste correct value into correct browser field
        print(f"{name} - {iban} - {amount} - {ref}")

        try:
            name_elem = driver.find_element(By.NAME, 'recipient')
            print("Name found")
            name_elem.clear()
            name_elem.send_keys(name)

        except:
            print("Unable to find name")

        try:
            iban_elem = driver.find_element(By.ID, 'sepa__suggester--receiver-iban_textfield')
            print("IBAN found")
            iban_elem.clear()
            iban_elem.send_keys(iban)

        except:
            print("Unable to find IBAN")

        try:
            amount_elem = driver.find_element(By.NAME, 'amount')
            print("Amount found")
            amount_elem.clear()
            amount_elem.send_keys(amount)

        except:
            print("Unable to find amount")

        try:
            ref_elem = driver.find_element(By.NAME, 'purpose')
            print("Ref found")
            ref_elem.clear()
            ref_elem.send_keys(ref)
            time.sleep(5)

        except:
            print("Unable to find ref")

        try:
            next_payment = driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Zahlung hinzufügen')]]")
            next_payment.click()
            time.sleep(3)

        except:
            print("Unable to find next payment btn")
            #driver.quit()
            break

#wait after every paste (2 sec?)

#click weiter

#increment counter, print batch total
    print(f"Transfer number {transfer_count}: Total: {total_transfer:.2f}€")
    transfer_count += 1
    print(input("Continue? Press enter"))