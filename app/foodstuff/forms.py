from django import forms


from foodstuff.models import FoodStuff, Size, Source, Topping, BaseIce


class ChooseFoodStuffForm(forms.ModelForm):
    class Meta:
        model = FoodStuff
        fields = [
            'base_ice',
            'source',
            'topping',
            'size',
        ]


class ChooseBaseiceForm(forms.ModelForm):
    ice_name = forms.ModelChoiceField(
        label='Baseice',
        queryset=BaseIce.objects.all(),
    )

    class Meta:
        model = BaseIce
        fields = ['ice_name']


class ChooseSizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['food_size']


class ChooseSourceForm(forms.ModelForm):
    source_name = forms.ModelChoiceField(
        label='Source',
        queryset=Source.objects.all())

    class Meta:
        model = Source
        fields = ['source_name']


class ChooseToppingForm(forms.ModelForm):
    topping_name = forms.ModelChoiceField(
        label='Topping',
        queryset=Topping.objects.all())

    class Meta:
        model = Source
        fields = ['topping_name']
