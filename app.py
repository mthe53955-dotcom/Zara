from flask import Flask

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>zara</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Courier New', monospace;
        }
        h1 {
            font-size: 2.2rem;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>
    <h1>zara is here</h1>
</body>
     <h1>The Forum...</h1>
</html>
"""

@app.route("/")
def home():
    return PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
