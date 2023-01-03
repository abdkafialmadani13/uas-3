from django.shortcuts import render
from .models import Posting
# Create your views here.
def index(request):
    postings = Posting.objects.all()
    return render(request, 'los/index.html', {'postings': postings})