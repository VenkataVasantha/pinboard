from django.db import models

class Board(models.Model):

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

	@classmethod
	def get_page_content(self, page_num):
		return context["data"][page_num - 1]

