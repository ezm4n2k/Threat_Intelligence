# from translate import *
from flask import Flask, jsonify
from get_content import get_all_content
from check_news import check_news

app = Flask(__name__)

@app.route('/get_articles', methods=['GET'])
def get_articles():
    new_article = check_news()
    for article in new_article:
        href = article['href']
        raw_result = get_all_content(href)
        article['raw_content'] = raw_result
        article['translate_content'] = None
    return jsonify(new_article)

if __name__ == '__main__':
    app.run(debug=True)
