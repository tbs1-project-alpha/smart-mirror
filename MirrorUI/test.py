import feedparser

NewsFeed = feedparser.parse("https://www.tagesschau.de/xml/rss2/")

print('Number of RSS posts :', len(NewsFeed.entries))

entries = NewsFeed.entries

entry_list = []

for (index) in range(0, round(len(entries)), 5):
    site_entries = entries[index:index+5]
    entry_list.append(site_entries)

    print(f"-------------[ Seite: {index} ]-------------")
    for entry in site_entries:
        print(entry.title)
