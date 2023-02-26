import requests
from bs4 import BeautifulSoup
import csv



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


page = requests.get('https://www.nba.com/stats', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

quotes = []


quote_elements = soup.find_all('table', class_='LeaderBoardPlayerCard_lbpcTable__q3iZD')

for quote_element in quote_elements:
    tag_elements = quote_element.find_all('a', class_="Anchor_anchor__cSc3P LeaderBoardPlayerCard_lbpcTableLink__MDNgL")
    tags = []
    for tag_element in tag_elements:
        tags.append(tag_element.text)

    quotes.append(
        {
            'tags': ', '.join(tags)
        }
    )


csv_file = open('quotes.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['The best scorres AT THE MOMENT, RIGHT NOW ! : '])

for quote in quotes:
    writer.writerow(quote.values())
    csv_file.close()

print(quotes[0])

# csv_file.close()

