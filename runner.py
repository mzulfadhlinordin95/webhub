from bottle import *
import bottle
import os

application = default_app()

@route("/")
def main():
	return template("index.html")

@route("/bs")
def bs():
	return template("bs.html")

@route('/favicon.ico')
def get_favicon():
	return server_static('favicon.ico')

@route('/robots.txt')
def serve_robots():
	return static_file('robots.txt',root='./static/')

# specifying the path for the files
@route('/<filepath:path>')
@route('/bs/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='./static/')

if __name__ == '__main__':
	application.run(reloader=True, host="0.0.0.0", port=int(os.environ.get("PORT", 9000))) 