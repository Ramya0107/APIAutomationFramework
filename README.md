# Python API Automation Framework

## Integrations Test Cases for the Restful Booker
URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PATCH, DELETE, PUT
2. Response Body, Headers, Status Code
3. Auth - Basic Auth, Cookie Based Auth
4. JSON schema validation


### Tech Stack (Python packages used)
1. Python, Request Module
2. 2.PyTest, PyTest-html
3. Allure Report
4. Faker, CSV, JSON, YML
5. Run via commandLine - Jenkins

#### P.S - DB Connection possible(in future)

### Install pip Packages
- `pip install requests pytest pytest-html faker allure-pytest jsonschema`
- `pip install requirement.txt`

### How to run locally and generate simple report
`pytest -s -v --html=report.html`

#### If module error, use below cmd to execute the script
`python -m pytest -s -v`

### Concepts
- dotenv file usage, readJSON
`pip install python-dotenv`

### How to run parallel test
- Step1: pip install pytest-xdist
- Step2: use below cmd to execute the script in parallel. 
- Path - tests/integration_test/parallel_test
- -n auto - runs the tests by using separate workers for each function. This is faster, since it distribute tests across multiple CPU's to speed up test execution. 
`pytest -n auto tests/integration_test/parallel_test -s -v`
- -n 2 - takes up 2 random function 1st and execute then takes up another 2 random functions
`pytest -n 2 tests/integration_test/parallel_test -s -v`

#### If module error, use below cmd to execute the script
`python -m pytest -n auto tests/integration_test/ -s -v --html=report.html`

### How to generate allure report?
- Step1: Install node.js in the system - this will install npm (node package manager)
- Step2: `open cmd -> check node --version`, if available Install allure-commandline which is a package manager by using npm
`npm i -g allure-commandline` which helps to generate a report.
- Step3: pycharm terminal - `pip install allure-pytest`
- Step4: Mark the test cases with annotations like 
  @allure.feature()
  @allure.story()

### How to run locally and generate allure report
- sample cmd for allure report
`python -m pytest tests/integration_test -s -v --alluredir=./reports`
- To open the allure report
`allure serve ./reports`



