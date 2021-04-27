# News-Analyzer
## Three modules:
- Secure file uploader module (entity-based)
- NLP analysis module (procedure-based)
- News feed ingester module (entity-based)
## My demo 
### My demo video
- Google Drive link [here](https://drive.google.com/file/d/1Kc8j8ljy9FM-fWYw16gFejVrgXa7JaX9/view?usp=sharing)
- preview gifs 

![preview0](https://user-images.githubusercontent.com/77998865/114019864-8137b380-98a1-11eb-8522-a18ff64a5309.gif)

![preview1](https://user-images.githubusercontent.com/77998865/114019889-8694fe00-98a1-11eb-95af-09e34001bf1f.gif)

![preview2](https://user-images.githubusercontent.com/77998865/114019914-8eed3900-98a1-11eb-8b71-324ba022d119.gif)

### My Demo
- Secure file uploader module [here](https://github.com/dongfang98/News-Analyzer/tree/main/analyser/Uploader)
- NLP analysis module [here](https://github.com/dongfang98/News-Analyzer/tree/main/analyser/NLPAnalysis)
- News feed ingester module [here](https://github.com/dongfang98/News-Analyzer/tree/main/analyser/NewsIngester)
## Install the .whl file and run the application
Install the analyser-1.0.0-py3-none-any.whl file in the directory.

    $ pip install analyser-1.0.0-py3-none-any.whl
Run the application:

    $ export FLASK_APP=analyser
    $ export FLASK_ENV=development
    $ flask run
You can see the following output.

    * Serving Flask app "analyser"
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 855-212-761
Initialize the database with `init-db`

    $ flask init-db
