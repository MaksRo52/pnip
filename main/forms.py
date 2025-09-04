from django import forms

GENDER_CHOICES = [
    ("male", "Мужской"),
    ("female", "Женский"),
]


class HeightForm(forms.Form):
    height = forms.FloatField(label="Рост (см)", min_value=50, max_value=250)
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label="Пол",
        widget=forms.RadioSelect
    )
    pnip_result = forms.FloatField(label="Результат измерения ПНИП (л/с)", min_value=10, max_value=300)
