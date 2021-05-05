# News-Analyzer
## My demo 
### My demo video
- Google Drive link [here](https://drive.google.com/file/d/1MYj2SxRJNxqYkmFEwSTnIoJqbfsVTire/view?usp=sharing)
- preview gif 

![preview0](https://user-images.githubusercontent.com/77998865/114019864-8137b380-98a1-11eb-8522-a18ff64a5309.gif)

## Functionalities implemented:
- Secure file upload
    - Secure Upload
        - All users must be registered and logged in
        - User login is required for any operation involving database
    - Support for pdf file uploads
        - Enables users to upload pdf files and store the content in database
    - View data
        - Users can see the content of their own uploaded files, but cannot see others'
    - Support to modify article content and title
        - Click **Edit** to modify
- NLP analysis
    - Text Sentiment Analysis
        - Import `nltk` to perform sentiment analysis on the text content of the article
    - Keyword acquisition
        - Get the keywords for the text content of the article and find the keyword in the paragraphs
    - Text sentiment and keyword (and keyword positions in the article) display
        - The text sentiment and keyword are displayed in the web page, so I do not have to keep running the functions
        - Also, the keyword positions in the article are shown in web page
- News feed ingest
    - Search for a specified number of news articles based on keywords
    - Store these articles in the database and display them on the webpage
        - Users can subsequently manipulate these articles, such as modifying and deleting
- News Search in existing database
    - Search news articles in existing database based on **keyword** and **sentiment**
    - The search result as well as the corresponding information (like keyword, author, etc.) are shown in a new web page
## Run the application
Run the application in development mode:

    $ export FLASK_APP=analyzer
    $ export FLASK_ENV=development
    $ flask run
You can see the following output.

    * Serving Flask app "analyzer"
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 855-212-761
Initialize the database with `init-db`

    $ flask init-db
