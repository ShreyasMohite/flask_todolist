from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']="4UIFJEKNDYG3HBEJND"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/newdata'

db=SQLAlchemy(app)


class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

    def __init__(self,name):
        self.name=name



@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['getname']
        mydata=Task(name)
        db.session.add(mydata)
        db.session.commit()
        return redirect(url_for('home'))
    if request.method=='GET':
        user=Task.query.all()
    return render_template("home.html",title="Home",user=user)


@app.route("/delete/<int:id>",methods=['GET','POST'])
def delete(id):
    user=Task.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)