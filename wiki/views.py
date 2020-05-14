from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from wiki.models import Page
from wiki.forms import PageForm


class PageCreateView(CreateView):
    '''Create a new wiki page'''
    model = Page
    fields = ['title', 'content', 'author']
    template_name = 'create_page.html'


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
            'pages': pages,
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
            'page': page,
            'form': PageForm()
        })

    def post(self, req, slug):
        '''Edit the page's information'''
        form = PageForm(req.POST)

        page = self.get_queryset().get(slug__iexact=slug)

        '''['title', 'author', 'content'] '''
        page.title = req.POST['title']
        page.content = req.POST['content']
        page.author = req.user
        '''['title', 'author', 'content'] '''
     
        page.slug = slugify(page.title)

        page.save()

        return HttpResponseRedirect(reverse('wiki-details-page', args=[page.slug]))