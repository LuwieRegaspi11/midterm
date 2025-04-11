from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    custom_subject = request.form.get('custom_subject')
    contact_method = request.form.getlist('contact_method')
    agreement = 'Yes' if request.form.get('agreement') else 'No'

    errors = []

    if not name or not email or not phone or not message:
        errors.append("All fields are required.")
    if not phone.isnumeric():
        errors.append("Phone number must be numeric.")
    if subject == "Other" and not custom_subject:
        errors.append("Please provide a custom subject.")
    if not request.form.get('agreement'):
        errors.append("You must agree to the terms and conditions.")

    if errors:
        return render_template('contact_form.html', errors=errors, form=request.form)

    if subject == "Other":
        subject = custom_subject

    return render_template('confirmation.html',
                           name=name,
                           email=email,
                           phone=phone,
                           message=message,
                           subject=subject,
                           contact_method=", ".join(contact_method),
                           agreement=agreement)

if __name__ == '__main__':
    app.run(debug=True)