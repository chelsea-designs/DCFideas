from flask import flash, render_template, request, redirect, url_for, session
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from dcfideas import app, mongo, db
from dcfideas.models import Strand, Idea
from datetime import datetime


@app.route("/")
def home():
    recentideas = list(Idea.query.order_by(Idea.created_at.desc()).limit(3).all())
    strands = list(Strand.query.order_by(Strand.id).all())
    return render_template("index.html", recentideas=recentideas, strands=strands)


# ---------- Ideas CRUD Functionality ---------- #

# --- Create Idea --- #
@app.route("/add_idea", methods=["GET", "POST"])
def add_idea():
    strands = list(Strand.query.order_by(Strand.id).all())
    subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
    camau_cynnydd = ['2','3','4','5']

    if "user" not in session:
        flash("You must be logged in to add ideas.")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            print("testing")
            idea = Idea(
                idea_name = request.form.get("idea_name"),
                idea_description = request.form.get("idea_description"),
                strand_id = request.form.get("strand-selector"),
                created_by = session["user"],
                created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                cam_cynnydd = request.form.get("cam_cynnydd-selector"),
                subject = request.form.get("subject-selector"),
                idea_resource = request.form.get("idea_resource")
            )
            db.session.add(idea)
            db.session.commit()
            return redirect(url_for('ideas'))
            flash("Idea added")
    return render_template("add_idea.html", strands=strands, subjects=subjects, camau_cynnydd=camau_cynnydd)

# --- Read Ideas --- #
@app.route("/about")
def about():
    strands = list(Strand.query.order_by(Strand.id).all())
    categories = set()
    for x in strands:
        categories.add(x.strand_name)
    return render_template("about.html", strands=strands, categories=categories)

@app.route("/full_idea/<int:idea_id>")
def full_idea(idea_id):
    """
    Displays full idea including description and link
    """
    if "user" not in session:
        flash("You must be logged in to view full idea details.")
        return redirect(url_for("login"))
    else:
        strands = list(Strand.query.order_by(Strand.id).all())
        categories = set()
        for x in strands:
            categories.add(x.strand_name)
        subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
        idea = Idea.query.get_or_404(idea_id)
        recentideas = list(Idea.query.order_by(Idea.created_at.desc()).limit(3).all())
    return render_template("full_idea.html", idea=idea, strands=strands, recentideas=recentideas, categories=categories, subjects=subjects)


# --- Update Ideas --- #
@app.route("/update_idea/<int:idea_id>", methods=["GET", "POST"])
def update_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    strands = list(Strand.query.order_by(Strand.id).all())
    subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
    camau_cynnydd = ['2','3','4','5']
    if "user" not in session:
        flash("You must be logged in to view edit ideas.")
        return redirect(url_for("login"))
    else:
        if session["user"].lower() == idea.created_by.lower() or session["user"].lower() == "admin".lower():
            print("testing")
            print(idea.strand_id)
            if request.method == "POST":
                idea.idea_name = request.form.get("idea_name"),
                idea.idea_description = request.form.get("idea_description"),
                idea.strand_id = request.form.get("strand-selector"),
                idea.created_by = session["user"],
                idea.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                idea.cam_cynnydd = request.form.get("cam_cynnydd-selector"),
                idea.subject = request.form.get("subject-selector"),
                idea.idea_resource = request.form.get("idea_resource")
                db.session.commit()
                return redirect(url_for('ideas'))
                flash("Idea updated")
        else:
            flash("You cannot update other users' ideas.")
            return redirect(url_for("ideas"))
    return render_template("update_idea.html", idea=idea, strands=strands, subjects=subjects, camau_cynnydd=camau_cynnydd)

# --- Delete Ideas --- #
@app.route("/delete_idea/<int:idea_id>")
def delete_idea(idea_id):
    idea = Idea.query.get_or_404(idea_id)
    if "user" not in session:
        flash("You must be logged in to delete ideas.")
        return redirect(url_for("login"))
    else:
        if session["user"].lower() == idea.created_by.lower() or session["user"].lower() == "admin".lower():
            db.session.delete(idea)
            db.session.commit()
            flash("Idea deleted")
        else:
            flash("You cannot delete other users' ideas.")
            return redirect(url_for("ideas"))
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


# ---------- User Account Functionality ---------- #

# --- Register Profile  --- #
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

# --- Login Profile  --- #
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

