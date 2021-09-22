import json

from django.views.generic import View
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

import networkx as nx

from ProcessNodeNetworkPlan.logic.ComputeMinMaxTime import ComputeMinMaxTime
from ProcessNodeNetworkPlan.logic.Graph import build_graph_from_json
from ProcessNodeNetworkPlan.media_handler import GraphImageCreator


class MainView(View):
    def get(self, request):
        if not request.is_ajax():
            return render(request, "main.html")

        rows_json = json.loads(request.GET.get("row_json"))
        success, cleaned_rows_json = self.clean_json_graph(rows_json)
        if not success:  # cleaned rows [0] says if op was successful
            return JsonResponse({"err_mes": cleaned_rows_json}, status=400)
        if not self.check_predecessor_indices(cleaned_rows_json)[0]:
            return JsonResponse({"err_mes": self.check_predecessor_indices(cleaned_rows_json)[1]}, status=400)
        graph = build_graph_from_json(cleaned_rows_json)
        if graph.has_positive_cycle():
            return JsonResponse({"err_mes": "Graph contains positive cycle"}, status=400)
        computer = ComputeMinMaxTime(graph)
        GraphImageCreator.create_image(graph)
        context = {"results": computer.compute_sxz_and_fxz(), "image": GraphImageCreator.get_image_base64(graph)}
        return render(request, "results.html", context)

    def check_predecessor_indices(self, cleaned_rows_json):
        indices = []
        for row in cleaned_rows_json.get("rows"):
            indices.append(row.get("#"))
        for row in cleaned_rows_json.get("rows"):
            for predecessor in row.get("Vorgänger"):
                if predecessor not in indices and predecessor is not None:
                    return False, f"Prozess mit Index {predecessor} in Zeile {row.get('#')} ist nicht vorhanden"
        return True, True

    def clean_json_graph(self, rows_json):
        for row in rows_json.get("rows"):
            try:
                predecessors = self.csv_to_list(row, "Vorgänger")
                min_times = self.csv_to_list(row, "Mindestabstand")
                max_times = self.csv_to_list(row, "Maximalabstand")
                if row.get("Dauer").strip() == "-" or row.get("Dauer").strip() == "":
                    length = float(0)
                else:
                    length = float(row.get("Dauer"))
            except ValueError:
                return False, f"Fehlerhafte Eingabe einer Zahl in Zeile {row.get('#')}"

            if len(predecessors) != len(min_times) or len(min_times) != len(max_times):
                return False, f"Ungleiche Anzahl an Argumenten in Zeile {row.get('#')}"

            row["#"] = int(row["#"])
            row["Vorgänger"] = predecessors
            row["Mindestabstand"] = min_times
            row["Maximalabstand"] = max_times
            row["Dauer"] = length
        return True, rows_json

    def csv_to_list(self, row, name):
        my_list = []
        for predecessor in row.get(name).split(','):
            if predecessor.strip() == '' or predecessor.strip() == '-':
                my_list.append(None)
            else:
                x = float(predecessor)
                if name == "Vorgänger":
                    if not x.is_integer():
                        raise ValueError()
                    x = int(x)
                my_list.append(x)
        return my_list

