from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(order):
    """Send the user a confirmation email"""
    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )

    # Required Printing for order tracing purposes (not for debuging)
    print(f"Email:\r\n"
          f"\tFrom:{settings.DEFAULT_FROM_EMAIL}\r\n"
          f"\tTo:{cust_email}\r\n"
          f"\tSubject:{subject}\r\n")
