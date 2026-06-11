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
  - I used Claude through VS Code chat feature to help me debug and see what is wrong with the code
  
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggested me a
  
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI suggested wrong on

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - filling
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - filling
- Did AI help you design or understand any tests? How?
  - filling

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - fill here

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
This could be a testing habit, a prompting strategy, or a way you used Git.
  - fill here
- What is one thing you would do differently next time you work with AI on a coding task?
  - fill here
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It depends on what model that you use for the AI. It helpful when it shows you the error that present in the code and acts as the guide ... 