from mobile_driver_handler import MobileDriverHandle


class Calculator:
    ONE = 'id=com.google.android.calculator:id/digit_1'
    TWO = 'id=com.google.android.calculator:id/digit_2'
    THREE = 'id=com.google.android.calculator:id/digit_3'
    FOUR = 'id=com.google.android.calculator:id/digit_4'
    FIVE = 'id=com.google.android.calculator:id/digit_5'
    SIX = 'id=com.google.android.calculator:id/digit_6'
    SEVEN = 'id=com.google.android.calculator:id/digit_7'
    EIGHT = 'id=com.google.android.calculator:id/digit_8'
    NINE = 'id=com.google.android.calculator:id/digit_9'
    ZERO = 'id=com.google.android.calculator:id/digit_0'
    ADD = 'id=com.google.android.calculator:id/op_add'
    SUBTRACT = 'id=com.google.android.calculator:id/op_sub'
    MULTIPLY = 'id=com.google.android.calculator:id/op_mul'
    DIVIDE = 'id=com.google.android.calculator:id/op_div'
    EQUALS = 'id=com.google.android.calculator:id/eq'

    def __init__(self):
        self.mobile_driver_handler = MobileDriverHandle()

    def number_1(self):
        self.mobile_driver_handler.click_element(self.ONE)

    def number_2(self):
        self.mobile_driver_handler.click_element(self.TWO)

    def number_3(self):
        self.mobile_driver_handler.click_element(self.THREE)

    def number_4(self):
        self.mobile_driver_handler.click_element(self.FOUR)

    def number_5(self):
        self.mobile_driver_handler.click_element(self.FIVE)

    def number_6(self):
        self.mobile_driver_handler.click_element(self.SIX)

    def number_7(self):
        self.mobile_driver_handler.click_element(self.SEVEN)

    def number_8(self):
        self.mobile_driver_handler.click_element(self.EIGHT)

    def number_9(self):
        self.mobile_driver_handler.click_element(self.NINE)

    def number_0(self):
        self.mobile_driver_handler.click_element(self.ZERO)

    def add(self):
        self.mobile_driver_handler.click_element(self.ADD)

    def subtract(self):
        self.mobile_driver_handler.click_element(self.SUBTRACT)

    def multiply(self):
        self.mobile_driver_handler.click_element(self.MULTIPLY)

    def divide(self):
        self.mobile_driver_handler.click_element(self.DIVIDE)

    def equals(self):
        self.mobile_driver_handler.click_element(self.EQUALS)
