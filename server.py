from flask import Flask, render_template, request, redirect
import datetime


app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    
    apple_count = int(request.form['apple'])
    blackberry_count = int(request.form['blackberry'])
    raspberry_count = int(request.form['raspberry'])
    strawberry_count = int(request.form['strawberry'])
    total = int(apple_count) + int(blackberry_count) + int(raspberry_count) + int(strawberry_count)
    print(f"THe value of apple = {apple_count}\
        \nThe value of Blackberry = {blackberry_count}\
        \nThe value of raspberry = {raspberry_count}\
        \nThe value of strawberry = {strawberry_count}\
        \n The Total value = {total}")
    firstname=request.form['first_name']
    lastname=request.form['last_name']
    studentid=request.form['student_id']
    if studentid == "":
        studentid="N/A"
    date = datetime.datetime.now()


    return render_template("checkout.html" 
                            ,apple_checkout = int(apple_count)
                            ,blackberry_checkout = int(blackberry_count)
                            ,raspberry_checkout = int(raspberry_count)
                            ,strawberry_checkout = int(strawberry_count) 
                            ,firstname_checkout = firstname
                            ,lastname_checkout = lastname
                            ,studentid_checkout = studentid
                            ,total_checkout = total
                            ,date_checkout = date.strftime('%c') )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    