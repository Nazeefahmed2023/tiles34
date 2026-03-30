from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

def landing_page(request):
	import smtplib
	form = ContactForm(request.POST or None)
	sent = False
	error = None
	if request.method == 'POST':
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			message = form.cleaned_data['message']
			subject = f"New Contact Form Submission from {name}"
			body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
			try:
				# Send notification to site owner
				send_mail(
					subject,
					body,
					settings.EMAIL_HOST_USER,
					[settings.EMAIL_HOST_USER],
					fail_silently=False,
				)
				# Send confirmation to user
				confirmation_subject = "Thank you for contacting Tiles Company!"
				confirmation_body = (
					f"Dear {name},\n\n"
					"Thank you for reaching out to Tiles Company. We have received your message and will get back to you soon.\n\n"
					"Here is a copy of your message:\n"
					f"{message}\n\n"
					"Best regards,\nTiles Company Team"
				)
				send_mail(
					confirmation_subject,
					confirmation_body,
					settings.EMAIL_HOST_USER,
					[email],
					fail_silently=False,
				)
				sent = True
				messages.success(request, 'Your message has been sent successfully! A confirmation email has been sent to you.')
				return redirect('landing_page')
			except smtplib.SMTPException as e:
				error = f"There was an error sending your message: {str(e)}"
			except Exception as e:
				error = f"There was an unexpected error: {str(e)}"
	whatsapp_number = '1234567890'  # Replace with your WhatsApp number
	return render(request, 'main/landing_page.html', {
		'form': form,
		'whatsapp_number': whatsapp_number,
		'sent': sent,
		'error': error,
	})
