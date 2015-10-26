# Start with relevant imports
from flask import Flask,request,json,jsonify,\
	abort,url_for,render_template,redirect
import uuid,json,os
from flask.ext.sqlalchemy import SQLAlchemy
from id_generator import *
# initialize flask app
app = Flask(__name__)
# link to local sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = \
'sqlite:////tmp/database.db'
# initialize Database
db = SQLAlchemy(app)



class Data(db.Model):
	__tablename__='learned'
	identifier = db.Column(db.Integer(),primary_key=True)
	asked = db.Column(db.String(125))
	has_asked = db.Column(db.Boolean())
	learned = db.Column(db.String(250))
	has_learned = db.Column(db.Boolean())
	upvotes = db.Column(db.Integer())

	def __init__(self,asked,learned):
		self.identifier = id_counter.next()
		self.asked = asked
		self.has_asked = asked != ''
		self.learned = learned
		self.has_learned = learned != ''
		self.upvotes = 0

	def __repr__():
		return "Entry %d: asked = %s, learned = %s"


db.create_all()
db.session.commit()

@app.route('/') # home page
def index():
  return render_template('index.html')

@app.route('/thankyou')
def thank_you():
	asked,learned = request.form['Asked'],request.form['Learned']
	new_entry = Data(asked,learned)
	return str(new_entry)



if __name__=='__main__':
  app.run(debug=True)
