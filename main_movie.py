import requests
from bs4 import BeautifulSoup
import lxml
from termcolor import cprint, colored

class Main:


	# cimaleak_url = 'https://cimalek.to/?s'

	def __init__(self):

		self.X = input(colored('Set Name Of Movie: ', 'green')).replace(' ','+')

		self.request = requests.get(f'https://cimalek.to/?s={self.X}')

		self.soup = BeautifulSoup(self.request.content, 'lxml')

		self.data = self.soup.find_all('div', {'class':'item'})
	
		self.list = []

	def analysis_data(self):

		for i in range(len(self.data)):

			self.title_movie = self.data[i].find('div', {'class':'title'}).text.strip()
			self.list.append(self.title_movie)

			print ('['+colored(i,'red')+']'+colored(self.title_movie,'magenta'))

Main().analysis_data()




