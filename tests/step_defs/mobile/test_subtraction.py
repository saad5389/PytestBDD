import pytest
from pytest_bdd import (given, scenario, then, when, parsers)
from pageObject.calculatorObj import Calculator

calculatorObj = Calculator()


@pytest.mark.skip
@pytest.mark.mobile
@scenario('../../../tests/features/mobile/test_subtraction.feature', 'Subtract two numbers')
def test_launch_application(setup_teardown):
    # Add code to launch the application
    """Subtract two numbers"""


@given('enter first number')
def enter_first_number():
    calculatorObj.number_1()
    calculatorObj.subtract()


@when(parsers.parse('enter second number'))
def enter_second_number():
    calculatorObj.number_2()


@then(parsers.parse('Subtract both numbers'))
def calculate():
    calculatorObj.equals()
