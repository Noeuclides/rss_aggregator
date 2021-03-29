from django import forms
from apps.feed.models import Feed


class FeedRegisterForm(forms.ModelForm):

    class Meta:
        model = Feed
        exclude = ['user', '_delete']

    def __init__(self, *args, **kwargs):
        super(FeedRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if hasattr(visible.field.widget, 'input_type'):
                visible.field.widget.attrs['class'] = 'form-control'

