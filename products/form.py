from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='title',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your description"
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "hitler" in title:
            raise forms.ValidationError("Not a apropriate title")
        return title
    class Meta:
        model = Product
        fields =[
            'title',
            'summary',
            'price',
            'date'

        ]