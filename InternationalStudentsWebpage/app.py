# import necessary libraries
from flask import Flask, render_template, url_for, jsonify

# create Flask app
app = Flask(__name__)

# create data for students
students = [    
    {    
    "id": 1,    
    "name": "John Doe",        
    "country": "USA",        
    "picture": "john_doe.jpg",        
    "title": "Studying Abroad in the US",        
    "subtitle": "My experience as an international student",        
    "article": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam commodo, magna eu facilisis tincidunt, nisl ante auctor arcu, id commodo magna dui vitae nulla. Donec pellentesque, arcu vel blandit dapibus, mi nunc venenatis sem, vel faucibus orci nibh auctor eros.",        
    "quote": "I love studying abroad!"    
    },    
    {
    "id": 2,
    "name": "Jane Smith",        
     "country": "Canada",        
     "picture": "jane_smith.jpg",        
     "title": "Adapting to Life in Canada",        
     "subtitle": "My journey as an international student",        
     "article": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam commodo, magna eu facilisis tincidunt, nisl ante auctor arcu, id commodo magna dui vitae nulla. Donec pellentesque, arcu vel blandit dapibus, mi nunc venenatis sem, vel faucibus orci nibh auctor eros.",        
     "quote": "I am learning so much from this experience!"    
    }
]


# define routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/students")
def student_list():
    return jsonify(students)

@app.route("/student/<int:id>")
def student_detail(id):
    student = students[id-1]
    return render_template("student_detail.html", student=student)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
