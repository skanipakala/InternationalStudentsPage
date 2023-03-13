# import necessary libraries
from flask import Flask, render_template, url_for, jsonify

# create Flask app
app = Flask(__name__)
app.use_static_for = True

# create data for students
students = [    
    {    
    "id": 1,    
    "name": "Divyansh Agrawal",        
    "country": "India",        
    "picture": "john_doe.jpg",        
    "title": "Mental health stigma in India causes delays in intervention and treatment",        
    "subtitle": "Some multigenerational families provide guidance for youth while others pass down misconceptions about mental health.",        
    "article_file": "InternationalStudentsWebpage/static/articles/Divyansh Agrawal/Divyansh_Agrawal.txt",        
    "quote": "“As you talk to more people, you get aware, and then you can decide what\'s best for you,” Argawal said.",
    "author": "By Winter Hawk",
    "audio_file": "IndiaDivyansh.mp3"    
    },    
    {
    "id": 2,
    "name": "Sophia Anderson",        
    "country": "Denmark",        
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Sofia_Anderson.txt",        
    "quote": "I'm still trying to figure out how to live with ADHD, but I feel like the depression is not really that big a deal anymore,” Katharina Andersen said. “I don't go into those slumps anymore because I'm learning how to manage it beforehand.",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }, 
    {
    "id": 3,
    "name": "Luisa Barros-Checcucci",        
    "country": "Belgium",        
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Divyansh Agrawal.txt",        
    "quote": "I was breaking down and he made me feel terrible,” Barros-Checcucci said. “He was just kind of like, 'okay, well what do you want me to do about it' type of thing.",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }, 
    {
    "id": 4,
    "name": "Ubaid Bakhtiar",        
    "country": "Pakistan",         
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Divyansh Agrawal.txt",   
    "quote": "I don't have a friend from U.S.A,” Bakhtiar said. “People who are in U.S.A, they prefer to have friends with the people that are from U.S.A",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }, 
    {
    "id": 5,
    "name": "Jane Smith",        
    "country": "Canada",        
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Divyansh Agrawal.txt",   
    "quote": "I am learning so much from this experience!",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }, 
    {
    "id": 6,
    "name": "Jane Smith",        
    "country": "Canada",        
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Divyansh Agrawal.txt",   
    "quote": "I am learning so much from this experience!",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }, 
    {
    "id": 7,
    "name": "Jane Smith",        
    "country": "Canada",        
    "picture": "jane_smith.jpg",        
    "title": "Adapting to Life in Canada",        
    "subtitle": "My journey as an international student",        
    "article_file": "Divyansh Agrawal.txt",   
    "quote": "I am learning so much from this experience!",
    "author": "John Smith",
    "audio_file": "divyansh_agrawal_interview.mp3"     
    }
]

# Read the article function
def read_article(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()
        paragraphs = text.split('\n\n')  # split text into paragraphs using two newline characters as a delimiter
        return paragraphs
  
# define routes
@app.route("/")
def home():
    return render_template("home.html", students=students)

@app.route("/students")
def student_list():
    return jsonify(students)

@app.route("/student/<int:id>")
def student_detail(id):
    student = students[id-1]
    article_file = student['article_file']
    audio_file = student['audio_file']
    article = read_article(article_file)
    return render_template("student_detail.html", student=student, article=article, audio_file=audio_file)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
