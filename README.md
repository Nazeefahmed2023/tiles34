# Tiles Company Landing Page

A clean, professional landing page for a tiles company built with Django. Features a beautiful UI, contact form with SMTP email, and WhatsApp integration.

## Features
- Modern, responsive landing page
- Contact form (sends email via SMTP)
- WhatsApp contact button
- Beautiful UI with Bootstrap 5

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Configure SMTP settings in `tiles/settings.py`:
   - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the server:
   ```sh
   python manage.py runserver
   ```
5. Visit [http://localhost:8000](http://localhost:8000)

## Customization
- Replace the WhatsApp number in `main/views.py` (`whatsapp_number` variable)
- Update images and branding in `main/templates/main/landing_page.html`

## SMTP Email
- Uses Django's SMTP backend. Make sure to use valid credentials.

## WhatsApp Integration
- The WhatsApp button opens a chat with your company number.

---

*Replace all placeholder values (SMTP, WhatsApp number, images) with your actual company details before deploying.*
