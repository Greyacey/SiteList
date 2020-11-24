from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bf2a0fbecd7030220d754389dcbd5ij9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ipnx:root.Account#20@ipNX@localhost/ipnx_db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    
class matrix(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    contact= db.Column(db.String(100), nullable=False)
    timeline = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return "id: {0} | level: {1} | timeline: {2} | contact_name: {3} | email: {4} | contact: {5} | name: {6}".format(self.id, self.level, self.timeline, self.email, self.contact, self.name) 



@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    qry = matrix.query.order_by(matrix.id.desc())
    
    if request.method == 'POST':
        data = request.form
        level = data['level']
        timeline = data['timeline']
        name = data['name']
        contact_name = data['contact_name']
        email = data['email']
        contact= data['contact']
        user = matrix(level=level, name=name, timeline=timeline, contact_name=contact_name, email=email, contact=contact)
        db.session.add(user)
        db.session.commit()
        flash('Matrix added Successfully')
    return render_template('index.html', result=qry, title=index)
 
@app.route('/mtn_matrix', methods=['GET', 'POST'])
def mtn_matrix():
    if request.method == 'POST':
        data = request.form
        name = data['query']
        qry = matrix.query.filter_by(name=name)
    return render_template('index.html', result=qry, title=index, exit=exit)











if __name__ =='__main__':
	app.run(debug=True)