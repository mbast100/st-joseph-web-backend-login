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
      <ul>
        <li><a href="#architecture-diagram">Architecture Diagram</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#dev-environment">Dev Environment</a></li>
        <li><a href="#deploying-to-aws">Deploying to AWS</a></li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#dynamodb">DynamoDB</a></li>
      </ul>
    </li>
     <li>
      <a href="#usage">Usage</a>
      <ul>
        <li>
          <a href="#sample-payloads">Sample Payloads</a>
            <ul>
              <li>
                <a href="#user-api">User API</a>
                <ul>
                  <li><a href="#post">POST</a></li>
                  <li><a href="#put">PUT</a></li>
                </ul>
              </li>
            </ul>
        </li>
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
* [JWT](https://jwt.io/introduction/)
* [PyTest](https://docs.pytest.org/en/stable/)
* [AWS](https://docs.aws.amazon.com)
  * [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
  * [AWS Lambda](https://aws.amazon.com/lambda/)
  * [AWS SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
  * [AWS Amplify](https://aws.amazon.com/amplify/)


### Architecture Diagram

Below is a diagram describing the architecture structure of the entire St Joseph web app.

![alt text](Diagram.png?raw=true)




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The `requirements.txt` file contains all the necessary frameworks and libraries. To download the prerequisites, run the following command (uses `pip`):

`pip install -r requirements.txt`
  
To update the requirements when installing new packages, run:

`pip freeze > requirements.txt`
  
### Dev Environment
- `python -v` 3.7 or greater
- AWS CLI [(version 1)](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)
- To clone the repo: `git clone https://github.com/shahirmikhail/shopify-image-repo.git`
- Change the current working directory to the local project root and run (only required for the first time):
    - Mac: `python3 -m venv venv`
    - Windows: `python -m venv venv`
- To start the virtual environment:
    - Mac: `source venv\bin\activate`
    - Windows: `source venv\scripts\activate`
- To run the app: `python app.py`


### Deploying to AWS

To deploy the lambda functions to AWS, run the follwoing commands:

- `zappa deploy`
- `zappa update`

### Testing

To run the tests in prod, use:

`pytest tests/routes/test_prod_login.py -s`

### DynamoDB

To scan all the users in the database, use the following command on the AWS CLI:

`aws dynamodb scan --table-name users`


<!-- USAGE EXAMPLES -->
## Usage

### Sample Payloads

#### User API

##### POST

Below is an example of a payload that the API whould take for the POST operation:

```sh
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@gmail.com",
  "role": "admin",
  "password": "SuperMan123!"
}
```

##### PUT

Below is an example of a payload that the API whould take for the PUT operation:

```sh
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@gmail.com",
  "role": "admin",
  "password": "SuperMan123!",
  "id": "23ca88b3-84ef-42be-9dd6-efb7426ec500"
}
```


<!-- CONTACT -->
## Contact

Mark Bastawros - [LinkedIn](https://www.linkedin.com/in/mark-bastawros-1ba081178) - mbast.amin97@gmail.com

Shahir Mikhail - [LinkedIn](https://linkedin.com/in/shahirmikhail) - shahir.mikhail@gmail.com


