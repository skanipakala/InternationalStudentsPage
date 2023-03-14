# import necessary libraries
from flask import Flask, render_template, url_for, jsonify
from students import students
# create Flask app
app = Flask(__name__)
app.use_static_for = True

# Read the article function
def read_article(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content =  f.read()
        paragraphs = content.split('\n\n')  # split text into paragraphs using two newline characters as a delimiter
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
    paragraphs = read_article(article_file)
    return render_template("student_detail.html", student=student, paragraphs=paragraphs, audio_file=audio_file)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
