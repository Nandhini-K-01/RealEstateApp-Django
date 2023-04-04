from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PropertyListing, PropertyInquiry
from .forms import PropertyPostForm
from django.urls import reverse_lazy
from authentication.models import UserProfile
from django.contrib.auth.models import User


def property_list(request):
    properties = PropertyListing.objects.all()
    properties = PropertyListing.objects.filter().order_by('-list_date')
    # context = {'properties': properties}
    return render(request, "property.html",  {'properties': properties})

def property_detail(request, pk):
    property = PropertyListing.objects.get(id=pk)
    # next_url = request.GET.get('next', reverse('property_list'))
    # if request.user.is_authenticated and next_url != reverse('property_list'):
    #     return redirect(next_url)
    # context = {'property': property}
    return render(request, 'property_detail.html', {'property': property})

# def property_detail(request, pk):
#     property = PropertyListing.objects.get(id=pk)
#     context = {'property': property, 'current_url': request.get_full_path()}
#     return render(request, 'property_detail.html', context)

# @login_required(login_url='/signin/')
# def contact_agent(request, pk):
#     property = get_object_or_404(PropertyListing, id=pk)
#     if request.method == 'POST':
#         inquiry = PropertyInquiry(listing=property, user=request.user)
#         inquiry.save()
#         messages.success(request, 'Your inquiry has been sent to the agent.')
#         print("print",inquiry)
#         return redirect('contact', pk=pk)
#     else:
#         return render(request, "contact.html", {'property':property})    
    
@login_required(login_url='/signin/')
def contact_agent(request, pk):
    property = get_object_or_404(PropertyListing, id=pk)
    if request.method == 'POST':
        # print(request.POST.get('property'))
        # print(request.POST.get('user'))
        if request.user.is_authenticated:
            print("contact_agent view executed")
            inquiry_exists = PropertyInquiry.objects.filter(listing=property, user=request.user).exists()
            if not inquiry_exists:
                inquiry = PropertyInquiry(listing=property, user=request.user)
                inquiry.save()
                messages.success(request, 'Your inquiry has been sent to the agent.')
                return redirect('contact_agent', pk=pk)
            else:
                return redirect('contact_agent', pk=pk)
        else:
            # User is not authenticated, redirect to login page
            next_url = reverse('contact_agent', kwargs={'pk': pk})
            login_url = f"{reverse('signin')}?next={next_url}"
            return redirect(login_url)
    else:
        if request.user.is_authenticated:
            inquiry = PropertyInquiry.objects.filter(listing=property, user=request.user).exists()
        else:
            inquiry = False
        return render(request, "contact.html", {'property':property, 'inquiry':inquiry})


# @login_required(login_url='/signin/')
# def contact_agent(request, pk):
#     property = get_object_or_404(PropertyListing, id=pk)
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             inquiry = PropertyInquiry(listing=property, user=request.user)
#             inquiry.save()
#             messages.success(request, 'Your inquiry has been sent to the agent.')
#             return redirect('property_detail', pk=pk)
#         else:
#             # User is not authenticated, redirect to login page
#             next_url = reverse('contact_agent', kwargs={'pk': pk})
#             login_url = f"{reverse('signin')}?next={next_url}"
#             return redirect(login_url)
#     else:
#         return render(request, "property_detail.html", {'property':property})


@login_required(login_url='/signin/?next=/post_property/')
def post_property(request):
    if request.method == 'POST':
        form = PropertyPostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form data and create PropertyListing object
            property = form.save(commit=False)
            property.agent = request.user
            property.save()
            messages.success(request, 'Your property has been added successfully.')
            return redirect('property_list')
    else:
        form = PropertyPostForm()
    return render(request, 'post_property.html', {'form': form})

def delete_property(request, pk):
    property = PropertyListing.objects.get(id=pk)
    if request.method == "POST":
        property.delete()
    return redirect('property_list')

def interested_users(request, property_id):
    property = PropertyListing.objects.get(id=property_id)
    interests = PropertyInquiry.objects.filter(listing=property).exclude(user=request.user)
    interested_users = [interest.user for interest in interests]
    context = {'property': property, 'interested_users': interested_users}
    return render(request, 'interestedusers.html', context)

# def interested_users(request, property_id):
#     property_obj = get_object_or_404(Property, pk=property_id)
    
#     # Retrieve all the interested users for the property
#     interested_users = InterestedUser.objects.filter(property=property_obj)
    
#     # Exclude the property owner from the list of interested users
#     interested_users = interested_users.exclude(user=property_obj.owner)
    
#     # Render the interested users template with the list of interested users
#     return render(request, 'interested_users.html', {'interested_users': interested_users})

# @login_required(login_url = '/signin/')
# def post_property(request):
#     if request.method == 'POST':
#         # Get form data and create PropertyListing object
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         built_up_area_in_sqft = request.POST.get('built_up_area_in_sqft')
#         bedrooms = request.POST.get('bedrooms')
#         bathrooms = request.POST.get('bathrooms')
#         location = request.POST.get('location')
#         address = request.POST.get('address')
#         is_for_sale = request.POST.get('is_for_sale')
#         is_for_rent = request.POST.get('is_for_rent')
#         agent = request.user
#         photo_main = request.FILES.get('photo_main')
#         photo_1 = request.FILES.get('photo_1')
#         photo_2 = request.FILES.get('photo_2')
#         photo_3 = request.FILES.get('photo_3')
#         photo_4 = request.FILES.get('photo_4')
#         property = PropertyListing(
#             title=title,
#             description=description,
#             price=price,
#             built_up_area_in_sqft=built_up_area_in_sqft,
#             bedrooms=bedrooms,
#             bathrooms=bathrooms,
#             location=location,
#             address=address,
#             is_for_sale=is_for_sale,
#             is_for_rent=is_for_rent,
#             agent=agent,
#             photo_main=photo_main,
#             photo_1=photo_1,
#             photo_2=photo_2,
#             photo_3=photo_3,
#             photo_4=photo_4,
#         )
#         property.save()
#         messages.success(request, 'Your property has been added successfully.')
#         return HttpResponseRedirect(reverse('property_list'))
#     return render(request, 'post_property.html')

