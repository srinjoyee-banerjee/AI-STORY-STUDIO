
import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from google import genai


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


# ============================================================
# FLASK
# ============================================================

app = Flask(__name__)
CORS(app)


# ============================================================
# GEMINI CLIENT
# ============================================================

API_KEY = os.environ.get("GEMINI_API_KEY")

client = None

if API_KEY:
    client = genai.Client(api_key=API_KEY)


# ============================================================
# FRONTEND
# ============================================================

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory(FRONTEND_DIR, filename)


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/api/health")
def health():

    return jsonify({
        "status": "success",
        "message": "AI Story Studio backend is running",
        "ai_configured": client is not None
    })


# ============================================================
# GENERATE STORY
# ============================================================

@app.route("/api/generate-story", methods=["POST"])
def generate_story():

    data = request.get_json() or {}

    idea = data.get("idea", "").strip()
    genre = data.get("genre", "Fantasy")
    tone = data.get("tone", "Cinematic")

    if not idea:

        return jsonify({
            "status": "error",
            "message": "Please provide a story idea."
        }), 400


    if client is None:

        return jsonify({
            "status": "error",
            "message": "AI service is not configured yet."
        }), 503


    prompt = f"""
You are the creative writing engine of AI Story Studio.

Create an original, immersive fictional story.

STORY IDEA:
{idea}

GENRE:
{genre}

TONE:
{tone}

Structure the response as:

TITLE:
A compelling title.

PREMISE:
A short description of the story.

CHARACTERS:
Introduce the important characters.

CHAPTER 1:
Write the opening chapter with strong atmosphere,
character development, dialogue and narrative progression.

CLIFFHANGER:
End with an interesting hook that encourages the reader
to continue the story.

Do not explain your instructions.
Do not mention that you are an AI.
Write original content.
"""


    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        story = response.text

        return jsonify({
            "status": "success",
            "title": "AI Story Studio",
            "story": story
        })


    except Exception as e:

        print("GENAI ERROR:", str(e))

        return jsonify({
            "status": "error",
            "message": "Story generation failed.",
            "details": str(e)
        }), 500


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
