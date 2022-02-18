from flask import Flask,render_template

app = Flask(__name__)
posts =[
    {
       "firstname": "lewis",
        "surname": "mwirigi",
        "lastname": " mutembei",
        "age": "20",
        "gender": 'male',
        "dateofbirth": "18th November 2000"

    }
]


@app.route('/')
def hello_world():
    return '<h1>Hello World! </h1>'
# render template is used to return an html or any static page
@app.route("/homepage")
def homepage():
    return render_template("index.html",posts=posts)
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route('/loginpage')
def loginpage():
    return render_template("base.html")


# this is compulsory condition however if the module its imported on a different module then the name value changes depending on the module name

if __name__ == '__main__':
    app.run(debug="true")
