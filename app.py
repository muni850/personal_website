from flask import Flask, render_template, request, redirect, url_for, flash
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv("data.env")

app = Flask(__name__)
app.secret_key = "secret_key_for_flash_messages"

# Gmail credentials from data.env
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
ORG_EMAIL = os.getenv("ORG_EMAIL")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        phone = request.form['phone']
        country_code = request.form['country_code']

        try:
            send_email_to_user(name, email, country_code, phone)
            flash("Contacted successfully! A confirmation email has been sent", "success")
        except Exception as e:
            flash("Failed to contact — please try again later.", "error")

        return redirect(url_for('contact'))

    return render_template('contact.html')

def send_email_to_user(name, email, country_code, phone):
    subject = "Thank you for your interest!"
    body = f"""
    Hi {name},

    Thanks for your interest in my profile!

    I’ve received your contact details:
    - Email: {email}
    - Phone: {country_code} {phone}

    I will get back to you soon.

    Regards,
    Muni Sundaram
    """

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, email, msg.as_string())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
