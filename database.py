from sqlalchemy import create_engine, text
import os

connection_variable=os.environ['POEM_DB_CONNECTION_STRING']

engine = create_engine(connection_variable,
connect_args={
  "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
  }
            }                     
)


