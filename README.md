# LOGIN API ST-Joseph

## requirements 
- set up AWS cli (version 1) https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html
- python 3.7 or higher


## setup dev env
- clone repo
- cd project root & run `python3 -m venv venv`
- run `source venv\bin\activate`
- `pip install -r requirements.txt`
- then `python app.py`

## AWS 

- from command line run : `aws dynamodb scan --table-name users`
should return content of users table

