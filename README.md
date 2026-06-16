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

1. **Launch the app.** Run `python -m streamlit run app.py` and it will automatically open the game in the browser. The title "🎮 Game Glitch Investigator" appears with a Setting sidebar.
2. **Pick a difficulty.** In the sidebar, there are three mode which are Easy, Normal, or Hard with different attempts. The sidebar shows the active range and the attempts allowed, and switching difficulty starts a fresh game.
3. **Enter a guess and click "Submit Guess 🚀".** A valid in-range number counts as one attempt; the "Attempts left" counter decreases by exactly one per guess. Empty, non-numeric, or out-of-range input shows an error and does not count as an attempt.
4. **Follow the hint.** With "Show hint" checked, a guess above the secret says "📉 Go LOWER!" and a guess below says "📈 Go HIGHER!" 
5. **Keep guessing toward the secret.** Each wrong guess is recorded in the history (viewable in the "Developer Debug Info" expander). Score rewards faster wins: an earlier win is worth more (100 − 10 × attempt, minimum 10).
6. **Win or out of attempt.** Guess the exact number to win — balloons pop and the final score is shown. If you used all the attempt limit, the game ends and reveals the secret.
7. **Start over with "New Game 🔁".** This resets attempts, score, status, and history, picks a new secret in the current range, and clears the input so the game is immediately playable again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.13.2, pytest-9.1.0, pluggy-1.6.0 -- C:\Users\xtran\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\xtran\Downloads\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.9.0
collecting ... collected 30 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  3%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [  6%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 10%]
tests/test_game_logic.py::test_parse_guess_valid_number PASSED           [ 13%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED           [ 16%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED            [ 20%]
tests/test_game_logic.py::test_parse_guess_rejects_above_range PASSED    [ 23%]
tests/test_game_logic.py::test_parse_guess_rejects_below_range PASSED    [ 26%]
tests/test_game_logic.py::test_parse_guess_accepts_boundary_values PASSED [ 30%]
tests/test_game_logic.py::test_invalid_input_should_not_count_as_attempt PASSED [ 33%]
tests/test_game_logic.py::test_out_of_range_should_not_count_as_attempt PASSED [ 36%]
tests/test_game_logic.py::test_valid_input_should_count_as_attempt PASSED [ 40%]
tests/test_game_logic.py::test_early_win_scores_more_than_late_win PASSED [ 43%]
tests/test_game_logic.py::test_win_score_minimum_is_10 PASSED            [ 46%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED     [ 50%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED     [ 53%]
tests/test_game_logic.py::test_win_on_attempt_1_gives_90_points PASSED   [ 56%]
tests/test_game_logic.py::test_win_on_attempt_5_gives_50_points PASSED   [ 60%]
tests/test_game_logic.py::test_easy_range PASSED                         [ 63%]
tests/test_game_logic.py::test_normal_range PASSED                       [ 66%]
tests/test_game_logic.py::test_hard_range PASSED                         [ 70%]
tests/test_game_logic.py::test_unknown_difficulty_falls_back_to_full_range PASSED [ 73%]
tests/test_game_logic.py::test_easy_secret_is_within_range PASSED        [ 76%]
tests/test_game_logic.py::test_normal_secret_is_within_range PASSED      [ 80%]
tests/test_game_logic.py::test_new_game_resets_attempts PASSED           [ 83%]
tests/test_game_logic.py::test_new_game_resets_score PASSED              [ 86%]
tests/test_game_logic.py::test_new_game_resets_status_to_playing PASSED  [ 90%]
tests/test_game_logic.py::test_new_game_resets_history PASSED            [ 93%]
tests/test_game_logic.py::test_won_status_would_block_play_without_reset PASSED [ 96%]
tests/test_game_logic.py::test_lost_status_would_block_play_without_reset PASSED [100%]

============================= 30 passed in 0.23s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
