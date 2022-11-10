from flask import Flask, render_template, jsonify,request
from database import get_jobs_rn,load_job_from_db
app = Flask(__name__)


@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=get_jobs_rn(), 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(get_jobs_rn())

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found",404
  return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply")
def apply_job(id):
  data = request.args
  
  return jsonify(data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)