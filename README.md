# News-Analyzer
Three modules:
-  Secure file uploader module
-  NLP analysis module
- News feed ingester module
## Secure file uploader module
A entity-based module.
### User stories
- I, an investigator / journalist, want to upload a file to my account on a remote server. 
- I, an investigator / journalist, want to be able to store metadata and access metadata for each file I store. 
- I, an investigator / journalist, will have a wide array of data types so I want to be able to upload a wide array of data types.
- I, an investigator / journalist, will want this system to be secure.
## NLP analysis module
A procedure-based module.
### User stories
- I, an investigator / journalist, want to be able to run functions that will analyze the text / image data on my stored data (locally or server side). 
- I , an investigator / journalist, want to be able to this analyzed information, so I do not have to keep running the functions.
## News feed ingester module
A entity-based module
### User stories
- I, an investigator / journalist , want to be able to ingest a large variety of file types and convert them into uploadable files. These uploadable files consist of json files that list the metadata in an accessible format, and a location that the data will be stored. 
- I, an investigator / journalist, want to be able to create a custom metadata entry, if my file type is not supported by the functions that automatically ingest metadata.
## My Demo and My Tests
- Secure file uploader module [here](https://github.com/BUEC500C1/news-analyzer-HaoranZ99/tree/main/analyser/Uploader/README.md)
- NLP analysis module [here](https://github.com/BUEC500C1/news-analyzer-HaoranZ99/tree/main/analyser/NLPAnalysis/README.md)
- News feed ingester module [here](https://github.com/BUEC500C1/news-analyzer-HaoranZ99/tree/main/analyser/NewsIngester/README.md)
- My tests [here](https://github.com/BUEC500C1/news-analyzer-HaoranZ99/tree/main/test)
## install the .whl file and run the application
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
