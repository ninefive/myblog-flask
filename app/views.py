#!/usr/bin/env python
# coding = utf-8
__author__ = "milo zhao"

from flask import render_template
from app import app

@app.route("/")
@app.route("/index/")
def index():
	user = {"nickname":"milo"}
	posts = [
			{"author":{"nickname":"Ancel"},
			 "body":"This is my first Flask project"
			 	},
			{"author":{"nickname":"Andy"},
			 "body":"This is my micro blog"
				}
			]
	return render_template("index.html",title="Flask",user=user,posts=posts)
