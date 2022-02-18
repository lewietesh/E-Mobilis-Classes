from flask import Flask,render_template,jsonify,request
# I imported the request mthod to enable me read the query string 

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])

def index():
    return "<h1> Hello world !</>"
# This return the home page including the name parameter passed i.e 'name' we can also assign a datatype to the variable being passed to the url
# example of the route below together with its variable and data type @app.route('/home/<int:15>', methods = ['get],'post')
@app.route('/home/<string:name>/<int:age>', methods=['GET','POST'],)

def home(name,age):

    return "<h2>Hello {} you are on the homepage and you are {} years old </>".format(name,age)

@app.route('/jsonif', methods =['GET','POST'])
def jsonif():
    # the jsonify function returns data in json format 
    return jsonify({'myname': "lewis", "units": ['java', 'c++','python']})

# how to pass in data using a query string
@app.route('/query', methods=['GET','POST'])
def query_string():
    # the request.args.get() method takes in the variable and passes it on 
    jina = request.args.get('jina')
    location = request.args.get('location')
    return "<h1> Hi {} you are from {} and You are on the query page </h1>".format(jina,location)

# sending and retrieving the form data
@app.route('/theform',methods=["GET",'POST'])
def theform():
    return ''' <form method="POST" action= "/process">
                <input type= "text" name ="jina">
                <input type="text" name = "location">
                <input type= "submit">
                </form>'''
@app.route("/process",methods=["POST"])
def process():
    jina = request.form['jina']
    location = request.form['location']
    return "<h3> Hello {} you are from {} and thank you for submitting the requested data".format(jina,location)
# request json data
@app.route('/processjson',methods=['POST'])
def processjson():
    # taking in data from json format to python format using the API 
    
    info = request.get_json()
    name = info['name']
    location =info['location']
    randomlist = info['randomlist']
    return jsonify({ "results": 'success', 'jina':name,'location':location,"randomkeyinlist":randomlist[1]})

if __name__ == "__main__":
    app.run(debug = True)