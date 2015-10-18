import logging, sys
from django.shortcuts import render
from django.core      import serializers
from django.http      import HttpResponse, JsonResponse
from pprint           import pprint
from .models          import Board

# Get an instance of a logger
logger = logging.getLogger(__name__)

# board data from DB based on selected page
def get_page_data(page):

    page_size = 20  # Default page size
    offset    = 0   # Default offset, changes based on page selection

    # If it is not first page then
    # change offset based on page number
    if page > 1:
        offset = page_size * page

    logger.info("offset: " + str(offset))

    # converting the queryset to JSON format
    b = Board.objects.all()[offset:page_size - 1]
    json = serializers.serialize("json", b)
    return json

# For first page, always load page 1
def index(request):
    return render(request, 'layout.html')

# For other pages , load selected page
def load_page(request, page):
    data = get_page_data(int(page))
    return HttpResponse(data, content_type="application/json")

