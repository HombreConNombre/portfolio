import requests
from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal para mostrar la página de inicio (index.html)
@app.route("/")
def index():
    repos_list = get_repos()
    technologies = [
        {"name": "Python", "icon": "images/Python.png"},
        {"name": "Flask", "icon": "images/flask.svg"},
        {"name": "Django", "icon": "images/django.png"},
        {"name": "HTML5", "icon": "images/html5.png"},
        {"name": "CSS3", "icon": "images/css3.png"},
        {"name": "JS", "icon": "images/js.png"},
        {"name": "Java", "icon": "images/Java.svg"},
        {"name": "Spring", "icon": "images/spring.png"},
        {"name": "C++", "icon": "images/CPP.png"}
    ]
    return render_template(
        "index.html", 
        technologies=technologies,
        repos = repos_list
        )

def get_repos():
    github_username = "HombreConNombre"
    url = f"https://api.github.com/users/{github_username}/repos?sort=updated&per_page=5"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
