from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>💌 Valentine ?</title>
    <style>
        body {
            background-color: #ffe6eb;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
        }
        h1 { color: #d6336c; }
        p { font-size: 22px; }
        button {
            font-size: 20px;
            padding: 15px 30px;
            margin: 20px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .yes { background-color: #ff4d6d; color: white; }
        .no { background-color: #adb5bd; color: white; }
    </style>
</head>
<body>
    {% if answer %}
        {% if answer == 'yes' %}
            <h1>💖 OUIIIII 💖</h1>
            <p>Je t'aime plus que tout ma juju d'amour 💕</p>
            <p>Je t'aime à l'infini ♾️❤️</p>
        {% else %}
            <h1>😱 Impossible.</h1>
            <p>Reviens cliquer sur OUI 💖 😌 et KOULI KHARA</p>
        {% endif %}
    {% else %}
        <h1>💌 Veux-tu être ma Valentine ? 💌</h1>
        <form method="post">
            <button name="answer" value="yes" class="yes">Oui 💖</button>
            <button name="answer" value="no" class="no">Non 🙈</button>
        </form>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = request.form.get("answer")
    return render_template_string(HTML, answer=answer)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

