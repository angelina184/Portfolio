from flask import Flask, render_template,request
from forms import SignupForm

#initialization of flask app -> creates aplication
app = Flask(__name__)
#secret key for configuring the flask app 
# flask-wtf for creation and validation
app.config['SECRET_KEY']='codexword'
#rout on our server. What will be after localhost
# here we specify the pass where server should go and what should return
@app.route('/')
#what we wanna show
def home():
    return 'Hello World'
@app.route('/about')
def about():
    return 'The Abaut Page'
@app.route('/blog')
#render the html code
def blog():
    posts = [{'title': 'Tech IT', 'author':'Me'},
            {'title': 'Programing', 'author':'Him'}]
    return render_template('blog.html',author = "Anhel", sunny = True, posts=posts)
# specifi a rule inside route
#add variable to url
@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignupForm()
    #what to do
    if form.is_submitted():
        result = request.form
        return render_template('/user.html',result = result)
    return render_template('signup.html',form=form)
if __name__ == '__main__':
    app.run()