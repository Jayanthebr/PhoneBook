from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/phonebooklist.html")
# def phonebooklist():
#     with open('details.txt',"r") as f:
#         phonebooklist=f.readlines()
    
#     return render_template("phonebooklist.html",phonelist=phonebooklist)

@app.route("/data", methods=["POST"])
def data():
    submitform = request.form.get('data')
    print(submitform, file=sys.stderr)
    if submitform == 'delete':
        return render_template('delete.html')
    elif submitform == 'search':
        return render_template('search.html')
    elif submitform == 'add':
        return render_template('add.html')
    else:
        with open('details.txt',"r") as f:
            phonebooklist=f.readlines()
        return render_template('phonebooklist.html',phonelist=phonebooklist)
    


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get('name')
    phone = request.form.get('phone')
    with open('details.txt', "a") as react:
        react.write(name + ":" + str(phone) + "\n")
        return "added to file"


@app.route("/search", methods=["POST"])
def search():
    search_name = request.form.get('search')
    with open('details.txt', "r") as file_search:
        search = file_search.readlines()
        for i in search:
            if search_name in i:
                x = i.split(":")
                searchnames = {}
                searchnames['name'] = x[0]
                searchnames['phone'] = x[1]
                return (searchnames['phone'])

@app.route("/delete",methods=["POST"])
def delete():
    delete_name=request.form.get('delete')
    with open("details.txt","r") as phone_list:
        delete=phone_list.readlines()
    
    with open("details.txt","w") as phone_list:

        for i in delete:
            if delete_name not in i:
                phone_list.write(i)
                return("Deleted")
    
    return("Not Found")
