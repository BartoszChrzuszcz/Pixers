# Pixers
QA task for Pixers
# Used tools and technologies:
- Python 3.7.1
- PyCharm Community
- Selenium Webdriver
- chromedriver in the newest version
# Brief Description
- You will need to download chromedriver.exe and paste it in the project directory 
- after opening code in PyCharm some packages can be requried to download if you do not have them allready (e.g. unittests)
- tests were written for Chrome webbrowser
- tests checks if there is only one product added to cart and if the price from items list is the same as the price on the item card site
- correct_price_test.py is for price test and product_addition_test.py is for one item in cart test
- you can run both of them by running code in testsuite_all_tests.py
# Possible upgrades
- the item quantity is received in JSON on the card page, however the requested url is dynamic and consist of ID that is added on the end of it. Right know without knowledge how this ID is being made the check the item quantity is made by using selectors. ID looks like timestamp is converted to integer but it also have got some more numbers.
- considering adding Allure to produce reports after test runs 
