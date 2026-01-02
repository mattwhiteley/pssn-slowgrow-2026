#import pandasql as psql
import streamlit as st

from flask import Flask, render_template, request, jsonify, redirect, make_response
from auth import set_admin_cookie, clear_admin_cookie, admin_required_route

import json
import os
from PIL import Image


app = Flask(__name__)

REGIONS_PATH = os.path.join("static", "regions.json")
USERS_PATH = os.path.join("static", "users.json")
MAP_PATH = os.path.join("static", "map.jpeg")


def load_json(path):
    with open(path, "r", encoding="utf8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def index():
    regions = load_json(REGIONS_PATH)
    users = load_json(USERS_PATH)

    img = Image.open(MAP_PATH)
    w, h = img.size

    return render_template(
        "index.html",
        regions=regions,
        users=users,
        img_width=w,
        img_height=h
    )


@app.post("/update_owner")
def update_owner():
    data = request.get_json()
    region_index = int(data["id"])
    owner_id = int(data["owner_id"])

    regions = load_json(REGIONS_PATH)
    regions[region_index]["owner_id"] = owner_id
    save_json(REGIONS_PATH, regions)

    return jsonify({"status": "ok"})

@app.route("/login-admin")
def login_admin():
    response = make_response(redirect("/"))
    return set_admin_cookie(response)


@app.route("/logout")
def logout():
    response = make_response(redirect("/"))
    return clear_admin_cookie(response)

@app.route("/admin/delete-user", methods=["POST"])
@admin_required_route
def delete_user():
    return "User deleted"


if __name__ == "__main__":
    app.run(debug=True)
