import requests
from bs4 import BeautifulSoup


class getnews(object):
	def __init__(self) -> None:
		self.url = 'https://www.tagesschau.de/'
		self.response = requests.get(self.url)

		self.soup = BeautifulSoup(self.response.text, 'html.parser')

	def report(self):
		text = []
		headlines = self.soup.find('body').find_all('h3')
		for x in list(dict.fromkeys(headlines)):
			if x.text.strip() not in self.unwanted:
				text.append(x.text.strip())

		return text


if __name__ == "__main__":
	news = getnews()
	news = news.report()
	for i in range(10):
		print(news[i])