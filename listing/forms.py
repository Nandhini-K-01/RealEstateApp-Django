from django import forms
from .models import PropertyListing
from django.forms.widgets import NumberInput

class ListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = '__all__'

# class PropertyPostForm(forms.ModelForm):
#     class Meta:
#         model = PropertyListing
#         fields = ('title', 'description', 'price', 'built_up_area_in_sqft','bedrooms', 'bathrooms', 'location', 'address', 'is_for_sale', 'is_for_rent', 'photo_main')
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'form-control'}),
#             'location': forms.TextInput(attrs={'class':'form-control'}),
#             'description': forms.Textarea(attrs={'class':'form-control'}),
#             'address': forms.TextInput(attrs={'class':'form-control'}),
#             'price': forms.DecimalField(attrs={'class':'form-control'}),
#             'built_up_area_in_sqft': forms.DecimalField(attrs={'class':'form-control'}),
#             'is_for_sale': forms.BooleanField(attrs={'class':'form-control'}),
#             'is_for_rent': forms.BooleanField(attrs={'class':'form-control'})
#         }

class PropertyPostForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ('title', 'description', 'price', 'built_up_area_in_sqft',
                  'bedrooms', 'bathrooms', 'location', 'address', 'is_for_sale',
                  'is_for_rent', 'photo_main')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'built_up_area_in_sqft': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_for_sale': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_for_rent': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
