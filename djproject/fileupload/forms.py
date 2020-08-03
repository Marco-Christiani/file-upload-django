from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
    # file = forms.FileField(widget=forms.TextInput(attrs={'class': 'custom-file-input'}))
    #
    # def __init__(self, *args, **kwargs):
    #     super(UploadFileForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].label = "File to Upload"

