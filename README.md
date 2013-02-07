# AI-Bot - API

***

## Pick a word

* **URL**
   <br>`/api/1/ai-bots/pick_a_word`

* **Method**
   <br>`POST`

* **URL Params**
   <br>**Required:** `level=[int], word=[dictionary]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'word_id': "AB123", 'letters' : ['g','r','o','i','n','d','i','r','k','t','e','n','n','i','s']}`

## Guess a word

* **URL**
   <br>`/api/1/ai-bots/guess_a_word`

* **Method**
   <br>`POST`

* **URL Params**
   <br>**Required:** `game=[game object], word=[dictionary]`

* **Success Response:**
    <br> **Code:** 200
    <br> **Content:**
      <br> `{'attempted_words': [list of word ids]}`
