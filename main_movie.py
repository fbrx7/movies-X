import requests
from bs4 import BeautifulSoup
import lxml
from termcolor import cprint, colored

class Main:

	list_name = []
	list_link = []

	# cimaleak_url = 'https://cimalek.to/?s'

	def __init__(self):
		self.X = input(colored('Set Name Of Movie: ', 'green')).replace(' ','+')
		self.request = requests.get(f'https://cimalek.to/?s={self.X}')
		self.soup = BeautifulSoup(self.request.content, 'lxml')
		self.data = self.soup.find_all('div', {'class':'item'})

	def analysis_data(self):
		for i in range(len(self.data)):
			self.title_movie = self.data[i].find('div', {'class':'title'}).text.strip()
			for link in self.data[i].find_all('a'):
				self.href = link.attrs['href']
			Main.list_name.append(self.title_movie)
			Main.list_link.append(self.href)
			print ('['+colored(i,'red')+']'+colored(self.title_movie,'magenta'))


	@classmethod
	def user_command(cls):
		if Main.list_name != 0:
				user_input = input(colored('Set Your Movie NUM: ', 'green'))
				print (colored('The Link: ','light_blue')+colored(Main.list_link[int(user_input)],'light_cyan'))

if __name__ == '__main__':

	op1 = Main()
	op1.analysis_data()
	op1.user_command()