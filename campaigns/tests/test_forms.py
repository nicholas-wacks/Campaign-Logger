from django.test import TestCase

from ..forms import CampaignForm, EMPTY_NAME_ERROR
from ..models import Campaign
from users.models import User

class CampaignFormTest(TestCase):

    def test_form_name_input_has_placeholder_and_css_classes(self):
        form = CampaignForm()
        self.assertIn('placeholder="Enter a name for your campaign"', form.as_p())
        self.assertIn('class="form-control"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = CampaignForm(data={'Name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['Name'], [EMPTY_NAME_ERROR])

    def test_form_save_handles_saving_to_admin_anduser_(self):
        user_ = User.objects.create_user('Flumphy', 'flumph@dire.space', 'dire565Flumpher')
        form = CampaignForm(data={'Name': 'Revenge of the Flumph'})
        new_campaign = form.save(for_user=user_)
        self.assertEqual(new_campaign, user_.campaigns.first())
        self.assertEqual(new_campaign.text, 'Revenge of the Flumph')
        self.assertEqual(new_campaign.Admins.first(), user_)