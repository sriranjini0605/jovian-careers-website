from flask import Flask, render_template,jsonify

app = Flask(__name__)

Jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
{
  'id':1,
  'title':'Data Scientist',
  'location':'Cupertino, California',
  'salary':'$1100,000'
},
{
  'id':1,
  'title':'Data Engineer',
  'location':'Houston, Texas ',
  'salary':'$1000,000'
},
{
  'id': 1,
  'title':'Software Developer',
  'location':'Mumabai, India',
  'salary':'Rs. 15,00,000'
},
{
  'id': 1,
  'title':'Software Developer Intern',
  'location':'Brooklyn, New York',
  'salary':'$45/hr'
},
  {
    'id': 1,
    'title':'Front End Engineer',
    'location':'Remote'
  }
  
]

@app.route("/")
def hello_jovian():
  return render_template('home.html',jobs=Jobs,company_name='Jovian')

@app.route("/")
def list_jobs():
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
