from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    """Using some quick things until I build the databases"""
    user = {'username': 'Edgecase'}    
    teamnames = [{'teamname':'edgecase'}, {'teamname':'angerpacket'}]

    return render_template('index.html',teamnames=teamnames,title="Flag Submissions", user=user)

@app.route('/scoreboard')
def scoreboard():
    user = {'username':'Miguel'}
    teamnames = [{'teamname':'edgecase'}, {'teamname':'angerpacket'}]

    return render_template('scoreboard.html', teamnames=teamnames, title="Flag Submissions", user=user)

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')

@app.route('/statistics')
def stats():
    return render_template('statistics.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect ('/index')
    return render_template('login.html', form=form)

@app.route('/signup')
def signup_page():
    return "Still coming"

