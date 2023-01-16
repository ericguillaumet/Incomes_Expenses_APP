# Incomes-Expenses web APP

Software for tracking Incomes and Expenses built in Python with the Flask framework and Jinja engine

## Install

- In the Python environment, execute command:

```
pip install -r requirements.txt
```

The used libraries: https://flask.palletsprojects.com/en/2.2.x/

## Execution of the Software

- Run the Flask server introducing these commands to the terminal:
    - iOS: ```export FLASK_APP=hello.py```
    - Windows: ```set FLASK_APP=hello.py```

## Another option would be to create the hidden directory .env and add the following lines:

- FLASK_APP=main.py
- FLASK_DEBUG=True

## Command to execute the server:

```
flask --app main run
```

# Command to execute the server live:

```
flask --app main --debug run 
```

## Command to run the server in a different port:

```
flask --app main run -p 5001
```

## Command to run the debug mode in the changed port:

```
flask --app main --debug run -p 5001
```