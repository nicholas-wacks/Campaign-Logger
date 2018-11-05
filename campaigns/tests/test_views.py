from django.test import TestCase
from django.utils.html import escape
from campaigns.views import index
from campaigns.models import Campaign
from users.models import User

CAMPAIGNS_LIST_ELEMENT = '<div class="list-group" id="campaigns">'
USERNAME = 'Flumphy'
USER_EMAIL = 'flumph@dire.space'
USER_PASSWORD = 'dire565Flumpher'

class HomePageTest(TestCase):

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/campaigns/')
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_has_no_list_for_unauthenticated_user(self):
        response = self.client.get('/campaigns/')
        self.assertNotContains(response, CAMPAIGNS_LIST_ELEMENT) 

    def test_home_page_shows_authenticated_user_campaigns(self):
        user_ = User.objects.create_user(USERNAME, USER_EMAIL, USER_PASSWORD)
        new_campaign = Campaign.objects.create(Name='Attack of the Flumphs')
        new_campaign.Users.add(user_)
        new_campaign.save()

        self.client.login(username=USERNAME, password=USER_PASSWORD)
        response = self.client.get('/campaigns/')

        self.assertContains(response, 'Attack of the Flumphs')
        self.assertContains(response, CAMPAIGNS_LIST_ELEMENT)