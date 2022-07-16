from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .scrappers.albert_heijn_scrapper import get_albert_heijn_product_nutri_data

# Create your views here.
def index(request):
    return HttpResponse("Hi! This service is used to scrap nutrition data for various products.")


def nutri_value(request, id):
    return JsonResponse(get_albert_heijn_product_nutri_data(id))