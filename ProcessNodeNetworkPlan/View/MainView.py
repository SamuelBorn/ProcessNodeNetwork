import json

from django.views.generic import View
from django.shortcuts import render


class MainView(View):
    def get(self, request):
        if not request.is_ajax():
            return render(request, "main.html")

        rows_json = json.loads(request.GET.get("row_json"))
        return render(request, "results.html")
