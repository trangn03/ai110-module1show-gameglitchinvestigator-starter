# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  When running the game for the first time, the game instruction got straight on point and easy to understand. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  At the start I notice that: 
  - When starting the game for the first time, I didn't submit anything but there is already 1 attempt counted. It shows 8 attempts on the left but however only 7 attempts allow in the center of the screen
  - In the submission it said press enter to apply but when Enter button pressed, the number didn't get submit 
  - After submitting the first guess, the game did not update the attempt, which is still show 7 on the screen
  - Once done, the score result in negative number 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess 4. Secret number 11 | Go higher | Go lower | None |
|Guess 92. Secret number 7 | Go lower | Go higher | None |
|Press New game button | The game refresh and user can guess the number | The game froze eventhough the screen displays "Game over. Start a new game to try again" | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude through VS Code chat feature to help me debug. I let it read through the whole codebase ```app.py```, ```logic_utils.py```, and the test file to see what happen with the code and diagnose the problems
  
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggested me on attempt that when the game begin on ```st.session_state.attemps``` which it set the counter starts at 1, so the first guess is recorded as attempt #2 and it should be initialize to 0. I read through the code to verify and test the game before I change the code. After apply what AI suggested me, I saw that the first attempt was set to 8 instead of 7. 
  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI suggested me on change the mode "Hard" range to 1000 in ```get_range_for_difficulty``` but it is not necessary because the prompt given to guess between 1 and 100. And also while it changed the number to 1000, it would be still apply only for the UI but not in the hardcoded logic so it would be still follow the original range.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decide whether a bug was fixed by applying both manual testing on the website and using ```pytest```.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - filling
- Did AI help you design or understand any tests? How?
  - filling

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Everytime a user clicks a button or change the input, Streamlit reruns the entire Python script. So when the secret number got generated like ```secret = random.randint(1,100)```, it get a brand new value on every single click. So if you want it to retained all of the secret number, you have to use ```st.session_state``` so it would keep a memory Streamlit data while the script restarts like guess history or your score. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
This could be a testing habit, a prompting strategy, or a way you used Git.
  - One habit that I could reuse for the future projects is that always read through the code to see how the script function then manually test the code at first look so I would understand what the project is about.  
- What is one thing you would do differently next time you work with AI on a coding task?
  - One thing I would do differently next time is rather than just prompt the AI "Fix the code for me" for the whole codebase, which it can lead to misleading details or making assumptions. I would break the code down into sections then give the prompt to be more specific so the AI would observed more information and give better result. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project shows me that the AI can analyze and point out the bugs rapidly even the code executed fine in the terminal. However, AI can make mistake so human still need to check everything before pushing the code into production stage. The AI acts as a helpful assistant whenever I need an overall review to catch small things that I might have missed.