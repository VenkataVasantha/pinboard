from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Board
import pprint,logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
pp     = pprint.PrettyPrinter(indent=4)

# board data from DB based on selected page
def get_page_data(page):
    page_size = 20  # Default page size
    offset    = 0   # Default offset, changes based on page selection

    # If it is not first page then
    # change offset based on page number
    if page > 1:
        offset = page_size * page

    b = Board.objects.all()[offset:page_size - 1]
    logger
    return b

# For first page, always load page 1
def index(request):
    data = get_page_data(1)
    pp.pprint(data)
    return HttpResponse("Foo")
    #return JsonResponse(data)

# For other pages , load selected page
def load_page(request, page):
	return JsonResponse( get_page_data( int(page) ) )
