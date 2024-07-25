import sys
import os.path
import csv
import pprint
import time

#run script with file pat as first arg, file name as second
x = sys.argv[1]
y = sys.argv[2]
print(x, y, sep="\n")

file_dir = os.path.join(x, y)
print(str(file_dir))

master_list = []

with open(file_dir) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        master_list.append(row)

#pprint.pprint(master_list)

chunks = [master_list[i:i+15] for i in range(0, len(master_list),15)]
#pprint.pprint(chunks)
#print(len(chunks))
#pprint.pprint(chunks[6])
'''
counter = 1

for list in chunks:
    for dict in list:
        print(f"{counter} {dict['Name']} - {dict['Iban']} - {dict['Amount']} - {dict['Reference']}")
        counter += 1
        '''
pprint.pprint(chunks[0])
print(f"List is {len(chunks[0])} long.")

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
#wait after every paste (2 sec?)

#click weiter

#increment counter, print batch total
    print(f"Transfer number {transfer_count}: Total: {total_transfer:.2f}€")
    transfer_count += 1
    print(input("Continue? Press enter"))

'''
Selenium todos
    Page title - <title>Überweisung - Commerzbank</title>
    Name filed name - name="recipient"
    Amount Field Name - name="amount"
    Iban field name - class="lsgs-1efab--text-field-input" // id="sepa__suggester--receiver-iban_textfield"
    Reference field name - name="purpose"
    Weiter field name - <span class="lsgs-1efab--spinner__overlay"></span> // <li class="lsgs-1efab--button"><button class="lsgs-1efab--action lsgs-1efab--action__interactive lsgs-1efab--action__no-overlay" tabindex="0" type="button"><span class="lsgs-1efab--action-inner"><div class="lsgs-1efab--dwindle lsgs-1efab--dwindle__primary lsgs-1efab--dwindle__circle-button lsg-1efab---theme__brand"><div class="lsgs-1efab--dwindle-inner"><div class="lsgs-1efab--button-inner lsgs-1efab--button-inner-icon__right"><div class="lsgs-1efab--icon"><div class="lsgs-1efab--icon-inner lsgs-1efab--icon__small lsgs-1efab--icon__default"><svg width="24px" height="24px" focusable="false" role="" aria-hidden="true" id="lsgs-1efab--icon-lyst8pyf" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title id="lsgs-1efab--icon-lyst8pyf-title"> </title><path d="m16.81 4.42-1.62 1.16L19.06 11H2v2h17.06l-3.87 5.42 1.62 1.16L22.23 12l-5.42-7.58z"></path></svg></div></div><div class="">Weiter</div></div></div></div></span><span class="lsgs-1efab--spinner__overlay"></span><span class="lsgs-1efab--spinner-label__hidden" aria-live="assertive" aria-atomic="true"></span></button></li>
'''