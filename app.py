from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')
if __name__ == '__main__':
    app.run()
