# Mini Project: Quiz 2.0 (CSV-Driven)

**Goal:**
Improve the old quiz by loading questions from a CSV file and using clean, reusable functions — **with Git and GitHub workflow**.

You will work **step by step**.After each task:

- run the program
- commit your changes

---

## Task 0 — Project & Git Setup

### Code setup

1. Create a folder:

```bash
mkdir quiz2
cd quiz2
```

2. Add files:

- `quiz.py`
- `quiz_questions.csv`

3. Run once:

```bash
python quiz.py
```

### Git setup

4. Initialize git:

```bash
git init
```

5. Create `.gitignore`:

```txt
__pycache__/
*.pyc
```

6. First commit:

```bash
git add .
git commit -m "Initial project setup"
```

7. Create a **GitHub repository** (empty, no README)
8. Connect and push:

```bash
git branch -M main
git remote add origin <repo-url>
git push -u origin main
```

**Done when:** repository exists on GitHub with first commit.

---

# Multi-PR Workflow (Important)

**Rule:**
**One PR = one clear improvement**
No PR should be bigger than **1–2 functions**.

**Never code directly on `main` branch!**

---

## Branch Naming

Use these prefixes:

- `chore/...` for setup / cleanup
- `feature/...` for new functionality
- `fix/...` for bug fixes

Examples:

- `chore/project-setup`
- `feature/load-csv`
- `feature/input-validation`

---

## PR Breakdown (Create Multiple PRs)

### PR 1 — Project & CSV Setup

**Branch:** `chore/project-setup`

Includes:

- `quiz.py` (hello world is fine)
- `quiz_questions.csv`
- `.gitignore`

Commands:

```bash
git checkout -b chore/project-setup
git add .
git commit -m "Initial project and CSV setup"
git push -u origin chore/project-setup
```

PR title:

```
Initial project setup
```

Merge this PR.

---

### PR 2 — Load CSV Questions

**Branch:** `feature/load-csv`

Includes:

- `load_questions()`
- CSV reading with `csv.DictReader`
- Print number of loaded questions

Commands:

```bash
git checkout -b feature/load-csv
git add .
git commit -m "Load questions from CSV"
git push -u origin feature/load-csv
```

PR title:

```
Load quiz questions from CSV
```

---

### PR 3 — Parse Question Data

**Branch:** `feature/question-model`

Includes:

- Parse `answers` into a list (split by `;`)
- Create a clean question dictionary structure

Commands:

```bash
git checkout -b feature/question-model
git add .
git commit -m "Parse CSV rows into question objects"
git push -u origin feature/question-model
```

PR title:

```
Parse quiz questions into structured objects
```

---

### PR 4 — Display a Question

**Branch:** `feature/print-question`

Includes:

- `print_question(question)` to format output
- Show `a/b/c` options

Commands:

```bash
git checkout -b feature/print-question
git add .
git commit -m "Add formatted question output"
git push -u origin feature/print-question
```

PR title:

```
Display quiz questions with options
```

---

### PR 5 — User Input Validation

**Branch:** `feature/input-validation`

Includes:

- `get_user_answer(valid_letters)`
- Keep asking until input is valid

Commands:

```bash
git checkout -b feature/input-validation
git add .
git commit -m "Validate user answer input"
git push -u origin feature/input-validation
```

PR title:

```
Validate quiz answer input
```

---

### PR 6 — Answer & Scoring Logic

**Branch:** `feature/answer-question`

Includes:

- `answer_question(question)`
- Return `+1` if correct, `-1` if wrong

Commands:

```bash
git checkout -b feature/answer-question
git add .
git commit -m "Add answer handling and scoring"
git push -u origin feature/answer-question
```

PR title:

```
Handle quiz answers and scoring
```

---

### PR 7 — Run Full Quiz

**Branch:** `feature/run-quiz`

Includes:

- `run_quiz(questions)`
- Loop through questions and track score

Commands:

```bash
git checkout -b feature/run-quiz
git add .
git commit -m "Run quiz from start to finish"
git push -u origin feature/run-quiz
```

PR title:

```
Run full quiz flow
```

---

### PR 8 — Quiz Selection

**Branch:** `feature/quiz-filter`

Includes:

- `filter_by_quiz(questions, quiz_name)`
- Ask user which quiz to play, then filter

Commands:

```bash
git checkout -b feature/quiz-filter
git add .
git commit -m "Filter questions by quiz name"
git push -u origin feature/quiz-filter
```

PR title:

```
Allow user to select quiz
```

---

## PR Checklist (Before Opening PR)

- [ ]  I ran the script: `python quiz.py`
- [ ]  My PR changes only **one feature**
- [ ]  I used small commits with clear messages
- [ ]  I did not commit directly to `main`
- [ ]  The code is easy to read (functions, not copy-paste)

# Coding Tasks (Step-by-step)

## Task 1 — Read the CSV File

**Objective:** Load the CSV and print all questions.

- Import `csv`
- Use `csv.DictReader`
- Loop through rows
- Print `row["question"]`

```bash
python quiz.py
```

---

## Task 2 — Parse a Question Row

**Objective:** Convert one CSV row into a Python dictionary.

Each question should contain:

- `quiz`
- `category`
- `question`
- `answers` (list split by `;`)
- `correct`

---

## Task 3 — Create `load_questions()` Function

Create:

```python
def load_questions(filename):
    ...
```

- Return a list of questions

---

## Task 4 — Print One Question Nicely

Create:

```python
def print_question(question):
    ...
```

- Print category, question text, and options `a/b/c`

---

## Task 5 — Validate User Input

Create:

```python
def get_user_answer(valid_letters):
    ...
```

- Keep asking until user types a valid letter

---

## Task 6 — Answer a Question

Create:

```python
def answer_question(question):
    ...
```

- Print question
- Ask input
- Return `+1` correct / `-1` wrong

---

## Task 7 — Run the Full Quiz

Create:

```python
def run_quiz(questions):
    ...
```

- Loop questions
- Track total score
- Print final score

---

## Task 8 — Filter by Quiz Name

Create:

```python
def filter_by_quiz(questions, quiz_name):
    ...
```

- Run only questions matching quiz name
