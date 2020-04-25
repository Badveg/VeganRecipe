from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recipe', methods=['GET', 'POST'])
def add_menu():
    main = str(request.args.get('main_give').replace(',', '+'))
    # ',' -> '+'

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query='+ '비건' + '+' + main + '+' + '레시피'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    recipe_posts = []
    for num in range(0,11):
        recipes = soup.select('#sp_blog_' + str(num))


        for recipe in recipes:

            title = recipe.select_one('dl > dt > a')['title']
            # image = recipe.select_one('div > a.sp_thmb.thmb80 > img')['src']
            url = recipe.select_one('dl > dd.txt_block > span > a.url')['href']
            # print(image)

            recipe_posts.append({'title': title, 'url': url})

    return jsonify(recipe_posts)


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)