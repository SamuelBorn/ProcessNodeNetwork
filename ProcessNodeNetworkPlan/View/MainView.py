import json

from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from ProcessNodeNetworkPlan.logic.Graph import Graph


class MainView(View):
    def get(self, request):
        if not request.is_ajax():
            return render(request, "main.html")

        rows_json = json.loads(request.GET.get("row_json"))
        cleaned_rows_json = self.clean_json_graph(rows_json, request)
        if not cleaned_rows_json[0]:  # cleaned rows [0] says if op was successful
            return JsonResponse({"err_mes": cleaned_rows_json[1]}, status=400)
        print(cleaned_rows_json)
        return render(request, "results.html")

    def clean_json_graph(self, rows_json, request):
        for row in rows_json.get("rows"):
            try:
                predecessors = self.csv_to_list(row, "Vorgänger")
                min_times = self.csv_to_list(row, "Mindestabstand")
                max_times = self.csv_to_list(row, "Maximalabstand")
                length = float(row.get("Dauer"))
            except ValueError:
                return False, f"Fehlerhafte Eingabe einer Zahl in Zeile {row.get('#')}"

            if len(predecessors) != len(min_times) or len(min_times) != len(max_times):
                return False, f"Ungleiche Anzahl an Argumenten in Zeile {row.get('#')}"

            row["Vorgänger"] = predecessors
            row["Mindestabstand"] = min_times
            row["Maximalabstand"] = max_times
            row["Dauer"] = length
        return True, rows_json

    def csv_to_list(self, row, name):
        my_list = []
        for predecessor in row.get(name).split(','):
            if predecessor.strip() == '':
                my_list.append(Graph.GraphJsonEnum.not_used)
            else:
                x = float(predecessor)
                if not x.is_integer():
                    raise ValueError()
                my_list.append(x)
        return my_list
