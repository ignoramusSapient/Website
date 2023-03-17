from flask import Flask, render_template, jsonify
from database import engine, text, load_poems, poem_db

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


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)