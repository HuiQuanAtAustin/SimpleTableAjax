from flask import Flask, render_template
from dataflow import etl
app= Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    #more codes go here
    return render_template('index.html')

@app.route('/Inventory', methods=['POST'])
def inventory():
    #more codes go here
    return render_template('inventory.html')

@app.route('/Sales', methods=['GET', 'POST'])

def display():
    form = PostForm()
    if form.validate_on_submit():
        #Actual code goes her
    return render_template('Sales.html')

if __name__ == "__main__":
    app.run()