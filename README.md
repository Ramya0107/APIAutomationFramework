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

### Intsall pip Packages
- `pip install requests pytest pytest-html faker allure-pytest jsonschema`
- `pip install requirement.txt`

### How to run locally and generate simple report
`pytest -s -v --html=report.html`

### How to Run via Jenkins?


