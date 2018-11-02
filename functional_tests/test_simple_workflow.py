from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
from selenium.common.exceptions import WebDriverException
from time import sleep

BOB_PASSWORD = 'G0Atz4R3al!'
CAMPAIGNS_LIST_SELECTOR = 'div#campaigns'

class SimpleWorkflowTest(FunctionalTest):

    def test_user_can_make_campagin_and_invite(self):
        # User Bob, our first invited user, goes to our site and sees a link to log in or sign up
        self.browser.get(self.live_server_url)
        login_link = self.browser.find_element_by_css_selector('a#signup')
        login_link.click()

        # Bob uses the new user form to create his account
        username_input = self.wait_for(lambda: self.browser.find_element_by_css_selector('input#id_username'))
        email_input = self.browser.find_element_by_css_selector('input#id_email')
        password_input = self.browser.find_element_by_css_selector('input#id_password1')
        password_repeat_input = self.browser.find_element_by_css_selector('input#id_password2')
        
        username_input.send_keys('DM_Bob')
        email_input.send_keys('dm.bob@fakemail.com')
        password_input.send_keys(BOB_PASSWORD)
        password_repeat_input.send_keys(BOB_PASSWORD)
        password_repeat_input.send_keys(Keys.ENTER)

        # Bob logs in with his new account
        self.wait_for(lambda: self.browser.find_element_by_css_selector('form#login_form'))
        username_input = self.browser.find_element_by_css_selector('input#id_username')
        password_input = self.browser.find_element_by_css_selector('input#id_password')
        username_input.send_keys('DM_Bob')
        password_input.send_keys(BOB_PASSWORD)
        password_input.send_keys(Keys.ENTER)

        # Bob sees that he is now logged in and has the option to log out
        self.wait_for(lambda: self.browser.find_element_by_css_selector('a#logout'))

        # Bob sees an empty list of campaigns, and selects a button 
        #   to create a new one
        self.wait_for(lambda: self.browser.find_element_by_css_selector(CAMPAIGNS_LIST_SELECTOR))
        self.assertEqual(0, self.browser.find_elements_by_css_selector(CAMPAIGNS_LIST_SELECTOR + ' a.list-group-item').count())
        new_campaign_button = self.browser.find_element_by_css_selector('a#new_campaign')
        new_campaign_button.click()

        # Bob names his campaign "The Boat's Requiem" and gives a description
        campaign_name_input = self.browser.find_element_by_css_selector('input#id_name')
        campaign_description_input = self.browser.find_element_by_css_selector('input#id_name')
        campaign_name_input.send_keys('The Boat\'s Requiem')
        campaign_description_input.send_keys('A testing campaign for testing things')
        campaign_description_input.send_keys(Keys.ENTER)

        # Bob sees his campaign in the list and clicks into it
        self.wait_for(lambda: self.browser.find_element_by_css_selector(CAMPAIGNS_LIST_SELECTOR))
        campaign_link = self.browser.find_element_by_link_text('The Boat\'s Requiem')
        campaign_link.click()

        # Bob sees that his campaign has no items, and clicks to make a new one
        self.wait_for(lambda: self.browser.find_element_by_css_selector('table#characters'))
        self.assertEqual(0, self.browser.find_elements_by_css_selector('table#characters td').count())
        new_item_button = self.browser.find_element_by_css_selector('a#new_character')
        new_item_button.click()

        # Bob creates a new character record, and gives it a name of "Wesley",
        #   and a description of "Dapper Bard and aspiring pirate"
        self.fail('finish this test')

        # Bob returns to the campaign's page and sees the Wesley record

        # Bob notices an invite players link and uses it to send an invite
        #   to Carol, who is one of his players

        # Bob is done for now, and logs out

        # Carol sees an invitation and follows it to the site

        # The link takes her to a page to log in or sign up, with her email prepopulated

        # She creates a new account, which takes her to the campaign, where she
        #   sees the Wesley record and an option to create a new record

        # Content for now, she logs out



