import keyboard
from youtube_dl import YoutubeDL
import os
import pyperclip

def Download(links):
	
	for link in links:
		#Setting the options for your download in this case the format of my download i.e audio
		opts={
			'format':'bestaudio'
		}
		#Changing The directory to the downloading folder
		os.chdir('F:\\songs23')
		#Downloading
		with YoutubeDL(opts) as ydl:
			ydl.download([link])
		print(f'{link} Download Complete : --------------------- >')

def check_link():
	#copying link from clipboard
	link = pyperclip.paste()
	#checking if the link is an actual youtube link
	if link.startswith('https://www.youtube.com/watch'):
		return link
	else:
		return None

def main():
	download_links = []
	while True:
		lnk = check_link()
		if lnk != None:
			if lnk not in download_links:
				download_links.append(lnk)
				print(f'Copied link {lnk}')
				print()
		elif lnk == None:
			pass
			
		try:
			if keyboard.is_pressed('d'):
				print('Downloading the songs you selected :::::::::::::::: - >')
				Download(download_links)
				#clearing all the previous download links from the list
				download_links.clear()
				print(" - : - : - : - : - : - : - : - : - : - : - : - : - : - ")
				print('clipboard cleared ----------- Scanning for new LINKS - >')

		except Exception as e:
			print(f'{e} Exception occured bro :( ')
			break

if __name__ == '__main__':
	main()












