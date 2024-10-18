import streamlit as st

# Sample paragraph with blanks (you can customize this)
paragraph = """
"1. __________ Singh or 2. ____________ Bhabhi? What should we watch today?" As per our daily ritual, we keep on getting frustrated on what to watch while eating dinner. Suddenly the doorbell rings and I open the door. Our next door neighbour 3. ____________ ji and your colleague 4. ____________ ji who lives in the house in front are at the door. Surprisingly, they are accompanied by Pramod ji's next door neighbour and the mother of 5. _________.

You are taken by surprise as they come with a 6. ____________ Chocolate cake, chicken gyozas from 7. ____________, namkeen 8. ____________, and chineese noodles from 9. ____________. Each item of food is of your liking. It is clear to you that the rest of the food, such as prawn biryani and dal baati are home-made. At any rate, they cannot be from the nearby 10. ____________ restaurant as it's kitchen seems to close absurdly early. Pramod ji also brought some chineese 11. ____________ just in case the gyozas were not similar enough to momos. People have also brought 12. ____________ vodka, one of the brands that you like. "If you want anything else, we can always go to 13. ____________ and Yeti in Croydon", says Pramod ji.

You shake your head and ask, "but why the surprise party? What's the occasion?" Pramod ji says, "We have been planning this party while keeping it a secret from you. After all it is your 14. ________ 15. ________!"

---
"""

# The correct words that the player needs to guess
correct_words = {
    1: 'Happu',
    2: 'Angoori',
    3: 'Panda',
    4: 'Pramod',
    5: 'Yashas',
    6: 'Belgian',
    7: 'Itsu',
    8: 'Rice',
    9: 'Tooting',
    10: 'Harvester',
    11: 'Dumplings',
    12: 'Absolut',
    13: 'Yak',
}

st.title("Harshda's Birthday Party")

# Instructions
st.info(
    """
    How would it have been if you had been in London for this birthday? Who knows! But here is a not too realistic imagination of what it could have been like.

    **Rules:**
    - In the paragraph below, 15 words are missing.
    - Fill in the blanks with the correct words.
    - You have to guess only the first 13 words.
    - The last two words are formed by the first letters of the other correct words.
    - Click the "Submit" button to check your answers.

    ---
    """
)


st.write("## The Story")
st.write(paragraph)

# Columns for input fields
col1, col2, col3 = st.columns(3)

# Text input for the guesses (arranged in three columns)
guesses = {}
for i in range(1, 14):
    if i % 3 == 1:
        guesses[i] = col1.text_input(f"Word {i} ({len(correct_words[i])} letters)", "")
    elif i % 3 == 2:
        guesses[i] = col2.text_input(f"Word {i} ({len(correct_words[i])} letters)", "")
    else:
        guesses[i] = col3.text_input(f"Word {i} ({len(correct_words[i])} letters)", "")

# Check if all words are guessed
if st.button('Submit'):
    correct = True
    for i, guess in guesses.items():
        if guess.lower() != correct_words[i].lower():
            st.write(f"Word {i} is incorrect. Try again!")
            correct = False
    if correct:
        st.success("Congratulations! You guessed all the words correctly.")

if st.button('Show Correct Answers'):
    st.write("## Correct Answers")
    for i in range(1, 14):
        st.write(f"Word {i}: {correct_words[i]}")
    st.write(f"Word 14: {''.join([correct_words[i][0].capitalize() for i in range(1, 6)])}")
    st.write(f"Word 15: {''.join([correct_words[i][0].title() for i in range(6, 14)])}")
