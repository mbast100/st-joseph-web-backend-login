# Authorization API


This project is being developed for St Joseph's web application.

The Authorization API is a Flask REST API which allows the user to authorize clients. It also allows the user to post, retrieve, modify and delete users in the database.


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#dev-environment">Dev Environment</a></li>
      </ul>
    </li>
     <li>
      <a href="#usage">Usage</a>
      <ul>
        <li>
          <a href="#sample-payloads">Sample Payloads</a>
            <ul>
              <li><a href="#post">POST</a></li>
              <li><a href="#put">PUT</a></li>
            </ul>
        </li>
        <li><a href="#validation">Validation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

Listed below are the frameworks and database used for this project.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
* [PyTest](https://docs.pytest.org/en/stable/)


### Architecture Diagram





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The `requirements.txt` file contains all the necessary frameworks and libraries. To download the prerequisites, run the following command (uses `pip`):
  ```sh
  pip install -r requirements.txt
  ```
  
### Dev Environment
- `python -v` 3.7 or greater
- To clone the repo: `git clone https://github.com/shahirmikhail/shopify-image-repo.git`
- Change the current working directory to the local project root and run (only required for the first time):
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- To start the virtual environment:
    - Mac: `source venv\bin\activate`
    - Windows: `source venv\scripts\activate`

<!-- USAGE EXAMPLES -->
## Usage

### Sample Payloads

#### POST

Below is an example of a payload that the repo whould take for the POST operation:

```sh
{
  "extension": "JPEG",
  "name": "Cute Dog",
  "owner": "Shahir Mikhail",
  "size": "300 KB",
  "url": "https://picsum.photos/id/237/200/300"
}
```

#### PUT

Below is an example of a payload that the repo whould take for the PUT operation:

```sh
{
  "extension": "JPEG",
  "id": "b2efff0a-38d6-4b02-8060-e7a0c03c0591",
  "name": "Cute Dog",
  "owner": "Shahir Mikhail",
  "size": "300 KB",
  "url": "https://picsum.photos/id/237/200/300"
}
```


### Validation

`extension`
- Mandatory field
- Must be one of the following (case sensitive): JPEG, JPG, PNG, GIF, TIFF, PSD, PDF, EPS, AI, INDD or RAW

`name`
- Mandatory field
- Must be alphanumeric
- Must have a minimum of 5 and a maximum of 37 characters

`owner`
- Mandatory field
- Must be alphanumeric
- Must have a minimum of 5 and a maximum of 37 characters

`size`
- Mandatory field
- Must have the following format: '### {KB, MB, GB or TB}'
- See the sample payloads for an example

`url`
- Mandatory field


<!-- CONTACT -->
## Contact

Shahir Mikhail - [LinkedIn](https://linkedin.com/in/shahirmikhail) - shahir.mikhail@gmail.com









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

