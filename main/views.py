from django.shortcuts import render
from .forms import HeightForm

def calc_view(request):
    result = None
    if request.method == "POST":
        form = HeightForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            gender = form.cleaned_data["gender"]

            # разные формулы по полу (пример)
            if gender == "male":
                result = height * 0.7 + 11.2
            else:
                result = height * 0.7
    else:
        form = HeightForm()

    return render(request, "main/main.html", {"form": form, "result": result})