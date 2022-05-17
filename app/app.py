import time
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/liveness')
def healthx():
  return "<h1><center>Liveness check completed</center><h1>"
  
@app.route('/readiness')
def healthz():
  return "<h1><center>Readiness check completed</center><h1>"

if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5000)
