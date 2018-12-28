from django.http import HttpResponse
from django.template import loader

from .models import Item, Category

def index(request):
    # Category.objects.get(id=1).item_set.all)()
    template = loader.get_template('pdb_app/index.html')
    context = {
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context, request))

def item(request, item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None
    
    template = loader.get_template('pdb_app/item.html')
    context = {
        'item': itm
    }
    return HttpResponse(template.render(context, request))