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

    return send_from_directory(
        FRONTEND_DIR,
        "index.html"
    )


@app.route("/<path:filename>")
def frontend_files(filename):

    return send_from_directory(
        FRONTEND_DIR,
        filename
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/api/health")
def health():

    return jsonify({

        "status": "success",

        "message":
            "STORY AI backend is running",

        "ai_configured":
            client is not None

    })


# ============================================================
# GENERATE STORY
# ============================================================

@app.route("/api/generate-story", methods=["POST"])
def generate_story():

    data = request.get_json() or {}


    # --------------------------------------------------------
    # GET USER INPUT
    # --------------------------------------------------------

    idea = data.get("idea", "").strip()

    title = data.get(
        "title",
        ""
    ).strip()

    genre = data.get(
        "genre",
        "Fantasy"
    )

    mood = data.get(
        "mood",
        "Magical"
    )

    length = data.get(
        "length",
        "Short"
    )

    character = data.get(
        "character",
        ""
    ).strip()

    setting = data.get(
        "setting",
        ""
    ).strip()


    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not idea:

        return jsonify({

            "status": "error",

            "message":
                "Please provide a story idea."

        }), 400


    if client is None:

        return jsonify({

            "status": "error",

            "message":
                "AI service is not configured yet."

        }), 503


    # --------------------------------------------------------
    # STORY LENGTH
    # --------------------------------------------------------

    if length == "Short":

        length_instruction = """
Write approximately 700–1000 words.
Focus on a strong beginning, atmosphere,
characters and a meaningful cliffhanger.
"""

    elif length == "Medium":

        length_instruction = """
Write approximately 1200–1800 words.
Develop the characters, world and plot carefully.
Include meaningful dialogue and a strong ending hook.
"""

    else:

        length_instruction = """
Write approximately 2000–3000 words.
Create a rich immersive world with detailed
characters, dialogue, atmosphere and plot progression.
End with a compelling cliffhanger.
"""


    # --------------------------------------------------------
    # GEMINI PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the creative storytelling engine of STORY AI.

Your purpose is to transform a user's imagination
into an immersive fictional experience.

Create a completely original story based on the
information below.

USER'S STORY IDEA:
{idea}

PREFERRED TITLE:
{title if title else "Create a compelling title"}

GENRE:
{genre}

MOOD:
{mood}

MAIN CHARACTER:
{character if character else "Create a suitable protagonist"}

SETTING:
{setting if setting else "Create an imaginative setting"}

STORY LENGTH:
{length}

{length_instruction}

WRITING STYLE:

- Highly immersive
- Cinematic atmosphere
- Strong sensory descriptions
- Natural dialogue
- Interesting characters
- Clear narrative progression
- Original ideas
- Avoid clichés where possible
- Make the reader feel present inside the world

STRUCTURE:

TITLE:
Create the final story title.

PREMISE:
Write a short 2–4 sentence description.

CHARACTERS:
Introduce the important characters naturally.

CHAPTER 1:
Write the opening chapter.

CLIFFHANGER:
End with an intriguing event, revelation,
question or discovery that makes the reader
want to continue.

IMPORTANT:

Do not explain your instructions.

Do not mention that you are an AI.

Do not discuss the prompt.

Write only the story content.

Make the story feel like the beginning of
a real novel.
"""


    # --------------------------------------------------------
    # GENERATE
    # --------------------------------------------------------

    try:

        response = client.models.generate_content(

            model="gemini-3.5-flash",

            contents=prompt

        )


        story = response.text


        # ----------------------------------------------------
        # RETURN RESULT
        # ----------------------------------------------------

        return jsonify({

            "status":
                "success",

            "title":
                title if title
                else "Your Story",

            "story":
                story

        })


    except Exception as e:

        print(
            "GENAI ERROR:",
            str(e)
        )


        return jsonify({

            "status":
                "error",

            "message":
                "Story generation failed.",

            "details":
                str(e)

        }), 500


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=False

    )
