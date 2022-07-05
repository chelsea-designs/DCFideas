from flask import flash, render_template, request, redirect, url_for, session
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from dcfideas import app, mongo, db
from dcfideas.models import Strand, Idea, Users


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        print(mongo.db)
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/strands")
def strands():
    strands = list(Strand.query.order_by(Strand.strand_name).all())
    categories = set()
    for x in strands:
        categories.add(x.strand_name)
    return render_template("strands.html", strands=strands, categories=categories)

@app.route("/ideas")
def ideas():
    ideas = list(Idea.query.order_by(Idea.idea_name).all())
    return render_template("ideas.html", ideas=ideas)

@app.route("/add_idea", methods=["GET", "POST"])
def add_idea():
    strands = list(Strand.query.order_by(Strand.strand_name).all())
    if "user" not in session:
        flash("You must be logged in to add ideas.")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            idea = Idea(
                idea_name=request.form.get("idea_name"),
                idea_description=request.form.get("idea_description"),
                strand_id=request.form.get("strand_id"),
                idea_teacher =request.form.get("idea_teacher"),
            )
            db.session.add(idea)
            db.session.commit()
            return redirect(url_for('ideas'))
            flash("Idea added")
    return render_template("add_idea.html", strands=strands)


@app.route("/update_idea/<int:idea_id>", methods=["GET", "POST"])
def update_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    strands = list(Strand.query.order_by(Strand.strand_name).all())
    if "user" not in session:
        flash("You must be logged in to view edit ideas.")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            idea.idea_name=request.form.get("idea_name")
            idea.idea_description=request.form.get("idea_description")
            idea.strand_id=request.form.get("strand_id")
            idea.idea_teacher=request.form.get("idea_teacher")
            db.session.commit()
            return redirect(url_for('ideas'))
            flash("Idea updated")
    return render_template("update_idea.html", idea=idea, strands=strands)

@app.route("/delete_idea/<int:idea_id>")
def delete_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    if "user" not in session:
        flash("You must be logged in to delete ideas.")
        return redirect(url_for("login"))
    else:
        db.session.delete(idea)
        db.session.commit()
        flash("Idea deleted")
    return redirect(url_for("ideas"))


# ---------- Error Handling Functionality ---------- #

# --- 404 Handler --- #
@app.errorhandler(404)
def page_not_found(e):
    """
    Renders a custom 404 error page with a button
    that takes the user back to the home page.
    """
    return render_template("errors/404.html", page_title="404"), 404


# --- 500 Handler --- #
@app.errorhandler(500)
def internal_server_error(e):
    """
    Renders a custom 500 error page with a button
    that takes the user back to the home page.
    """
    return render_template("errors/500.html", page_title="500"), 500





@app.route("/change_password/<username>", methods=["POST", "GET"])
def change_password(username):
    if request.method == "POST":
        new_password = generate_password_hash(request.form.get("new_password"))
        mongo.db.users.update(
            {"username": username},
            {"$set": {"password": new_password}})
        flash("Your Password has been changed")
        return redirect(url_for("profile", username=session["user"]))


# --- Delete Profile Functionality --- #
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = mongo.db.users.find_one({'username': session["user"]})
    # Checks if password matches existing password in database
    if check_password_hash(user["password"],
        request.form.get("confirm_deletion")):
        flash("We can confirm that your account has been deleted.")
        session.pop("user")
        mongo.db.users.remove({"_id": ObjectId(user['_id'])})
        return redirect(url_for("register"))
    else:
        flash("The password you entered was incorrect. Please try again!")
        return redirect(url_for("profile", username=session["user"]))
    # return to home page page
    return redirect(url_for("register"))
