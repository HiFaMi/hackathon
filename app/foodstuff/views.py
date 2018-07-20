from django.http import HttpResponse
from django.shortcuts import render

from foodstuff.forms import ChooseSizeForm, ChooseSourceForm, ChooseToppingForm, ChooseBaseiceForm, ChooseFoodStuffForm
from foodstuff.models import FoodStuff, BaseIce, Source, Topping, Size
from members.forms import User


def choose_category(request):

    if request.method == 'POST':
        forms = ChooseFoodStuffForm(request.POST)

        if forms.is_valid:

            FoodStuff.objects.create(
                base_ice=BaseIce.objects.get(pk=request.POST['ice_name']),
                source=Source.objects.get(pk=request.POST['source_name']),
                topping=Topping.objects.get(pk=request.POST['topping_name']),
                size=Size.objects.create(food_size=request.POST['food_size'])
            )

            user = User.objects.get(username=request.user.username)
            user.order = FoodStuff.objects.last()
            return HttpResponse('Choice Success')

    baseice = ChooseBaseiceForm()
    source = ChooseSourceForm()
    toppings = ChooseToppingForm()
    sizes = ChooseSizeForm()
    context = {
        'baseice': baseice,
        'source': source,
        'toppings': toppings,
        'sizes': sizes,

    }

    return render(request, 'foodstuff/choose.html', context)


def show_foodstuff(request):
    user = User.objects.get(username=request.user.username)

    food_order = user.order

    context = {
        'foods': food_order
    }

    return render(request, 'foodstuff/food.html', context)
