from django.views.generic import View
from django.shortcuts import render


class MainView(View):
    def get(self, request):
        if not request.is_ajax():
            print("Normal Request")
            return render(request, "main.html")

        print(request.GET["action"])
