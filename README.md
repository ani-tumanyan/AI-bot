# AI-Bot - API

***

## Pick a word

* **URL**
   <br>`/api/1/ai-bots/pick_a_word`

* **Method**
   <br>`POST`

* **URL Params**
   <br>**Required:** `level=[int], words=[dictionary]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'word_id': "AB123", 'letters' : ['g','r','o','i','n','d','i','r','k','t','e','n','n','i','s']}`

### Get word's length

* **URL**
   <br>`/api/1/ai-bots/get_word_length`

* **Method**
   <br>`GET`

* **URL Params**
   <br>**Required:** `level=[int], maxLength=[int]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'wordLength': [int]}`

* An example of the function defining the length of the word
   <br> `wordLength = (maxLength - 2) / sqrt(level) + 1;`

## Guess the Word

* **URL**
   <br>`/api/1/ai-bots/guess_a_word`

* **Method**
   <br>`POST`

* **URL Params**
   <br>**Required:** `game=[game object], words=[dictionary]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'attempted_words': [list of word ids]}`

### Get the number of the guessed words by Robot

* **URL**
   <br>`/api/1/ai-bots/get_word_number`

* **Method**
   <br>`GET`

* **URL Params**
   <br>**Required:** `level=[int], maxNumber=[int]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'wordNumber': [int]}`

* An example of the function defining the number of the word
   <br> `wordLength = rand(1, max(maxNumber - level, 1));`
