from flask import Flask, Response

app = Flask(__name__)

MESSAGE = "hello appsec world"


def colorful_text(text: str) -> str:
    colors = ["red", "green", "yellow", "blue", "purple"]
    spans = []

    for index, character in enumerate(text):
        color = colors[index % len(colors)]
        spans.append(
            f'<span style="color:{color}">{character}</span>'
        )

    return "".join(spans)


@app.get("/")
def index() -> Response:
    colored_message = colorful_text(MESSAGE)
    html = f"""
    <html>
    <head><title>Colorful Output</title></head>
    <body style="font-family: monospace; font-size: 24px;">
    {colored_message}
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/message")
def message() -> dict[str, str]:
    return {"message": MESSAGE}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # nosec B104
