from flask import Flask 
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

# Index Page 
# 示範 rander 一個 HTML 頁面
# 示範 Jinja2 Template
@app.route('/')
def index():
	urls = [
		'user/Franklin',
		'api/books',
		'api/books?bid=3',
		'api/books?bid=4'
	]
	return render_template('index.html',urls=urls)


# Get User Name 
# 示範 rander 一個 HTML 頁面
# 示範 routing + 取得 route
@app.route('/user/<name>')
def user(name='Noname'):
	return render_template('user.html',name=name)

# 假資料
books = [
	{'bid':'1', 'name':'Harry Potter and the Sorcerer'},
	{'bid':'2', 'name':'The Selection Series Box Set'},
	{'bid':'3', 'name':'The Official Guide for Gmat Verbal Review'}
]

# Get one of books
# 示範 rander json
# 示範取得 url query string
@app.route('/api/books')
def getbook():
	bid = request.args.get('bid',None)
	return jsonify(books) if bid is None else jsonify(next((book for book in books if book['bid']==bid),{'msg':'book is not found'}))
app.run()