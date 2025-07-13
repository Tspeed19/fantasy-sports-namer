import os
from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    team_name = None

    if request.method == "POST":
        user_input = request.form["player_name"]

        prompt_text = f"""
        You are a witty and creative sports humor writer.

        Generate exactly 1 unique, funny fantasy football team name based on the name: "{user_input}"

        Rules:
        - The name must include or play on words from "{user_input}"
        - Make it clever, humorous, and safe for work
        - Use creative puns, cultural references, or wordplay
        - Avoid generic sports phrases like "Champions", "Winners", "Squad"
        - Max 4 words
        - It should sound like a real fantasy football team name

        Return only the team name and nothing else.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative assistant who generates funny fantasy football team names."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=1.2,
            max_tokens=50
        )

        team_name = response.choices[0].message.content.strip()

    return render_template("index.html", team_name=team_name)

# ✅ THIS IS THE MISSING PART
if __name__ == "__main__":
    app.run(debug=True)
