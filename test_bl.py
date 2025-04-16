import pytest
import allure
import bl

@allure.title("Test 1 is a prime ")
@allure.description("This test attempts to test wether 7 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "Luca Rendes-Kardos")
@allure.link("https://dev.example.com/", name = "Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_isprime_1():
    assert bl.isprime(7) == True
    
@allure.title("Test 2 is not a prime ")
@allure.description("This test attempts to test wether 100 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "Luca Rendes-Kardos")
@allure.link("https://dev.example.com/", name = "Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_isprime_2():
    assert bl.isprime(100) == False

@allure.title("Test 3 is a prime ")
@allure.description("This test attempts to test wether 0 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "Luca Rendes-Kardos")
@allure.link("https://dev.example.com/", name = "Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_isprime_3():
    assert bl.isprime(0) == True

