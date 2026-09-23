# Landing Page  
  
```  
┌──────────────────────────────────────────────────────────┐  
│                       StudySync                          │  
│              AI-assisted NLP study companion             │  
│                                                          │  
│                                                          │  
│  Paste your NLP course notes or study material below.    │  
│                                                          │  
│  ┌────────────────────────────────────────────────────┐  │  
│  │                                                    │  │  
│  │ Paste notes here...                                │  │  
│  │                                                    │  │  
│  │                                                    │  │  
│  └────────────────────────────────────────────────────┘  │  
│                                                          │  
│                   [ Start Studying ]                     │  
│                                                          │  
└──────────────────────────────────────────────────────────┘  
```

After clicking Start Studying, the notes should be saved in the Streamlit session so they don't have to paste them again when moving between tools.  

# Study Choice Page  
  
This essentially becomes the StudySync home screen after notes have been entered.  

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                                      NLP Study │  
├──────────────────────────────────────────────────────────┤  
│                                                          │  
│               How do you want to study?                  │  
│                                                          │  
│  ┌────────────────────┐      ┌────────────────────┐      │  
│  │    REVIEW GUIDE    │      │     FLASHCARDS     │      │  
│  │                    │      │                    │      │  
│  │ Review key ideas,  │      │ Practice terms and │      │  
│  │ concepts, and      │      │ concepts with      │      │  
│  │ definitions.       │      │ recall cards.      │      │  
│  │                    │      │                    │      │  
│  │ [ Generate Guide ] │      │[ Start Flashcards ]│      │  
│  └────────────────────┘      └────────────────────┘      │  
│                                                          │  
│  ┌────────────────────┐      ┌────────────────────┐      │  
│  │  MULTIPLE CHOICE   │      │   SHORT RESPONSE   │      │  
│  │                    │      │                    │      │  
│  │ Test yourself with │      │ Explain concepts   │      │  
│  │ questions based on │      │ in your own words. │      │  
│  │ your notes.        │      │                    │      │  
│  │                    │      │                    │      │  
│  │   [ Start Quiz ]   │      │ [ Start Practice ] │      │  
│  └────────────────────┘      └────────────────────┘      │  
│                                                          │  
│                       [ Edit Notes ]                     │  
└──────────────────────────────────────────────────────────┘  
```

Edit Notes gives the user a way back without resetting the whole app.  
  
# Review Guide  

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                                   Review Guide │  
├──────────────────────────────────────────────────────────┤  
|                                                          |  
|                 Your NLP Review Guide                    |  
|                                                          |  
|  KEY CONCEPTS                                            |  
| ────────────────────────────────────────                 |  
| Tokenization                                             |  
|    Explanation...                                        |  
|                                                          |  
| N-grams                                                  |  
|    Explanation...                                        |  
|                                                          |  
| IMPORTANT TERMS                                          |  
| ────────────────────────────────────────                 |  
| ...                                                      |  
|                                                          |  
| CONCEPT CONNECTIONS                                      |  
| ────────────────────────────────────────                 |  
| ...                                                      |  
|                                                          |  
| ────────────────────────────────────────                 |  
|                                                          |  
├──────────────────────────────────────────────────────────┤  
| Study another way:                                       |  
|                                                          |  
| [ Flashcards ]  [ Multiple Choice ]  [ Short Response ]  |  
|                                                          |  
| [ ← Study Home ]                         [ Edit Notes ]  |  
└──────────────────────────────────────────────────────────┘  
```

