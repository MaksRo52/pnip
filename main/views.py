from django.shortcuts import render
from .forms import HeightForm

def calc_view(request):
    result = None
    normal_result = None
    dv = None
    if request.method == "POST":
        form = HeightForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            gender = form.cleaned_data["gender"]

            # разные формулы по полу (пример)
            if gender == "male":
                result = height * 0.7 + 11.2
                normal_result =  14.3134 + 0.637057 * height
                dv = result / normal_result * 100
            else:
                result = height * 0.7
                normal_result = -0.43188 + 0.664578 * height
                dv = result / normal_result * 100

    else:
        form = HeightForm()

    return render(request, "main/main.html", {"form": form, "result": result, "normal_result": normal_result, "dv": dv})