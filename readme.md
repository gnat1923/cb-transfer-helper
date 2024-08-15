# cb-transfer helper
*A script to take the monotony out out copy-pasting mutiple bank transfers into Commerzbank's bank transfer page*
## Requirements
You will need a CSV export of the transfers to be made, with the following headings:
1. Name - Recipient name
2. Iban - Recipient IBAN
3. Amount - Euro amount, with euro and cents separated by "," (because, Germany)
4. Reference - The payment reference
5. Amount2 - Euro amount, with euro and cents separated by "." (for mathematical operations)

You will also need the *Selenium* module for Phyhon (see requirements.txt)

## Quickstart
- Ensure your .csv file is in the format outlined abouve and that Selenium is installed
- Run the script with the .csv file location as the first arguement, and the file name as the second
- Selenium will open an instance of google Chrome. Sign into you Commerzbank account and complete any required 2FA
- When fully signed in and the transfer page is visible, press enter on your terminal to continue
- The script will automatically populate fields, up to 15 transfers at a time
- When the current block of transfers is finished, script will output a total amount
- Please verify this total, confirm payment, and click "new transfer"
- Hit enter on your terminal. The script continues.

## ToDo
- Create log export. This will help in the instance of Commerzbank crashing / unexpected behaviour
- On completion of final transaction copy /paste, if final chunk is <15, do not click "add transaction"