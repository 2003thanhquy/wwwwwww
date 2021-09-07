from django.shortcuts import render
from .forms import ProductForm , RawProductForm
from .models import Product
#Create your views here.
def procduct_create_view(request):
	# if request.method == 'POST'
	# 	new_title =request.POST.get('title')
	# 	
	my_form = RawProductForm()
	if request.method == 'POST':
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			#now the data is good
			Product.objects.create(**my_form.cleaned_data)
		else :
			print(my_form.errors)
	context ={
	'form': my_form
	}
	return render(request,"products/product_create.html",context)

# def procduct_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm()
# 	context ={
# 	'form':form
# 	}
# 	return render(request,"products/product_create.html",context)
