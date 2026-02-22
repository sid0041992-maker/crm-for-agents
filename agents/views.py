from django.shortcuts import render, get_object_or_404
from .models import Property, Deal

def apartment_list(request):
    properties = Property.objects.all()
    return render(request, 'agents/apartment_list.html', {'properties': properties})

def apartment_detail(request, id):
    property = get_object_or_404(Property, id=id)
    context = {
        "property": property,
        "owner": {
            "phone": property.owner.phone if property.owner else "не указан",
        },
        "tenant": {
            "phone": "+7 (234) 234-2342",
        },
        "deal": {
            "commission": 14000,
            "insurance_amount": 5200,
            "rent_amount": 28000,
        }
    }
    return render(request, "agents/apartment_detail.html", context)

def deal_detail(request, id):
    deal = get_object_or_404(Deal, id=id)
    return render(request, 'agents/deal_detail.html', {'deal': deal})