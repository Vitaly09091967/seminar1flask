from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/category/clothing')
def clothing():
    return render_template('category.html', category_name='Одежда')

@app.route('/category/shoes')
def shoes():
    return render_template('category.html', category_name='Обувь')

@app.route('/category/jacket')
def jacket():
    return render_template('category.html', category_name='Куртка')

if __name__ == '__main__':
    app.run(debug=True)
