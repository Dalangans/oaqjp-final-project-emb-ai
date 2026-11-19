"""Flask web server for the emotion detection application."""

from flask import Flask, render_template, request

from Final_project import emotion_detector as detect_emotion

app = Flask(__name__)


@app.get("/")
def index():
    """Render the provided emotion detection web page."""
    return render_template("index.html")


@app.get("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return a readable score summary."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = detect_emotion(text_to_analyze)
    emotion_scores = ", ".join(
        f"'{emotion}': {result[emotion]}"
        for emotion in ("anger", "disgust", "fear", "joy", "sadness")
    )
    return (
        f"For the given statement, the system response is {emotion_scores}. "
        f"Dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
