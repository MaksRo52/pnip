from django.shortcuts import render
from .forms import HeightForm

def calc_view(request):
    result = None
    minimal_result = None
    dv = None
    if request.method == "POST":
        form = HeightForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            gender = form.cleaned_data["gender"]
            pnip_result = form.cleaned_data["pnip_result"]

            # разные формулы по полу (пример)
            if gender == "male":
                result = height * 0.7 + 11.2
                minimal_result =  14.3134 + 0.637057 * height
                dv = pnip_result / result * 100
            else:
                result = height * 0.7
                minimal_result = -0.43188 + 0.664578 * height
                dv = pnip_result / result * 100

    else:
        form = HeightForm()

    return render(request, "main/main.html", {"form": form, "result": result, "minimal_result": minimal_result, "dv": dv})