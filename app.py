from flask import Flask, render_template, jsonify
from database import get_jobs_rn
app = Flask(__name__)


@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=get_jobs_rn(), 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(get_jobs_rn())

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)