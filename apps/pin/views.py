from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

context = {
	'data' : [
	    {
	    	'page': 1, 
	    	'content': [
	    		{
	    			'title_txt'    :'Sample Title 1', 
	    			'blurb_txt'    :'Blurb Text 1',
	    			'author_txt'   :'Author Text 1',
	    			'thumbnail_url':'Thumbnail URL 1',
	    			'details_url'  :'Details Url 1'
	    		},
	    		{
	    			'title_txt'    :'Sample Title 2', 
	    			'blurb_txt'    :'Blurb Text 2',
	    			'author_txt'   :'Author Text 2',
	    			'thumbnail_url':'Thumbnail URL 2',
	    			'details_url'  :'Details Url 2'
	    		}    		
	    	]
	    }
	]
}


# For first page, always load page 1
def index(request):
	content = context["data"][0]
	return JsonResponse(content)

# For other pages , load selected page
def load_page(request, page):
	content = context["data"][int(page) - 1]
	return JsonResponse(content)
