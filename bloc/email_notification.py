

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
from rest_framework.views import APIView
from rest_framework import status, response
from celery import shared_task


@shared_task
def send_custom_email(
    to_email, subject, template_name, context, remark=None, attachments=None
):    
    payload = {
        "subject": subject,
        "remark": remark,
        "attachments": attachments,
        "vars": context,  # Your template expects this
    }
    html_content = render_to_string(template_name, payload)

    
    text_content = strip_tags(html_content)  # or render a separate .txt file
    # Create the email object
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=os.environ.get("DEFAULT_FROM_EMAIL", "app@emoticup.com"),
        to=to_email,
    )

    # Attach the HTML version
    email.attach_alternative(html_content, "text/html")

    if attachments:
        for att in attachments:
            if isinstance(att, tuple):
                # (filename, file_bytes)
                filename, file_bytes = att
                email.attach(
                    filename,
                    file_bytes,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            else:
                # assume file path
                email.attach_file(att)

    email.send()
