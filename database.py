import os
from sqlalchemy import create_engine,text

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string,
                      connect_args={
                        "ssl" : {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
             })

def get_jobs_rn():
  jobs=[]
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    lst = result.all()
    for job in lst:
      jobs.append(dict(job))
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),
                         val =id)
    job = result.all()
    if len(job) == 0:
      return None
    else:
      return dict(job[0])

def enter_job_to_db(data,id):
  with engine.connect() as conn:
    querrr = "INSERT into jobresponses(job_id,full_name,age,email) VALUES(:job_id,:full_name,:age,:email)"
    query = text(querrr)
    conn.execute(query,job_id=id,full_name=data['name'],age=
                 data['age'],email=data['email'])
    