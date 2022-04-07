import requests
from bs4 import BeautifulSoup


class GetNews(object):
	def __init__(self) -> None:
		self.url = 'https://www.tagesschau.de/'
		self.response = requests.get(self.url)
		self.unwanted = []
		self.soup = BeautifulSoup(self.response.text, 'html.parser')

	def report(self):
		headlines = self.soup.find('body').find_all('h3')
		retur = [
		    x.text.strip() for x in list(dict.fromkeys(headlines))
		    if x.text.strip() not in self.unwanted
		]

		return "".join(retur[i] + "\n\n" for i in range(5))


if __name__ == "__main__":
	news = GetNews()
	news = news.report()
	print(news)