from django import forms
from .models import Product
import datetime
class ProductForm(forms.ModelForm):
	class Meta:
		model  =Product
		fields=[
		'title',
		'description',
		'price',
		]
class RawProductForm(forms.Form):
	title  = forms.CharField(label='title',widget=forms.TextInput(attrs={'placeholder':'your title'}))
	description = forms.CharField(label='description', required=False, widget =forms.Textarea(
		attrs = {
		# 'class':'new-class-name two',
		# 'id':'my-id-for-textarea',
		'rows':20,
		'cols':120
		})
		)
	price = forms.DecimalField(max_digits = 100 , decimal_places =2)
