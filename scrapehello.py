
#scrapehello.py

from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

#show the HTML document structure, not useful for large documents
print(soup.prettify())



# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')


print('list items:', all_list_items)
print('------')
print('divs:', all_divs)
print('------')
print('goodbye elements:', all_goodbye_elements)
print('------')
print('french stuff:', all_french_list_items)
print('------')
print('hello id elements:', all_hello_elements)
print('------')


print(type(all_list_items[0]))
print('------')


for li in all_list_items:
  print(li.string)
print('------')


for child in all_hello_elements[0].children:
  print(child.string)
print('------')


print('List items within the hello tag')
hello_list_items = all_hello_elements[0].find_all('li')
print (hello_list_items)
print('------')

#if you know what you're looking for, don't use findall()
all_hello_elements = soup.find_all(id='hello-list')
print(all_hello_elements[0])
print('------')

#instead find it directly by id
the_hello_element = soup.find(id='hello-list')
print(the_hello_element)
print('------')


img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('------')

#1. Push to Github
#2. Elements of Goodbye List
all_gb_elements = soup.find_all(id='goodbye-list')
print('List items within the goodbye tag')
gb_list_items = all_gb_elements[0].find_all('li')
for li in gb_list_items:
  print(li.string)
print('------')

#3. Get width of IMG
img_tag = soup.find_all('img')
for img in img_tag:
  print("Image Width: " + img['width'])

#4. Get the href of a tag
a_tag = soup.find_all('a')
for a in a_tag:
  print("href source: " + a['href'])
