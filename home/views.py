from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def subscribe(request):
    email = request.POST.get('EMAIL')
    print(f"email: {email}")
    valid_email = False
    try:
        validate_email(email)
        valid_email = True
    except ValidationError:
        valid_email = False

    if valid_email:
        messages.info(
            request,
            (f"<p class='text-black text-center'>{email}</p>"
                "<p class='text-success text-center'>"
                "<strong> Thanks for subscribing to our newsletter!</strong>"
                "</p>"))
    else:
        messages.error(
            request,
            (f"<p class='text-black text-center'>{email}</p>"
                "<p class='text-danger text-center'>"
                "Not a valid Email, please try again"
                "</p>"))

    return redirect(reverse('home'))
