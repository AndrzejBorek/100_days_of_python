# from bs4 import BeautifulSoup
# import requests
#
# url = "https://news.ycombinator.com/"
#
# response = requests.get(url=url)
#
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")

# links = {tag.find(name='a').text: tag.find(name='a')['href'] for tag in soup.find_all(class_='titleline')}
#
# for link in links.items():
#     print(link)
#
#


#
# article_links = [tag.find(name='a').get('href') for tag in soup.find_all(class_='titleline')]
#
# for link in article_links:
#     print(link)
#
# article_upvotes = [tag.find(name='span').getText() for tag in soup.find_all(class_='score')]
#
# for vote in article_upvotes:
#     print(vote)
#
# for tag in soup.find_all(name='span' ,class_='score'):
#     print(tag)
#
# print(soup.find(name='span', class_='score').getText)
#
#

#
# article_data = {tag.get('id'): {
#     'title': tag.find(class_='titleline').getText(),
#     'link': tag.find(class_='titleline').find(name='a').get('href'),
#     # 'score': soup.find(class_='score', id=f"score_{tag.get('id')}").getText()
# }
#     for tag in soup.find_all(class_='athing')}
#
# for article in article_data:
#     try:
#         article_data[f'{article}']['score'] = soup.find(class_='score', id=f'score_{article}').getText()
#     except AttributeError:
#         article_data[f'{article}']['score'] = '0'

# for article in article_data.items():
#     print(article)
