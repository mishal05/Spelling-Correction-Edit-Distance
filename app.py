from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# --- Load English words file ---
with open("words.txt", "r", encoding="utf-8") as f:
    WORDS = set(w.strip().lower() for w in f if w.strip().isalpha())

# --- Edit Distance Function ---
def edit_distance(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[-1][-1]

# --- Suggest Closest Words ---
def suggest_word(word):
    word = word.lower()
    if word in WORDS:
        return {"correct": True, "suggestions": [word]}
    candidates = [(w, edit_distance(word, w)) for w in WORDS if abs(len(w) - len(word)) <= 2]
    candidates.sort(key=lambda x: x[1])
    best = [w for w, d in candidates[:3] if d <= 2]
    return {"correct": False, "suggestions": best or ["No close matches found."]}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    word = request.form.get("word", "").strip()
    if not re.match("^[a-zA-Z]+$", word):
        return jsonify({"error": "Please enter alphabets only."})
    return jsonify(suggest_word(word))

if __name__ == "__main__":
    app.run(debug=True)
