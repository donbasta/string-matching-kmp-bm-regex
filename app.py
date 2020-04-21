from flask import Flask, render_template, request, redirect
from extractor import convert, extractor

app = Flask(__name__)
keyword = None
uploaded_files = set()
news = []

@app.route('/')
def index():

	global keyword
	global uploaded_files

	return render_template("index.html", keyword=keyword, files=uploaded_files)


@app.route('/set_keyword', methods=['GET','POST'])
def set_keyword():

	global keyword

	if request.method == 'POST':
		keyword = request.form['keyword']
		return redirect('/')
	else:
		return render_template("index.html", keyword=keyword)


@app.route('/uploader', methods=['GET','POST'])
def uploader():

	global uploaded_files

	if request.method == 'POST':
		f = request.files['file']
		uploaded_files.add(f.filename)
		news.append([f.filename, convert(f.read().decode())])
		return redirect('/')
	else:
		return render_template("index.html", files=uploaded_files)


@app.route('/extract')
def extract():

	informations = []

	for sentences in news:
		informations += extractor(keyword, sentences[1])
	
	return render_template("index.html", informations=informations)

	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)