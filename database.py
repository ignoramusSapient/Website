from sqlalchemy import create_engine, text
import os

connection_variable = os.environ['POEM_DB_CONNECTION_STRING']

engine = create_engine(connection_variable,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_poems():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM POEMS"))

    p_poems = []
    for row in result.all():
      p_poems.append(row._asdict())
    return p_poems


def poem_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f'SELECT * FROM POEMS WHERE id ={id}'))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_feedback_to_db(id, feed):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO feedback (id, full_name, email, comments) VALUES (:id, :full_name, :email, :comments);"
    )

    conn.execute(
      query, {
        'id': id,
        'full_name': feed['full_name'],
        'email': feed['email'],
        'comments': feed['comments']
      })
