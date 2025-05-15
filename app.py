from flask import Flask, render_template, request, redirect, session
import random, json, os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Load/save users
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Fake users and post images
FAKE_USERS = ["@naturelover", "@chef_mom", "@dev_coder", "@art_queen", "@travel_guru"]
POST_IMAGES = [
    "nature.jpg", "food.jpg", "code.jpg", "art.jpg", "travel.jpg"
]  # These should exist in /static/images/

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        if username in users:
            if users[username]["password"] == password:
                session["username"] = username
                return redirect("/posts")
            else:
                return render_template("index.html", error="Incorrect password.")
        else:
            users[username] = {
                "password": password,
                "liked_posts": [],
                "followed_users": []
            }
            save_users(users)
            session["username"] = username
            return redirect("/posts")
    return render_template("index.html")


@app.route("/posts", methods=["GET", "POST"])
def posts():
    if "username" not in session:
        return redirect("/")

    posts = []
    for i in range(5):
        user = random.choice(FAKE_USERS)
        image = random.choice(POST_IMAGES)
        post_id = random.randint(1000, 9999)
        posts.append({"post_id": post_id, "user": user, "image": image})

    return render_template("posts.html", posts=posts)


@app.route("/action", methods=["POST"])
def action():
    post_id = int(request.form["post_id"])
    post_user = request.form["post_user"]
    image = request.form["image"]
    like = request.form.get("like")
    follow = request.form.get("follow")

    users = load_users()
    current_user = session["username"]

    if like == "on":
        users[current_user]["liked_posts"].append({"post_id": post_id, "user": post_user, "image": image})
    if follow == "on" and post_user not in users[current_user]["followed_users"]:
        users[current_user]["followed_users"].append(post_user)

    save_users(users)
    return redirect("/posts")


@app.route("/history")
def history():
    if "username" not in session:
        return redirect("/")
    
    users = load_users()
    user_data = users.get(session["username"], {})
    return render_template("history.html", user=session["username"], data=user_data)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)