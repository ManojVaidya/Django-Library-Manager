from django.shortcuts import render
from django.views import generic
from .models import Booking
# Create your views here.


def makeentry(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname', '')
        authorname = request.POST.get('authorname', '')
        category = request.POST.get('category', '')
        count = request.POST.get('count', '')
        callno = request.POST.get('callno', '')
        publication = request.POST.get('publication', '')
        section = request.POST.get('section', '')

        booking = Booking(bookname=bookname, authorname=authorname, category=category, count=count, callno=callno, publication=publication, section=section)
        booking.save()
        return render(request,'genericViews/makeEntry.html')
    else:
        return render(request, 'genericViews/makeEntry.html')


def home(request):
    return render(request, 'genericViews/landing.html')


def login(request):
    return render(request, 'genericViews/login.html')


class IndexView(generic.ListView):
    context_object_name = 'booking_list'
    template_name = 'genericViews/index.html'

    def get_queryset(self):
        return Booking.objects.all()


class DetailView(generic.DetailView):
    model = Booking
    template_name = 'genericViews/detail.html'


