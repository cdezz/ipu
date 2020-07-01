import time
import datetime
from ftplib import FTP
import pyautogui
from twilio.rest import Client

print('Logging into IPU Website...')

ftp = FTP('ftp.ipu.ie', user='gibb902434', passwd='g90i24b34b')
ftp.login(user='gibb902434', passwd='g90i24b34b')

# IPU product file
file = ftp.nlst()[1]

print('Downloading IPU product file...')

with open(f"C:\MPS\{file}.exe", 'wb') as product_file:
	ftp.retrbinary(f"RETR {ftp.nlst()[1]}", product_file.write)

print('Download Complete.')

pyautogui.click(382, 1003)


panel = list(pyautogui.locateOnScreen(r'C:\Users\MPS\Desktop\icons\mpspanel.png'))
pyautogui.click(panel[0], panel[1])
time.sleep(1)

coords = list(pyautogui.locateOnScreen(r'C:\Users\MPS\Desktop\icons\dbupgrade.png'))
pyautogui.click(coords[0], coords[1])
time.sleep(1)
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.typewrite(['left', 'enter'])


now = datetime.datetime.now()
nowtime = datetime.datetime.strftime(now, '%c')

account_sid = 'AC1900d2845d6de1bf47fed90797644a60'
auth_token = '3f0e14a933b5acfdd42aa1aec5b2d936'
client = Client(account_sid, auth_token)

message = client.messages .create( body="DB upgraded on {}.".format(nowtime), from_='+12133772445',  to='+353874112360' )






