from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('input_data')
    return render_template('result.html', result=data)

if __name__ == '__main__':
    app.run(debug=True)
