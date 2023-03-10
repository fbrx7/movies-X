import requests
from bs4 import BeautifulSoup
import lxml
from termcolor import cprint, colored
import os;os.system('cls || clear')
class Main:

	list_name = []
	list_link = []

	# cimaleak_url = 'https://cimalek.to/?s'

	def __init__(self):

		self.X = input(colored('Set Name Of Movie: ', 'light_green')).replace(' ','+')
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

				user_input = input(colored('Set Your Movie NUM: ', 'light_green'))
				print (colored('The Link: ','light_blue')+colored(Main.list_link[int(user_input)],'light_cyan')+'\r\n')

if __name__ == '__main__':


	cprint("""



 __  __            _               __   __
|  \/  |          (_)              \ \ / /
| \  / | _____   ___  ___  ___ _____\ V / 
| |\/| |/ _ \ \ / / |/ _ \/ __|______> <  
| |  | | (_) \ V /| |  __/\__ \     / . \ 
|_|  |_|\___/ \_/ |_|\___||___/    /_/ \_\


	by z3kan
	Github: https://github.com/z3kan
		""",'light_red')

	op1 = Main()
	op1.analysis_data()
	op1.user_command()