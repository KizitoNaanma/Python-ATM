import string
import os
import getpass


# Hardcoded lists of users, their PINs and bank statements (Would Advice you use some Encryption Technology and a way to fetch data of some kind)
users = ['cyber', 'cybermonk', 'JOSHUA']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER YOUR USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('***********************************')
		print('INVALID USERNAME, PLEASE CONFIRM IT')
		print('***********************************')

# comparing pin
while count < 3:
	print('------------------')
	print('******************')
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	print('******************')
	print('------------------')
	if pin.isdigit():
		if user == 'cyber':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()

		if user == 'cybermonk':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'JOSHUA':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
	else:
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')
		count += 1
	
# in case of a valid pin- continuing, or exiting
if count == 3:
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------')
print()
print('--------------------------')
print('**************************')	
print(str.capitalize(users[n]), 'welcome, What Would i help you with')
print('**************************')
print('**************************')
print('**************************')
print('----------ATM SYSTEM-----------')


#Hard coding the main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nBalance__(S) \nWithdraw___(W) \nDeposit__(L)  \nChange PIN_(P)  \nLogout_______(Q) \n: ').lower()
	print('*******************************')
	print('-------------------------------')
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print('*********************************************')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'NAIRA ON YOUR ACCOUNT.')
		print('*********************************************')
		print('---------------------------------------------')
		
	elif response == 'w':
		print('---------------------------------------------')
		print('*********************************************')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('*********************************************')
		print('---------------------------------------------')
		if cash_out%1 != 0:
			print('------------------------------------------------------')
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 1 THOUSAND NAIRA NOTES EXACTLY')
			print('******************************************************')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('*****************************')
			print('     INSUFFICIENT BALANCE    ')
			print('*****************************')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			print('-----------------------------------')
			print('***********************************')
			print('YOUR NEW ACCOUNT BALANCE IS: ', amounts[n], 'NAIRA')
			print('***********************************')
			print('-----------------------------------')
			
	elif response == 'l':
		print()
		print('---------------------------------------------')
		print('*********************************************')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
		print('*********************************************')
		print('---------------------------------------------')
		print()
		if cash_in%1 != 0:
			print('----------------------------------------------------')
			print('****************************************************')
			print('AMOUNT YOU WANT TO DEPOSIT MUST TO MATCH 1 NAIRA NOTES')
			print('****************************************************')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			print('----------------------------------------')
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'EURO')
			print('****************************************')
			print('----------------------------------------')
	elif response == 'p':
		print('-----------------------------')
		print('*****************************')
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')
		print('-----------------------------')
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
			print('------------------')
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')
			print('-------------------')
			if new_ppin != new_pin:
				print('------------')
				print('************')
				print('PIN MISMATCH')
				print('************')
				print('------------')
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:
			print('-------------------------------------')
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
			print('*************************************')
			print('-------------------------------------')
	elif response == 'q':
		exit()
	else:
		print('******************')
		print('INVALID RESPONSE  ')
		print('******************')
#THis is Just a simulation, an ATM system is way more complicated
#For Learntocode.io BY Joshua Anop (Cybermonk)
