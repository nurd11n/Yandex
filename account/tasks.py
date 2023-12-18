from config.celery import app
from account.utils import send_activation_code, send_application_code


@app.task
def send_activation_code_celery(email, activation_code):
    return send_activation_code(email, activation_code)


@app.task
def send_application_celery(first_name, last_name, driver_license, email, activation_code):
    return send_application_code(first_name, last_name, driver_license, email, activation_code)