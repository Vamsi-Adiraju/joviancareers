import os
from sqlalchemy import create_engine,text

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string,
                      connect_args={
                        "ssl" : {
                    "ssl_ca": "/etc/ssl/cert.pem"
                }
             })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  lst = result.all()
  print(type(dict(lst[0])))
  print(dict(lst[0]))

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
    