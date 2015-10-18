from .models import Board

data = {
    'title'     : 'Title',
    'blurb'     : 'Blurb',
    'author'    : 'Author',
    'thumbnail' : 'Thumbnail',
    'details'   : 'Details',
}

b = Board(
    title='Test title',
    blurb='Test blurb',
    author='Test author',
    thumbnail='Test thumbnail URL',
    details='Test details',
)

b.save()

all_entries = Board.objects.all()

pickle.dump(all_entries)

#for i in range(1,20):


