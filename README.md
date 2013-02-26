MAIN FUNCTIONS
------------------

* **Generate a new game<br>**
    * **URL:**         /api/1/api-bots/generate_a_game<br>
    * **Method:**	     POST<br>
    * **URL Params:**  level=[int]<br>
    * **Response:**    {word: "some word", letters: [list of some letters]}<br><br>

    * **Implementation**
        - Gets the length of the word that is suitable to the current user with "level" experience. Here we call "get_word_length" utility function.
        - Gets a word from the dictionary that satisfies the required length. Here we call "get_word_by_length" utility function.
        - (Optional) Makes sure that we haven't provided that word to the same user before.
        - Now when we have the word for the user, we would also need to generate a list of letters for the game. This list will contain all the letters from the word + additional letters. We make a call to generate_letter_list utility function.
        - Returns a JSON object, which includes the word and the list of letters!

-----------
* **Guess the word<br>**
  * **URL:**          /api/1/api-bots/guess_word<br>
  * **Method:**	      GET<br>
  * **URL Params:**   level=[int], word=[string], letters=[list of letters]<br>
  * **Response:**     ["attemp1", "attemp2", …]<br><br>

  * **Implementation**
     - Gets the number of mistaken attempt that the Robot should make before guessing the actual word. We call get_attempts_number utility function.
     - Now we have some number of attempts that we want to generate before guessing the actual word. 
         - If the number is 0, then we have an ACE, so we add the correct word to the final resulting list and return that array.
         - If the number is greater than 0, then we would need to generate some words.

     - 1. Generates a word from the letters list by calling generate_word utility function. We add this word to the final resulting list.
     - 2. Checks the match between the actual and guess words by calling compare_words. If the "is_correct" is true, then we were lucky and we have guessed the word by chance. So we  return the list. Otherwise we go to step 1 passing the "result" string for the generate_word function. 
     - We continue these steps "attempt_number" times. When we are done that much attempts, we add the correct word to the list and pass that list back.

----------

UTILITY FUNCTIONS
--------------------

* **Get word's length<br>**
  * **URL:**         /api/1/api-bots/get_word_length<br>
  * **Method:**	     GET<br>
  * **URL Params:**  level=[int]<br>
  * **Response:**    {word_length: [int]}<br><br>

  * **Implementation**
      * This function gets the user experience level and using a mathematical function gets the length of a word that would be suitable in this case. Here is the function`<br>

              - number 	      = (maxLength - 1)/sqrt(level) + 1<br>
              - offset 	      = rand(0, someNumber)<br>
              - wordLength    = rand(max(2, number - offset), min(maxLength, number + offset))<br><br>
	

       * This function will return some number between 2 and maxLength depending on the "level". "maxLength" is a constant defined by our system. If the user is more experienced then the function will return smaller number, hence the word would be shorter. (Right now this is the distinction between a novice and experienced users. We assume that it would be more challenging to guess a shorter word than a longer ones.)<br>

******************************************************************************************

* **Get a word by word length<br>**
  * **URL:**            /api/1/api-bots/get_word_by_length<br>
  * **Method:**	        GET<br>
  * **URL Params:**	length=[int]<br>
  * **Response:**	{word: "some word"}<br><br>

  * **Implementation**
     - Makes a SQL query with LENGTH() function and returns a word. The important concept here is to shuffle the words, so we don't get the same word over and over.

_This function needs to be defined in the "Dictionary" class_<br>
******************************************************************************************

* **Generate Letter List<br>**
  * **URL:**		/api/1/api-bots/generate_letter_list<br>
  * **Method:**	        GET<br>
  * **URL Params:**	existing_letters=[list of letters]<br>
  * **Response:**	{letters: [complete list of letters]}<br><br>

  * **Implementation:**
      - Gets the list of the words and adds additional letters keeping the proportion of vowels and consonants. <br>

******************************************************************************************

* **Get the number of attempts**
  * **URL:**		/api/1/api-bots/get_attempts_number
  * **Method:**	        GET
  * **URL Params:**	level=[int]
  * **Response:**	{attempt_number: [int]}<br><br>

  * **Implementation**
       * This function gets the user experience level and using some mathematical functions gets the number of the attempts that should be hypothetically made by Robot<br>

            - number 	   = (maxAttempts - 1)/sqrt(level) + 1<br>
            - offset 	   = rand(0, someNumber)<br>
            - attemptNumber  = rand(max(0, number - offset), min(maxAttempts, number + offset))<br><br>

	* This function will return some number between 0 and maxAttempts depending on the "level". "maxAttempts" is a constant defined by our system. If the user is more experienced then the function will return smaller number, hence the Robot will be able to guess the word in fewer steps.

******************************************************************************************

* **Generates a word from the letters list<br>**
  * **URL:**		/api/1/api-bots/generate_word  <br>
  * **Method:**	        GET<br>
  * **URL params:**	letters=[list of letters], wordLength=[int], word_result=[array]<br>
  * **Response: **	{word: "some word"}<br><br>

  * **Implementation**
     - When the "word_result" is empty or null, then we just pick "wordLength" letters from letters list and generate a word.
     - When we have a "word_result" array, then we keep the correct letters in their positions. We take the letters that has "2" value, which means they are correct but their position is not correct. We change their positions in the word. And finally we eliminate wrong letters from "letters" list and pick the rest of the letters to generate the letter.

******************************************************************************************

* **Compare two words<br>**
  * **URL:**		/api/1/api-bots/compare_words<br>
  * **Method:**	        GET<br>
  * **URL Params:**	correctWord=[string], guessWord=[string]<br>
  * **Response:**	{is_correct:[boolean], word_result :["b" : 0, "a" : "1", "i" : "2" …]}<br>

     Where the "result" is a number sequence, which has the same length as the guessed word and can contain 0, 1, and 2. 0 means that the letter at that position is completely wrong. 1 means that the letter at that position is correct. 2 means that the letter exists in the word, but the position is wrong.<br><br>

  * **Implementation**
     - This function first compares the two words:
        - If the words are the same then we return {is_correct: True, word_result: ["b" : 1, "a" : "1", "i" : "1" ...]}.
        - If the words don't match, then we compare the characters for the guess word and the correct word one by one. We keep the letters of the correct word in a separate array. We check to see if the first letters of correct and guessing words match. If they match, then we remove that letter from the list, add an element to our word_result array with the letter key and value "1". Otherwise we check to see if the letter from the guessing word contains in the letter array. If it contains then we again remove that letter from the list, then add an element to the word_result with "letter" : 2. Finally, if the array doesn't contain that letter, then we just add "letter" : 0 to the word_result array.

The separate list of correct word letters is for avoiding repetitions and other problems, which can occur during comparison.




