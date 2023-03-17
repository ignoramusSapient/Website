from flask import Flask, render_template, jsonify
from database import engine, text

app=Flask(__name__,template_folder='templates')
def load_poems():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM POEMS"))
    
    p_poems=[]
    for row in result.all():
      p_poems.append(row._asdict())
  return p_poems
  
@app.route("/")
def hello_func():
  df_poems=load_poems()
  return render_template('home.html', 
                         poems=df_poems)

@app.route('/api/poems')
def full_poems():
  df_poems=load_poems()
  return jsonify(df_poems)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)