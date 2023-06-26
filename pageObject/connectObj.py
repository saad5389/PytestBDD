import time

from selenium.webdriver.common.by import By
from driver_handler import DriverHandle


class Connect:
    INVITATION_METHOD = (By.ID, 'invitation1')
    EMAIL_INVITATION_METHOD = (By.XPATH, '//*[@id="dropdown-invitation-method1"]/li/a[contains(text(), "Email Invitation")]')
    CONTACT_DETAILS = (By.ID, 'invitationDetail1')
    INVITE_PARTICIPANTS_BTN = (By.CSS_SELECTOR, '[ng-click="inviteParticipants()"]')
    INVITE_URL = (By.CSS_SELECTOR, '[text="invitation_url"]')
    JOIN_ROOM_BTN = (By.CSS_SELECTOR, '[automation="joinRoomNow"]')
    VIDEO_PLAYER = (By.ID, '#video-container')
    END_CALL = (By.CSS_SELECTOR, '[automation="endCall"]')
    BLACK_TOAST = (By.ID, '#noty_layout__bottomCenter')

    def __init__(self):
        self.driver_handler = DriverHandle()

    def email_invitation_method(self):
        self.driver_handler.click_element(*self.INVITATION_METHOD)
        self.driver_handler.click_element(*self.EMAIL_INVITATION_METHOD)
        # return self.driver_handler.click_element_by_text(*self.EMAIL_INVITATION_METHOD, ' Email Invitation')

    def enter_email(self, email):
        self.driver_handler.send_keys(*self.CONTACT_DETAILS, email)

    def invite_participants(self):
        self.driver_handler.click_element(*self.INVITE_PARTICIPANTS_BTN)
        time.sleep(3)
        self.driver_handler.wait_for_element_to_display(*self.INVITE_URL)

    def join_room(self):
        print("-------------------1-------------")
        self.driver_handler.click_element(*self.JOIN_ROOM_BTN)
        time.sleep(5)
        # self.driver_handler.alert()

    def joined_call_end(self):
        self.driver_handler.wait_for_element_to_display(*self.VIDEO_PLAYER)
        self.driver_handler.click_element(*self.END_CALL)

    def black_toast(self):
        self.driver_handler.wait_for_element_to_display(*self.BLACK_TOAST)
