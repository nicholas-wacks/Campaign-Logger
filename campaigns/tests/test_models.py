from django.test import TestCase
from campaigns.models import Campaign
from users.models import User
from django.core.exceptions import ValidationError

class CampaignModelTest(TestCase):
    def test_campaign_is_related_to_user(self):
        _user = User.objects.create_user('Flumphy', 'flumph@dire.space', 'dire565Flumpher')
        _user.save()
        _campaign = Campaign()
        _campaign.Name = 'Test of the Flumph'
        _campaign.save()
        _campaign.Users.add(_user)
        _campaign.save()

        self.assertIn(_campaign, _user.campaign_set.all())