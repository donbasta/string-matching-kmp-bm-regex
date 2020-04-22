from flask import Flask, render_template, request, redirect
from extractor import convert, extractor

app = Flask(__name__)
keyword = None
uploaded_files = []
news = []
option = None

@app.route('/')
def index():

	global keyword
	global uploaded_files
	global option

	return render_template("index.html", keyword=keyword, files=uploaded_files, algorithm=option)


@app.route('/set_keyword', methods=['GET','POST'])
def set_keyword():

	global keyword

	if request.method == 'POST':
		keyword = request.form['keyword'].lower()
		return redirect('/')
	else:
		return render_template("index.html", keyword=keyword)


@app.route('/picker', methods=['GET','POST'])
def picker():

	global option

	if request.method == "POST":
		option = request.form['options']
		print(option)
		return redirect('/')
	else:
		return render_template("index.html", algorithm=option)


@app.route('/uploader', methods=['GET','POST'])
def uploader():

	global uploaded_files

	if request.method == 'POST':
		f = request.files['file']
		if f.filename not in uploaded_files:
			uploaded_files.append(f.filename)
			news.append([f.filename, convert(f.read().decode())])
		return redirect('/')
	else:
		return render_template("index.html", files=uploaded_files)


@app.route('/extract')
def extract():

	global option
	global uploaded_files

	if len(uploaded_files) < 1:
		return "Choose some files first"

	if option is None:
		return "Pick the option first"

	informations = []

	for sentences in news:
		informations += extractor(keyword, sentences, option)
	
	return render_template("index.html", informations=informations, query=keyword)

if __name__ == "__main__":
	app.run(debug=True)