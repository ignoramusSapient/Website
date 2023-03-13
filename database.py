from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://gvm39gm6m3vnpb1ryhqk:pscale_pw_VnBv5WNNccF3UN2sME8zu3N0HiCswYjETOyaRO2MEZe@ap-south.connect.psdb.cloud/ap-south.connect.psdb.cloud?charset=utf8mb4"


engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from poems"))
print(result.all())
