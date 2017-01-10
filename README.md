## Instructions for submitting assignments

By the end of the second week of class, each student should have their own private GitHub repository at:  
<https://github.com/iit-cs585/[your-github-id]>

This is where you will submit all assignments. You should clone this repository to your local machine with

`git clone https://github.com/iit-cs585/[github-username].git`

substituting your actual github username for [github-username]

Your repository should already contain starter code for each assignment. This starter code has been pulled from the assignment repository at <https://github.com/iit-cs585/assignments>.

Throughout the course, I may update the assignments to clarify questions or add content. To ensure you have the latest content, you can run the `update.sh`, which will fetch and merge the content from the assignments repository.

For each assignment, then, you should do the following:

1. Run `./update.sh` to get the latest starter code. (On unix-like machines, you may need to run `chmod a+x` to make the file executable). If you have trouble running this script, you can just run the git commands yourself:
  ```
  git remote add template https://github.com/iit-cs585/assignments
  git fetch template
  git merge template/master
  ```

2. Do the homework, adding and modifying files in the assignment directory. **Commit and push often!** Nothing will be graded until after the deadline, so this is a good practice to backup your work and also timestamp partial solutions.

3. Before the deadline, push all of your changes to GitHub. E.g.:
  ```
  cd a1
  git add *
  git commit -m 'homework completed'
  git push
  ```

4. Double-check that you don't have any outstanding changes to commit:
  ```
  git status
  # On branch master
  nothing to commit, working directory clean
  ```

5. Double-check that everything works, by cloning your repository into a new directory and executing all tests.
  ```
  cd 
  mkdir tmp
  cd tmp
  git clone https://github.com/iit-cs585/[your_iit_id]
  cd [your_iit_id]/a1
  [...run any relevant scripts/tests]
  ```

6. You can also view your code on Github with a web browser to make sure all your code has been submitted.

7. Assignments contain [unit tests](http://docs.python-guide.org/en/latest/writing/tests/) to test your code. (E.g., in assignment 1, see the file [a1_test.py](https://github.com/iit-cs585/assignments/blob/master/a1/a1_test.py)). You should ensure that your code passes all test by running `python a1_test.py`. **N.b. Passing all tests is necessary, but not sufficient, for receiving full marks.**

8. Typically, each assignment contains a number of methods for you to complete. I recommend tackling these one at a time, debugging and testing, and then moving onto the next method. Implementing everything and then running at the end will likely result in many errors that can be difficult to track down. In order to run the test from a single function, you can pass an extra argument to the test command. E.g., to run only the test `test_baa_fsa` in `a1.py`, you would call:
  - `python a1_test.py TestA1.test_baa_fsa`
