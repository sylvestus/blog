from flask import render_template, request,redirect,url_for,abort
from . import main
from .forms import CommentForm,BlogForm,SubscriberForm
from ..models import Blogs, Comments,User,Subscriber
from flask_login import login_required,current_user
from .. import db
from wtforms import form
from ..email import mail_message
from ..requests import get_quote

# As a user, I would like to view the blog posts on the site
# As a user, I would like to comment on blog posts
# As a user, I would like to view the most recent posts
# As a user, I would like to an email alert when a new post is made by joining a subscription.
# As a user, I would like to see random quotes on the site
# As a writer, I would like to sign in to the blog.
# As a writer, I would also like to create a blog from the application.
# As a writer, I would like to delete comments that I find insulting or degrading.
# As a writer, I would like to update or delete blogs I have created.

@main.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    title = 'hello and welcome to our blog site'
    quote = get_quote()
    
    return render_template('index.html', main_title=title,quote=quote)

@main.route('/blogs')
@login_required
def blogs():
    """
    view blogs function that returns blogs
    """
    title = "silvano blogs"
    blogs = Blogs.get_blogs()
    # user_d=User.query.filter_by(id=id).first()
    user=User.username

    # Blogs.query.filter_by(id=id).first()
    # .
   
    return render_template('blogs.html', title=title,myblogs=blogs,user=user)

@main.route('/new_blogs',methods=['GET','POST'])
@login_required
def new_blogs():
    """
    view new_blogs function that lets us create blogs
    """  
    title ='blogs form'
    form= BlogForm()

    if form.validate_on_submit():
        blog = form.blog.data
        title= form.title.data

        new_blog = Blogs(blog=blog,title=title,user_id=current_user.id)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.blogs'))
    return render_template('new_blog.html',blog_form=form)

@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteBlog(id):
    blog = Blogs.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.blogs'))


@main.route('/comments/<int:id>',methods=['GET','POST'])
@login_required
def comment(id):
    """
     comment function that returns comment details
    """
    title="This blog's comments"
    blog=Blogs.get_blogs()
    # blog_id= blog.id
    
    comments=Comments.get_comments(id)
    
    return render_template('comments.html',blog_comments=comments,title=title)


@main.route('/new_comment/<int:blogs_id>', methods = ['GET', 'POST'])
@login_required
def new_comment( blogs_id):
    
    blogs = Blogs.query.filter_by(id = blogs_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.user_comment.data
        new_comment = Comments(comment=comment,user_id=current_user.id, blogs_id=blogs_id)
        new_comment.save_comment()

        return redirect(url_for('main.comment',id = blogs_id))
    title='New Blog'
    return render_template('new_comment.html',title=title,comment_form = form,blogs_id=blogs_id)

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comments.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect (url_for('main.comment',id=id))

@main.route('/Subscribe',methods=['GET','POST'])
def subscribe():
    
    form = SubscriberForm()
    if form.validate_on_submit():
        subs = Subscriber(email = form.email.data, username = form.username.data)    
        db.session.add(subs)
        db.session.commit()


        mail_message("You have successfully subscribed to Blog website,Thank for joining us", "email/welcome_subs", subs.email,subs=subs)
    
    return render_template('subscribe.html',subscribe_form=form)




