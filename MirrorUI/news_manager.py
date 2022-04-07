import feedparser

class NewsManager():
    def __init__(self):
        self.url = "https://www.tagesschau.de/xml/rss2/"
        self.articles_per_page = 5
        self.current_feed = self.parse_feed()
        self.current_page = -1
        
    
    def parse_feed(self):
        NewsFeed = feedparser.parse(self.url)
        entries = NewsFeed.entries
        entry_list = []

        for (index) in range(0, round(len(entries)), self.articles_per_page):
            site_entries = entries[index:index + self.articles_per_page]
            entry_list.append(site_entries)

        return entry_list

    def next_page(self):
        page = self.current_feed[self.current_page]
        self.current_page += 1

        if self.current_page > len(self.current_feed) - 1:
            self.current_page = 0

        return page

    def parse_page(self, content):
        page_headings = ""
        for entry in content:
            page_headings += entry['title'] + "\n\n"

        page_headings += f"\n\n Seite: {self.current_page + 1} / {len(self.current_feed)}"

        return page_headings
