import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set!")

client = OpenAI(api_key=api_key)

user_input = input("Enter the name to generate a fantasy football team name for: ")

prompt_text = f"""

Generate exactly 1 unique, funny fantasy football team name based on the name: "{user_input}"

**Instructions:**
- The team name must specifically incorporate or play off parts of "{user_input}"
- Think sexual innuendo, potty humor, mild dirty jokes, or double meanings — but keep it PG-13, not explicit or pornographic
- The name should be clever, not just random dirty words
- Avoid simply putting two random words together that start with the same letter
- It should sound like something a human would say and laugh about
- Maximum length: 4 words
- Avoid generic words like “Champions,” “Squad,” “Winners,” etc.
- Return only the team name, nothing else

**Example of the humor style:**
- My Balls Zach Ertz (sounds like “my ballsack hurts”)
- Kupp My Balls
- Instant Kamara Sutra
- Golladay Inn Express
- Lick Chubb
- Ertz When I Pee
- Mahomies in Low Places

**Examples of good styles:**
- Mahomeland Security
- My Kupp Runneth Over
- Sherlock Mahomes
- Baby Got Dak
- Instant Kamara
- The Thielen is Mutual
- Chubb Hub
- Ertz So Good
- Zeke and Destroy
- Kittle Big Town

It is also ok to repeat any of the names listed just not frequently

Return only the team name and nothing else.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a creative assistant who generates funny fantasy football team names."
        },
        {
            "role": "user",
            "content": prompt_text
        }
    ],
    temperature=1.2,
    max_tokens=50
)

team_name = response.choices[0].message.content.strip()
print("Generated Team Name:", team_name)

