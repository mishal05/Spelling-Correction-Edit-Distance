
## Spelling Correction using Edit Distance

### Microproject  – Introduction to AI and NLP

### Objective

To implement a **spelling correction system** using **Edit Distance**, **Regular Expressions**, and **Text Processing** techniques. The system checks a single word typed by the user and provides correction suggestions. If the word is correct, a success animation appears.

---

###  Features

* Backend implemented with **Python (Flask)**
* Edit distance–based **spelling correction algorithm**
* Uses **Regular Expressions** for word validation and cleaning
* Simple and **colorful frontend** using **HTML, CSS, and JavaScript**
* **Keyboard and mouse interactive**
* A **Submit** button triggers correction
* **Reset** button clears input
* Displays a **thumbs-up animation** when the spelling is correct
* Suggests **closest words** when incorrect
* Uses an **online dictionary file (words.txt)**

---

### Folder Structure

```
SpellingCorrection/
│
├── static/
│   ├── style.css          # Frontend styling (UI colors, animations)
│   └── images/            # Optional image assets
│
├── templates/
│   └── index.html         # Frontend HTML structure
│
├── app.py                 # Flask backend for Edit Distance logic
├── words.txt              # Dictionary file with valid words
└── README.md              # Project documentation
```

---

### How It Works

1. User enters a single word in the text box.
2. On clicking **Submit**, the Flask backend:

   * Cleans input using **Regular Expressions**
   * Compares the word with dictionary entries
   * Calculates the **Levenshtein (edit) distance**
   * Finds closest matches and returns suggestions
3. If the word matches an entry → shows ✅ animation.
4. If incorrect → shows ❌ and top 3 nearest suggestions.

---

###  How to Run

#### Step 1: Install Dependencies

Make sure you have Python 3 installed.
Then install Flask:

```bash
pip install flask
```

#### Step 2: Place the Dictionary File

Download the dictionary file (`words.txt`) from
👉 [https://raw.githubusercontent.com/dwyl/english-words/master/words.txt](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt)
Save it in your project root folder.

#### Step 3: Run the Server

```bash
python app.py
```

#### Step 4: Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

Type a word → click **Submit** → see results and suggestions.

---

###  Core Concepts Used

* **Regular Expressions (re module)** → to clean and validate input text
* **Text Processing** → reading dictionary words and computing similarity
* **Edit Distance (Levenshtein Distance)** → to find the minimum number of edits between input and dictionary words
* **Web App Integration** → linking Python logic with frontend UI

---

### Future Improvements

* Support for multiple words or full sentences
* Integration with larger language models for contextual correction
* Speech input and pronunciation-based corrections

---

### Developed By

**Mary Mishal Francis**


---