# Flash Cards

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                                   Flash Cards  │  
├──────────────────────────────────────────────────────────┤  
|                                             Card 3 of 12 |  
|                                                          |  
|              ┌────────────────────────────┐              |  
|              │                            │              |  
|              │       What is BPE?         │              |  
|              │                            │              |  
|              │     [ Reveal Answer ]      │              |  
|              │                            │              |  
|              └────────────────────────────┘              |  
|                                                          |  
|                    [ ← ]       [ → ]                     |  
|                                                          |  
├──────────────────────────────────────────────────────────┤  
| Study another way:                                       |  
|                                                          |  
| [ Review Guide ] [ Multiple Choice ] [ Short Response ]  |  
|                                                          |  
| [ ← Study Home ]                         [ Edit Notes ]  |  
└──────────────────────────────────────────────────────────┘  
```

# Multiple Choice

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                               Multiple Choice  │  
├──────────────────────────────────────────────────────────┤  
|                                         Question 3 of 12 |  
|                                                          |  
| Which statement best describes tokenization?             |  
|                                                          |  
|     ○ Answer A                                           |  
|     ○ Answer B                                           |  
|     ○ Answer C                                           |  
|     ○ Answer D                                           |  
|                                                          |  
|                    [ Submit Answer ]                     |  
|                                                          |  
|       ────────────────────────────────────────────       |  
|                                                          |  
| Feedback appears here after submission.                  |  
|                                                          |  
|    Correct!                                              |  
|        Explanation...                                    |  
|                                                          |  
|                   [ Next Question → ]                    |  
|                                                          |  
|                                                          |  
├──────────────────────────────────────────────────────────┤   
| Study another way:                                       |  
|                                                          |  
|  [ Review Guide ]  [ Flashcards ]  [ Short Response  ]   |  
|                                                          |  
|  [ ← Study Home ]                       [ Edit Notes ]   |  
└──────────────────────────────────────────────────────────┘  
```

# Short Response

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                                Short Response  │  
├──────────────────────────────────────────────────────────┤  
|                                         Question 3 of 12 |  
|                                                          |  
| Explain why smoothing is used in an n-gram               |  
| language model.                                          |  
|                                                          |  
|     ┌─────────────────────────────────────────────┐      |  
|     │ Type your response...                       │      |  
|     │                                             │      |  
|     └─────────────────────────────────────────────┘      |  
|                                                          |  
|                    [ Submit Response ]                   |  
|                                                          |  
|      ─────────────────────────────────────────────       |  
|                                                          |  
|  Feedback                                                |  
|                                                          |  
|  You identified the main problem correctly...            |  
|                                                          |  
|    Consider what happens when the model encounters       |  
|    an n-gram that did not appear in the training data.   |  
|                                                          |  
|         [ Give Me a Hint ]          [ Try Again ]        |  
|                                                          |  
|                   [ Show Explanation ]                   |  
|                                                          |  
├──────────────────────────────────────────────────────────┤  
| Study another way:                                       |  
|                                                          |  
|  [ Review Guide ]  [ Flashcards ]  [ Multiple Choice ]   |  
|                                                          |  
|  [ ← Study Home ]                       [ Edit Notes ]   |  
└──────────────────────────────────────────────────────────┘  
```

# Results
Instead of a separate Session Summary page, Multiple Choice and Short Response can each end with a small results state:

```
┌──────────────────────────────────────────────────────────┐  
│ StudySync                             Practice Complete  │  
├──────────────────────────────────────────────────────────┤  
|                                                          |  
|                                                          |  
|         8 / 10 Questions Completed Successfully          |  
|                                                          |  
|  You did well with:                                      |  
|      • Tokenization                                      |  
|      • N-grams                                           |  
|                                                          |  
|  Consider reviewing:                                     |  
|      • Smoothing                                         |  
|      • Perplexity                                        |  
|                                                          |  
|     [ Review These Concepts ]  [ Try More Questions ]    |  
|                                                          |  
├──────────────────────────────────────────────────────────┤  
| Study another way:                                       |  
|                                                          |  
|  [ Review Guide ]  [ Flashcards ]  [ Other Choice ]      |  
|                                                          |  
|  [ ← Study Home ]                       [ Edit Notes ]   |  
└──────────────────────────────────────────────────────────┘  
```
