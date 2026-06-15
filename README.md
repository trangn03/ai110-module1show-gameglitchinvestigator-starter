# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Game's purpose
  - Guessing a secret number that build with Streamlit app. First, choose a difficulty and the chance that you have to guess based on your difficulty. The app will give a hint whether you need to guess the number higher or lower. If you run out of attempts, the secret number will be reveal and you have options to start a new game
- Bugs I found
  - The game already counted one attempt when first started.
  - After submitting the first guess, the game did not update the attempt, which is still show 7 on the screen.
  - The hints were backwards. When user guess too high number, it display "Go HIGHER!" instead of "Go LOWER!".
  - After losing, click "New game" froze the screen and just showing the game is over. 
- Fixes I applied.
  - Changed ```attempts``` to start at 0 instead of 1 to fix the off by one scoring
  - Move the increment inside the ```else``` block in if submit function so it only runs when ```parse_guess``` return ```ok=True```.
  - Refactor the function into ```logic_utils.py``` by swapped the hint messages so "Too High" displays "Go LOWER!" and "Too Low" display "Go HIGHER!"
  - Updated the New Game handler to reset the attempt, score, history, and status

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
