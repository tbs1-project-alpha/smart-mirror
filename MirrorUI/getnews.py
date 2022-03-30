import requests
from bs4 import BeautifulSoup


class getnews(object):
	def __init__(self) -> None:
		self.url = 'https://www.tagesschau.de/'
		self.response = requests.get(self.url)
		self.unwanted = []
		self.soup = BeautifulSoup(self.response.text, 'html.parser')

	def report(self):
		headlines = self.soup.find('body').find_all('h3')
		return [
		    x.text.strip() for x in list(dict.fromkeys(headlines))
		    if x.text.strip() not in self.unwanted
		]


# if __name__ == "__main__":
# 	news = getnews()
# 	news = news.report()
# 	for i in range(10):
# 		print(news[i])