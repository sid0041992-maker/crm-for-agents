from django.shortcuts import render

def apartment_detail(request):
    # Пока тестовые данные, потом заменим на настоящие из базы
    context = {
        "property": {
            "main_image": "https://via.placeholder.com/200x150",
            "address_full": "Иркутск г., Рябикова б-р., 36/5",
            "property_type": "студия",
            "area": 30,
            "floor": 14,
            "floors_total": 14,
            "contract_url": "#",
            "service_contract_url": "#",
            "acceptance_url": "#",
        },
        "owner": {
            "phone": "+7 (926) 596-8648",
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