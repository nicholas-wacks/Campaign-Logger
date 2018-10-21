from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class SimpleWorkflowTest(FunctionalTest):

    def test_user_can_make_campagin_and_invite(self):
        # User Bob goes to base page and sees a link to log in

        # Bob creates a new account

        # Bob sees that he is now logged in and has the option to log out

        # Bob sees an empty list of campaigns, and selects a button 
        #   to create a new one

        # Bob names his campaign "The Boat's Requiem"

        # Bob sees that his campaign has no items

        # Bob creates a new character record, and gives it a name of "Wesley",
        #   and a description of "Dapper Bard and aspiring pirate"

        # Bob returns to the campaign's page and sees the Wesley record

        # Bob notices an invite players link and uses it to send an invite
        #   to Carol, who is one of his players

        # Bob is done for now, and logs out

        # Carol sees an invitation and follows it to the site

        # The link takes her to a page to log in or sign up, with her email prepopulated

        # She creates a new account, which takes her to the campaign, where she
        #   sees the Wesley record and an option to create a new record

        # Content for now, she logs out



