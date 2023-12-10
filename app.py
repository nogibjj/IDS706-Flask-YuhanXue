from flask import Flask, render_template, request
from copy import deepcopy
from transformers import pipeline

app = Flask(__name__)
en_fr_translator = pipeline("translation_en_to_fr")

app_data = {
    "name": "Yuhan's Flask App",
    "description": "Flask app using LLM",
    "author": "Yuhan Xue",
    "html_title": "Flask App",
    "project_name": "Flask App",
    "keywords": "flask, webapp, llm",
}


@app.route("/")
def home():
    return render_template("index.html", app_data=app_data)


@app.route("/translate", methods=["GET", "POST"])
def translate():
    if request.method == "POST":
        input_text = request.form["prompt"]

        # Extract the English sentence
        prompt = f"{input_text}"

        # Translate using BART LLM based on the constructed prompt
        Answer = en_fr_translator(prompt)

        # Extract the translated texts
        txt = Answer[0]["translation_text"]
        tmp = deepcopy(app_data)
        tmp["response"] = txt

        return render_template("index.html", app_data=tmp)
    return render_template("index.html", app_data=app_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
