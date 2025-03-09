from .forms import SearchForm, Category

# Pass the search form to all the views
def search_form(request):
    return {'search_form': SearchForm(request.GET or None)}

# Add the categories list to every page, so it can appear in the navbar
def categories(request):
    return {'categories': Category.objects.exclude(id=1)}