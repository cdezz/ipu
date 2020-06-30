from ftplib import FTP 

print('Logging into IPU Website...')

ftp = FTP('ftp.ipu.ie', user='gibb902434', passwd='g90i24b34b')
ftp.login(user='gibb902434', passwd='g90i24b34b')

# IPU product file
ftp.nlst()[1]

print('Downloading IPU product file...')

with open(f"{ftp.nlst()[1]}.exe", 'wb') as product_file:
	ftp.retrbinary(f"RETR {ftp.nlst()[1]}", product_file.write)

print('Download Complete.')
