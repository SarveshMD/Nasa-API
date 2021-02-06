import os

os.remove("APOD.sqlite")

vars_js = open("variables.js", "a")
vars_js.truncate(0)