# ---  Profile  --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    ideas = list(Idea.query.order_by(Idea.idea_name).all())
    strands = list(Strand.query.order_by(Strand.id).all())

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", ideas=ideas, strands=strands, username=username)

    return redirect(url_for("login"))

# --- Logout  --- #
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# --- Change Password --- #
@app.route("/change_password/<username>", methods=["POST", "GET"])
def change_password(username):
    if request.method == "POST":
        new_password = generate_password_hash(request.form.get("new_password"))
        mongo.db.users.update(
            {"username": username},
            {"$set": {"password": new_password}})
        flash("Your Password has been changed")
        return redirect(url_for("profile", username=session["user"]))


# --- Delete Profile  --- #
@app.route('/delete_account/<user_id>', methods=["GET", "POST"])
def delete_account(user_id):
    user = mongo.db.users.find_one({'username': session["user"]})
    if check_password_hash(user["password"],
        request.form.get("confirm-deletion")):
        flash("We can confirm that your account has been deleted.")
        session.pop("user")
        mongo.db.users.remove({"_id": ObjectId(user['_id'])})
        return redirect(url_for("register"))
    else:
        flash("The password you entered was incorrect. Please try again!")
        return redirect(url_for("profile", username=session["user"]))
    return redirect(url_for("register"))


# ---------- Search and Filter Functionality ---------- #

# --- New Search --- #
@app.route('/search', methods=["POST"])
def search():
    if request.method: "POST"
    searched = request.form.get('searched')
    ideas = Idea.query.filter(Idea.idea_description.like('%' + searched + '%')).order_by(Idea.idea_name).all()
    subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
    strands = list(Strand.query.order_by(Strand.id).all())
    categories = set()
    for x in strands:
        categories.add(x.strand_name)

    return render_template("ideas.html", searched = searched, ideas=ideas, strands=strands, subjects=subjects, categories=categories)

# --- Filter Ideas By Strand Name  --- #
@app.route("/ideas/strand_name<strand_name>")
def filter_ideas_by_strand_name(strand_name):
    subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
    strands = list(Strand.query.order_by(Strand.id).all())
    categories = set()
    for x in strands:
        categories.add(x.strand_name)
    if strand_name=='Dinasyddiaeth':
        ideas = list(Idea.query.filter(Idea.strand_id.between(1,4)).all())
    elif strand_name=='Rhyngweithio a chydweithio':
        ideas = list(Idea.query.filter(Idea.strand_id.between(5,7)).all())
    elif strand_name=='Cynhyrchu':
        ideas = list(Idea.query.filter(Idea.strand_id.between(8,10)).all())
    elif strand_name=='Data a meddwl cyfrifiadurol':
        ideas = list(Idea.query.filter(Idea.strand_id.between(11,12)).all())
    return render_template("ideas.html", ideas=ideas, strands=strands, subjects=subjects, categories=categories)

# --- Filter Ideas Using Query Params  --- #
@app.route("/ideas")
def filter_ideas_by_query_param():
    args = request.args
    subjects = ['Cymraeg','Saesneg','Ffrangeg','Sbaeneg','Hanes','Daearyddiaeth','Addysg Grefyddol','Busnes','Celf','Cerddoriaeth','Drama','Mathemateg','Bioleg','Cemeg','Ffiseg','Technoleg Digidol','Dylunio a Thechnoleg','Tecstiliau','Graffeg','Addysg Gorfforol','Bwyd a Maeth','ABCh','Bagloriaeth Cymru']
    strands = list(Strand.query.order_by(Strand.id).all())
    camau_cynnydd = ['2','3','4','5']
    categories = set()
    for x in strands:
        categories.add(x.strand_name)
    if args.get("subject"):
        param = args.get("subject")
        ideas = list(Idea.query.filter_by(subject=param).all())
    elif args.get("strand_id"):
        param = args.get("strand_id")
        ideas = list(Idea.query.filter_by(strand_id=param).all())
    elif args.get("cam_cynnydd"):
        param = args.get("cam_cynnydd")
        ideas = list(Idea.query.filter_by(cam_cynnydd=param).all())
    elif args.get("created_by"):
        param = args.get("created_by")
        ideas = list(Idea.query.filter_by(created_by=param).all())
    else:
        ideas = list(Idea.query.order_by(Idea.idea_name).all())
    return render_template("ideas.html", subjects=subjects, strands=strands, ideas=ideas, categories=categories, camau_cynnydd=camau_cynnydd)