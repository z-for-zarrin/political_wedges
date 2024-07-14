from io import BytesIO
import base64
import matplotlib.pyplot as plt
import json
from django.http import JsonResponse, HttpResponse
from my_project.polpargraph import parallelogram
from django.views.decorators.csrf import csrf_exempt

def home_view(request):
    return HttpResponse("Welcome to the home page!")


@csrf_exempt
def parallelogram_view(request):

    dic_reception = json.loads(request.body)
    print(dic_reception)
    group_var = dic_reception["groupVar"]
    group_1_value = dic_reception["group1Value"]
    group_2_value = dic_reception["group2Value"]
    question = dic_reception["question"]

    parallelogram(group_var, group_1_value, group_2_value, question)

    buffer = BytesIO()
    plt.savefig(buffer, format = 'png', dpi=300)
    buffer.seek(0)
    graph = base64.b64encode(buffer.read()).decode('utf-8')

    plt.clf()
    plt.close()
    
    return JsonResponse({'graph': graph})
