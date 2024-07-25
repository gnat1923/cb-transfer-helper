from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

name = "Chris"
iban = "DE76500105170526029730"
amount = "1,23"
ref = "ref"

driver = webdriver.Chrome()

driver.get("https://kunden.commerzbank.de/dailybanking/payments")
print(input("Please log in. Press enter to continue."))
#time.sleep(5)
for x in range(5):
    try:
        name_elem = driver.find_element(By.NAME, 'recipient')
        print("Name found")
        name_elem.clear()
        name_elem.send_keys(name)

    except:
        print("Unable to find name")

    try:
        iban_elem = driver.find_element(By.ID, 'sepa__suggester--receiver-iban_textfield')
        print("iban found")
        iban_elem.clear()
        iban_elem.send_keys(iban)

    except:
        print("Unable to find iban")

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
        driver.quit()
        break

print(input("Continue?"))
'''
Selenium todos
    Page title - <title>Überweisung - Commerzbank</title>
    Name filed name - name="recipient" class=lsgs-1efab--text-field-input
    Amount Field Name - name="amount" class=lsgs-1efab--text-field-input
    Iban field name - class="lsgs-1efab--text-field-input" // id="sepa__suggester--receiver-iban_textfield"
    Reference field name - name="purpose"
    Weiter field name - <span class="lsgs-1efab--spinner__overlay"></span> // <li class="lsgs-1efab--button"><button class="lsgs-1efab--action lsgs-1efab--action__interactive lsgs-1efab--action__no-overlay" tabindex="0" type="button"><span class="lsgs-1efab--action-inner"><div class="lsgs-1efab--dwindle lsgs-1efab--dwindle__primary lsgs-1efab--dwindle__circle-button lsg-1efab---theme__brand"><div class="lsgs-1efab--dwindle-inner"><div class="lsgs-1efab--button-inner lsgs-1efab--button-inner-icon__right"><div class="lsgs-1efab--icon"><div class="lsgs-1efab--icon-inner lsgs-1efab--icon__small lsgs-1efab--icon__default"><svg width="24px" height="24px" focusable="false" role="" aria-hidden="true" id="lsgs-1efab--icon-lyst8pyf" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title id="lsgs-1efab--icon-lyst8pyf-title"> </title><path d="m16.81 4.42-1.62 1.16L19.06 11H2v2h17.06l-3.87 5.42 1.62 1.16L22.23 12l-5.42-7.58z"></path></svg></div></div><div class="">Weiter</div></div></div></div></span><span class="lsgs-1efab--spinner__overlay"></span><span class="lsgs-1efab--spinner-label__hidden" aria-live="assertive" aria-atomic="true"></span></button></li>
    Add payment - class=lsgs-1efab--action lsgs-1efab--action__interactive lsgs-1efab--action__no-overlay
'''