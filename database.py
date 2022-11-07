from sqlalchemy import create_engine,text

connection_string = "mysql+pymysql://38ihl6dge12q5jcrmvl9:pscale_pw_YCFL4WJrScTxhXsqkp0en8xrbfNgW3ZXet7Uzp8Kmps@ap-south.connect.psdb.cloud/joviancareers?charset=utf8mb4"
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