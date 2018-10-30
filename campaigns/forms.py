from django import forms
from .models import Campaign

EMPTY_NAME_ERROR = "You can't have an empty name for your campaign"

class CampaignForm(forms.models.ModelForm):
    
    class Meta:
        model = Campaign
        fields = ('Name', )
        widgets = {
            'Name': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a name for your campaign',
                'class': 'form-control',
            })
        }
        error_messages = {
            'Name': {'required': EMPTY_NAME_ERROR}
        }

    def save(self, for_user):
        super().save()
        self.instance.Users.add(for_user)
        self.instance.Admins.add(for_user)
        return super().save()
