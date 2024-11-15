import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Basic template with styling
html_template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Welcome to My Flask App</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
    .container { max-width: 500px; margin: auto; padding: 20px; }
    h1 { color: #333; }
    form { margin-top: 20px; }
    input, button { padding: 10px; margin: 5px; font-size: 16px; }
    .button { background-color: #007bff; color: white; border: none; }
  </style>
</head>
<body>
  <div class="container">
    <h1>{{ greeting }}</h1>
    {% if question %}
      <p>{{ question }}</p>
      <form method="POST" action="/response">
        <input type="text" name="user_input" placeholder="Your answer here..." required>
        <button class="button" type="submit">Submit</button>
      </form>
    {% else %}
      <a href="/">Go back to home</a>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/")
def main():
    return render_template_string(html_template, greeting="Welcome to My Flask App!", question="How are you?")

@app.route("/how_are_you")
def how_are_you():
    return render_template_string(html_template, greeting="Hello!", question="How are you?")

@app.route("/response", methods=["POST"])
def response():
    user_input = request.form.get("user_input")
    response_message = f"I'm glad to hear you're '{user_input}'!" if user_input else "I see!"
    return render_template_string(html_template, greeting="Response Received!", question=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

