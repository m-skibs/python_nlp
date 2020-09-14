# python_nlp
Takes in a string and returns ten related words.

This project leverages spaCy and the NLTK WordNet. To run, first [install spaCy](https://spacy.io/usage) [and NLTK](http://www.nltk.org/install.html)
Then refer to spaCy's documentation to [install the model for the language you want to use](https://spacy.io/models).

If you are not using English, besides loading the appropriate module, inside the calls to `.lemma_names()` you will need to write `lang="XXX"` replacing "XXX" with a three-letter code for the desired language. A cheat sheet of the codes [can be found here](http://compling.hss.ntu.edu.sg/omw/)

Navigate to the directory of this project and enter your desired string as the value for `text` on line 8 of `words.py`run the command `python words.py`
