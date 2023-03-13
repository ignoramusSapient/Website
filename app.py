from flask import Flask, render_template, jsonify

app=Flask(__name__)

Poems = [
    {
          'Title': 'Chanchal Mann',
          'Genre': 'Life'
    },
 {
          'Title': 'Bachpan Bahut Sunder',
          'Genre': 'Childhood'
    },
   {
          'Title': 'Shaam Badalon Se',
          'Genre': 'Nature'
    },
]

@app.route('/')
def home_func():
  return render_template('home.html', poems=Poems)

@app.route('/api/poems')
def full_poems():
  return jsonify(Poems)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)