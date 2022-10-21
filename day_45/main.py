from bs4 import BeautifulSoup

# import lxml

with open('website.html') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
# print(soup.prettify())

# print(soup.li)  # finds first <li> from html
# print(soup.find_all("li"))  # finds all <li>
# print(soup.find_all("a"))
#
# for tag in soup.find_all(name='a'):
#     print(tag.getText())

# print(soup.a['href']) # getting link from <a> tag

# for tag in soup.find_all(name='a'):
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading)
# print(heading.text)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# company_url = soup.select_one(selector='p a')  # way of getting something using css selectors
# print(company_url)

# name = soup.select_one(selector='#name')  # way of getting something using id of that element
# print(name)

# books_and_teaching = soup.select_one(selector='.heading')  # way of getting something using class of that element
# print(books_and_teaching)
