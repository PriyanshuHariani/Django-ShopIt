from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def trial(request):
    map = {"4041478854555202009200"
            :{
                "product_name":"Anjeer (Figs) : 100 gms ",
                "quantity": 0.5,
                "amount": 70.3}
           }
    from json import dumps, load
    print(dumps(map), type(map))
    # print(load(map), type(load(map)))
    return render(request, 'shop/trial.html', context={'maps': map})