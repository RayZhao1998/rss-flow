from flask import Flask
from flask import jsonify
from generate_page import get_first_10_blogs

app = Flask(__name__)

@app.route('/')
def index():
    blogs = []
    f = open("index.txt")
    for i in range(10):
        title = f.readline()
        link = f.readline()
        time = f.readline()
        blogs.append({'title': title, 'link': link, 'time': time})
    f.close()
    return jsonify(blogs)

if __name__ == "__main__":
    app.run()
