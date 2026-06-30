from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json
import math
import os
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True 


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config ['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL =True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_pass']
)
mail = Mail(app)


if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']

else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    phone_num = db.Column(db.String(12))
    msg = db.Column(db.String(180), nullable =False)
    date = db.Column(db.String(12))
    email = db.Column(db.String(30))

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    slug = db.Column(db.String(30), nullable =False)
    content = db.Column(db.String(180), nullable =False)
    tagline = db.Column(db.String(180), nullable =False)
    date = db.Column(db.String(12))
    img_file = db.Column(db.String(12))
    
    
    # http://localhost/phpmyadmin/ 
    
@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    # [0:params['no_of_post']]
    last = math.ceil(len(posts) / int(params['no_of_post']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
        
        # this slicing is for how many post we want to display by default
    posts = posts[(page-1)*int(params['no_of_post']): (page-1)*int(params['no_of_post'])+int(params['no_of_post'])]
    
    if page == 1:
        prev = '#'
        next = "/?page="+ str(page+1)
        
    elif page == last:
        prev = "/?page="+ str(page-1)
        next = '#'
        
    else:
        prev = "/?page="+ str(page-1)
        next = "/?page="+ str(page+1)
    
    return render_template('index.html', params=params, posts = posts, prev=prev, next=next)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html',params=params, post = post)


@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts = posts)
        
    if request.method=='POST':
        username = request.form.get('uname')
        user_pass = request.form.get('pass')
        if username == params['admin_user'] and user_pass == params['admin_pass']:
            # set the session variables
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html',params=params, posts = posts)
        
    return render_template('login.html',params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        
        if request.method == 'POST':
            title = request.form.get('title') 
            tagline = request.form.get('tagline') 
            slug =  request.form.get('slug') 
            content = request.form.get('content') 
            img_file = request.form.get('img_file') 
            date= datetime.now()
            
            if sno == '0':
                post = Posts(title=title, tagline =tagline, slug=slug, content=content,img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/dashboard')
                
            else:
                post= Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.tagline = tagline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/'+ sno)
            
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)
    
    return redirect('/dashboard')

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "Uploaded Sucessfully"
        
@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/dashboard')
    
    
@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method=='POST':
        
        '''Add Entry to Database'''
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        phone = request.form.get('phone')
        entry = Contacts(name = name, phone_num = phone, msg = message, date= datetime.now(), email = email)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('New message from Blog from ' + name, 
        #                 sender=email,
        #                 recipients = [params['gmail_user']],
        #                 body= message + "\n" + phone)
        # flash("Your message has been sent!", "success")
        # return redirect(url_for('contact'))  
        flash("Thanks For Submitting Your Details", "success")
    return render_template('contact.html',params=params)
    
if __name__ =="__main__":
    app.run(debug=True)