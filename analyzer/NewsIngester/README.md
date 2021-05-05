# News feed ingester module
A entity-based module
## User stories
- I, an investigator / journalist , want to be able to ingest a large variety of file types and convert them into uploadable files. These uploadable files consist of json files that list the metadata in an accessible format, and a location that the data will be stored. 
- I, an investigator / journalist, want to be able to create a custom metadata entry, if my file type is not supported by the functions that automatically ingest metadata.
## Functionalities Implemented
- Search for a specified number of news articles based on keywords
- Store these articles in the database and display them on the web
	- Users can subsequently manipulate these articles, such as modifying and deleting