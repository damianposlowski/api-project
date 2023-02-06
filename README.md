This is a project to develop an API from scratch using Python, FastAPI and PostgreSQL. The project is written and executed on a virtual environment, using Python version 3.10.6

To test the API functions I used Postman. To validate the data schema I used pydantic.


To run the FastAPI server, enter in the command line:
$ uvicorn app.main:app --reload

After starting the server you can access the app documentation, by going to:
http://127.0.0.1:8000/docs