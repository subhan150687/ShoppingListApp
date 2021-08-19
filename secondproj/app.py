from flask import Flask, render_template, request, redirect, url_for, json


app = Flask(__name__)

# /// = relative path, //// = absolute path
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)



@app.route("/")
def home():
    with open('items.json') as f:
        item_list=json.load(f)
    #print(todo_list)
    return render_template("base.html", item_list=item_list)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    quantity = 0
    new_item = {"name":name, "quantity":quantity}
    with open('items.json','r') as f:
        item_list=json.load(f)
    item_list.append(new_item)
    with open('items.json','w') as f:
        json.dump(item_list,f)
    return redirect(url_for("home"))


@app.route("/update/<string:item_name>")
def update(item_name):
    with open('items.json','r') as f:
        item_list=json.load(f)
    for item in item_list:
        if item["name"]==item_name:
            if item["quantity"]>=0 and item["quantity"]<=9:
                item["quantity"]=item["quantity"]+1
            break
    with open('items.json','w') as f:
        json.dump(item_list,f)
    return redirect(url_for("home"))


@app.route("/delete/<string:item_name>")
def delete(item_name):
    with open('items.json','r') as f:
        item_list=json.load(f)
    for item in item_list:
        if item["name"]==item_name:
            if item["quantity"]!=0:
                item["quantity"]=item["quantity"]-1
            break
    with open('items.json','w') as f:
        json.dump(item_list,f)
    return redirect(url_for("home"))
 #   todo = Todo.query.filter_by(id=todo_id).first()
  #  db.session.delete(todo)
   # db.session.commit()
   # return redirect(url_for("home"))

if __name__ == "__main__":
    #db.create_all()
    #db.session.commit()
    app.run(debug=True)
