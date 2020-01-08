#Create Flask App
import os
import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
print(__name__)

#Decorator
@app.route('/')
def home_page():
    return render_template("./index.html")

@app.route('/<string:page_name>')
def render_page(page_name):
    print(page_name)
    return render_template(page_name + ".html")

@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("./thankyou")
        except:
            return "Something went wrong"
    else:
       return "something went wrong"

# def write_to_file(data):
#     with open("./database.txt", mode="a") as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open("./database.csv", newline="", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])