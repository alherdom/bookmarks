from django import forms


def clean_url(self):
    url = self.cleaned_data["url"]
    valid_extensions = ["jpg", "jpeg", "png"]
    extension = url.rsplit(".", 1)[1].lower()
    if extension not in valid_extensions:
        raise forms.ValidationError(
            "The given URL does not ", "match valid image extensions."
        )
    return url
