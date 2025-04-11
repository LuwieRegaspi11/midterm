from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        subject = request.form['subject']
        preferred_contact = request.form.getlist('preferred_contact')
        agreement = 'Yes' if 'agreement' in request.form else 'No'

        if not name or not email or not phone or not message:
            error = "All fields must be filled out."
            return render_template('contact_form.html', error=error)
        if not phone.isdigit():
            error = "Phone number must be numeric."
            return render_template('contact_form.html', error=error)
        if subject == "Other" and not request.form.get('other_subject'):
            error = "Please specify your subject if 'Other' is selected."
            return render_template('contact_form.html', error=error)
        if agreement != 'Yes':
            error = "You must agree to the terms and conditions."
            return render_template('contact_form.html', error=error)
        return render_template('confirmation.html', name=name, email=email, phone=phone, message=message,
                               subject=subject, preferred_contact=preferred_contact, agreement=agreement)
        return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)