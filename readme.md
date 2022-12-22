# Incomes-Expenses web APP

Software built in Python with the framework Flask, Hello World

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
flask --app hello run
```

# Command to execute the server live:

```
flask --app hello --debug run 
```

## Command to run the server in a different port:

```
flask --app hello run -p 5001
```

## Command to run the debug mode in the changed port:

```
flask --app hello --debug run -p 5001
```