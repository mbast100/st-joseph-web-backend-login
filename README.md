# LOGIN API ST-Joseph

## Requirements 
- set up AWS cli (version 1) https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html
- python 3.7 or higher


## Setup dev env
- clone repo
- cd project root & run:
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- start virtual env:
    - Mac: `source venv\bin\activate`
    - Windows: `source venv\scripts\activate`
- Install requirements: `pip install -r requirements.txt`
- Run app: `python app.py`

## AWS 

- from command line run : `aws dynamodb scan --table-name users`
should return content of users table.


## Update requirements.txt

- Install: `pip install ...`
- Update: `pip freeze > requirements.txt`

## Deploying to AWS

- zappa deploy
- zappa update

## Testing

- test login api in prod: `pytest tests/routes/test_prod_login.py -s`

