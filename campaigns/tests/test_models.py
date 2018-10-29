from django.test import TestCase
from campaigns.models import Campaign
from users.models import User
from django.core.exceptions import ValidationError

class CampaignModelTest(TestCase):
    def test_campaign_is_related_to_user(self):
        user_ = User.objects.create_user('Flumphy', 'flumph@dire.space', 'dire565Flumpher')
        user_.save()
        _campaign = Campaign()
        _campaign.Name = 'Test of the Flumph'
        _campaign.save()
        _campaign.Users.add(user_)
        _campaign.save()

        self.assertIn(_campaign, user_.campaigns.all())