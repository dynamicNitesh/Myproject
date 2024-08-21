from flask import Flask,render_template,request,redirect,url_for,flash,session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = "food application"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'food'

mysql = MySQL(app)

app.config["UPLOAD_FOLDER"] = 'static/assets/'

@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from Product")
    data = cursor.fetchall()
    cursor.close()
    return render_template("index.html",data=list(data))

@app.route("/<cat>")
def category_vise(cat):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from Product WHERE category = %s",(cat,))
    data = cursor.fetchall()
    cursor.close()
    return render_template("index.html",data=list(data))


@app.route("/sign_in",methods=["GET","POST"])
def sign_in():
    if request.method == "GET":
        return render_template("signin.html")
    else:
        data = request.form
        cursor = mysql.connection.cursor()
        cursor.execute("select email,password from users WHERE email = %s",(data["email"],))
        record = cursor.fetchone()
        cursor.close()
        if record :
            if data["email"] == record[0] and data["password"] == record[1] :
                session["email"] = data["email"]
                session["passeord"] = data["password"]
                return redirect(url_for("index"))
            elif data["email"] == record[0] and data["password"] != record[1]:
                flash("Password Wrong")
                return redirect(url_for("sign_in"))
            else:
                flash("Unknown error")
                return redirect(url_for("sign_in"))
        elif data["email"]=="admin@gmail.com" and data["password"]=="admin@1234":
                session["admin"] = data["email"]
                return redirect(url_for("admin_home"))
        else:
            flash("Account not found")
            return redirect(url_for("sign_in"))
        
@app.route("/logout")
def logout():
    session.pop("email",None)
    session.pop("password",None)
    return redirect(url_for("sign_in"))

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        data = request.form
        cursor = mysql.connection.cursor()
        query = "INSERT INTO Users (name, email, phone, password) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(data["name"],data["email"],data["phone"],data["password"]))
        mysql.connection.commit()
        cursor.close()
        flash("Successfully Registered")
        return redirect(url_for("sign_in"))


@app.route("/admin_home",methods=["GET","POST"])
def admin_home():
    if "admin" in session:
        if request.method == "GET":
            return render_template("admin_home.html")
        else:
            data = request.form
            photo = request.files["photo"]
            photo.save(os.path.join(app.config["UPLOAD_FOLDER"],photo.filename))
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO Product (name, photo, category, price, description) VALUES (%s,%s,%s,%s,%s);",(data["name"],photo.filename,data["category"],data["price"],data["desc"]))
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for("admin_items"))
    else:
        flash("Please, sign in as admin")
        return redirect(url_for("sign_in"))


@app.route("/admin_items")
def admin_items():
    if "admin" in session:
        cursor = mysql.connection.cursor()
        cursor.execute("select * from Product")
        data = cursor.fetchall()
        cursor.close()
        return render_template("admin_items.html",data=list(data))
    else:
        flash("Please, sign in as admin")
        return redirect(url_for("sign_in"))

@app.route("/delete/<int:id>")
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Product WHERE id = %s",(id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for("admin_items"))

@app.route("/admin_orders")
def admin_orders():
    if "admin" in session:
        return render_template("admin_orders.html")
    else:
        flash("Please, sign in as admin")
        return redirect(url_for("sign_in"))

@app.route("/logout_admin")
def logout_admin():
    session.pop("admin",None)
    return redirect(url_for("sign_in"))

@app.route("/query")
def query():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from Product")
    data = cursor.fetchall()
    cursor.close()
    return list(data)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')