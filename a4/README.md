## Part 1

In this part, we will train a word2vec model, then use it to (hopefully) improve the named-entity classifier from A3.
You will have to modify a4.py to accomplish the instructions below. You may use your solution to A3 as a starting point.

**Output should be written to output1.txt**

1. Install [gensim](https://radimrehurek.com/gensim/) using `pip install gensim`.
2. Install [nltk](http://www.nltk.org/) using `pip install nltk`.
3. Download the Brown Corpus, a collection of news articles.
  - From a python shell, do:
  ```
  import nltk
  nltk.download('brown')
  ```
4. Read the word2vec gensim documentation [here](https://radimrehurek.com/gensim/models/word2vec.html)
5. Train a word2vec model on the sentences from the Brown corpus.
  - Use `size=50`, `window=5`, and `min_count=5`
6. Modify your make_feature_dicts method from a3 to have:
  - an additional parameter w2v_model, which will store the... word2vec model you trained.
  - an additional parameter w2v, which is a boolean, that is True if we are to add the w2v features
  - For each token in the input, if w2v==True, you will add 50 new feature from the word2vec model.
    - E.g., one feature key may be 'w2v_6', and its value may be 2.6, indicating that the 6th w2v dimension has value 2.6 for this token.
  - Allow the word2vec features to be combined with the context features as well (so, you could have a feature like 'prev_w2v_6' = 2.6.
7. Modify evaluate_combinations to take in the word2vec model. Re-run all combinations and report the final results.
8. Store the output of evaluate_combinations in a file called `output1.txt`.


## Part 2: Bonus (15 pts)

Use TensorFlow to implement a Recurrent Neural Network for the Named Entity Recognition problem.  
**Your code will go in rnn.py. The output of your program should be written to output2.txt.**

Using the same data as the above, train a Recurrent Neural Network.
- Use dimension 20 for the hidden layer of each state
- Use cross-entropy as the loss function
- Use the logistic function as the activation function for the hidden state, and use softmax to product the output for each time step.
- Other than that, you are free to use any parameter settings you like to optimize the model.

You may find it helpful to go through the tensorflow tutorial here:
https://www.tensorflow.org/tutorials/recurrent
