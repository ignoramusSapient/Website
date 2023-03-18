from flask import Flask, render_template, jsonify, request
from database import engine, text, load_poems, poem_db, add_feedback_to_db

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_func():
  df_poems = load_poems()
  return render_template('home.html', poems=df_poems)


@app.route('/api/poems')
def full_poems():
  df_poems = load_poems()
  return jsonify(df_poems)


@app.route('/poems/<id>')
def id_poem(id):
  poem = poem_db(id)
  if not poem:
    return 'Not Found', 404
  return render_template('pageforeachpoem.html', poem=poem)

@app.route("/api/poems/<id>")
def poems_json(id):
  poem = poem_db(id)
  return jsonify(poem)

@app.route('/poems/<id>/submit', methods=['post'])
def feedback_to_poem(id):
  data = request.form
  poem = poem_db(id)
  add_feedback_to_db(id, data)
  return render_template('feedbacksubmitted.html', 
                         feedback=data)
  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)