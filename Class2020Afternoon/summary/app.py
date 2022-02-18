from flask import Flask, render_template


app = Flask(__name__)
# variable rules
# you can add variable sections to a url by marking sections
# with <variable_name>. Your function then receives the < variable_name>
# as the keyword argument. optionally, you can use the a convertor to specify the type of argument like <converter: variable_name>
# http://127.0.0.1:5000
@app.route('/')
def index():
    greetings = "Heeey welcome to my website "
    list =["pearls",'orange',"banana"]
    age ={'john':23,'mary':21,'paul':30}
    return render_template('index.html',salamu = greetings ,orotha = list , miaka= age)

# http;//127.0.0.1:5000/about


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login')
def login():
    return render_template("login.html")



@app.route('/signup')
def signup():
    return render_template("signup.html")
@app.route('/<virus>')
def get_covid19(virus):
    print("VIRUS NOT FOUND : {}".format(virus))
    return  virus
@app.route('/covidcases/<int:cases>')
def get_c0vid_cases(cases):
    print("CASES FOUND : {}".format(cases))
    return cases

# error handling
@app.errorhandler(404)
def page_not_found(e):

    return "ERROR {} ".format(e),404
@app.errorhandler(500)
def internal_server_error(e):
    return "ERROR:500 {} ".format(e),500


if __name__ == '__main__':
    app.run(debug=True)
# command to see what has been installed in the virtual environment
# pip list

