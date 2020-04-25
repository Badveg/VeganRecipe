import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query=' + '비건레시피'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

for i in range(0,11):
    recipes = soup.select('#sp_blog_' + str(i))
    print('#sp_blog_' + str(i))

    for recipe in recipes:
        title = recipe.select_one('dl > dt > a')['title']
        image = recipe.select_one('div > a.sp_thmb.thmb80 > img')['src']
        url = recipe.select_one('dl > dd.txt_block > span > a.url')['href']

        recipe_posts = [{'title': title, 'image': image, 'url': url}]