# Automated Software Testing for [the-internet](https://the-internet.herokuapp.com/)
This repository contains automated software tests for the-internet, a demo web application commonly used for simple element interactions. This project utilises **Selenium WebDriver**, **Pytest**, and **Allure** for structured execution and reporting.

## Deployment
1. Clone the Repository
```
git clone https://github.com/sofiaamihan/the-internet.git
```
2. Set up a Virtual Environment
```
python3.9 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Running Tests
```
pytest -vv -n=3 --alluredir allure-results
```
5. Generate Allure Reports
```
allure serve allure-results
```

## Results
![Results]()
