from django.shortcuts import render
from .forms import ContactForm


# add to your views
def contact(request):
    form_class = ContactForm

    return render(request, 'contactform/contact.html', {
        'form': form_class,
    })
