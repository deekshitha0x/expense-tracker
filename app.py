from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []


@app.route('/', methods= ['GET','POST'])
def home(): 
    if request.method == 'POST':

        title= request.form["title"]
        amount= float(request.form["amount"])
        category= request.form["category"]

        # Validation
        if amount <= 0:
            return redirect('/')


        expense= {"title": title, 
                  "amount": amount, 
                  "category": category}
        
        expenses.append(expense)

        
    total=0
    total= sum(expense["amount"] for expense in expenses)    

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route('/delete/<int:index>')
def delete(index):
    if 0<= index < len(expenses):
        expenses.pop(index)
        
    return redirect('/')

app.run(debug=True)