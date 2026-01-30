from flask import Flask, request, render_template
from classifier import classify_email, generate_response
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    category = ""
    response = ""
    if request.method == "POST":
        email_text = ""

        # Caso o usuário tenha enviado um arquivo
        if "file" in request.files and request.files["file"].filename != "":
            file = request.files["file"]

            if file.filename.endswith(".pdf"):
                reader = PdfReader(file)
                email_text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
            elif file.filename.endswith(".txt"):
                email_text = file.read().decode("utf-8")

        # Caso tenha colado texto no textarea
        elif "email_text" in request.form and request.form["email_text"].strip() != "":
            email_text = request.form["email_text"]

        # Se houver conteúdo, processa
        if email_text:
            category = classify_email(email_text)
            response = generate_response(category, email_text)

    return render_template("index.html", category=category, response=response)

if __name__ == "__main__":
    app.run(debug=True)
