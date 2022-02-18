##These are summary notes of the flask wtf extension of flask

# installation command 
# pip install flask_wtf 
# Here's a listing of wtf fields
# 1   TextField	It is used to represent the text filed HTML form element.
# 2	BooleanField	It is used to represent the checkbox HTML form element.
# 3	DecimalField	It is used to represent the text field to display the numbers with decimals.
# 4	IntegerField	It is used to represent the text field to display the integer values.
# 5	RadioField	It is used to represent the radio button HTML form element.
# 6	SelectField	It is used to represent the select form element.
# 7	TextAreaField	It is used to represent text area form element.
# 8	PasswordField	It is used to take the password as the form input from the user.
# 9	SubmitField	It provides represents the <input type = 'submit' value = 'Submit'> html form element.


# here's a list of form validators
# 1. ValidationError(message = "") - raised when a validator fails to validate its input
# 2. StopValidation(message = ' args,**kwags') - stops the validation of the form 
# 3. DataRequired( message = " ") - Checks the field’s data is ‘truthy’ otherwise stops the validation chain.
# 4. validators.Email(message ="")- Validates an email address
# 5. validators.EqualTo( field, message ="") - this compares two value fields
# the parameter field refers to the field its supposed to be equal to 

##sample 
# class ChangePassword(Form):
#     password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
#     confirm  = PasswordField('Repeat Password')


#6 validators.InpuRequired(message = " ") - this ensures that the field if not empty and the user has to fill it
#7 class wtforms.validators.IPAddress(ipv4=True, ipv6=False, message=None)
# 8.class wtforms.validators.Length(min=-1, max=-1, message=None)
# 9.class wtforms.validators.MacAddress(message=None)¶
# 10.class wtforms.validators.NumberRange(min=None, max=None, message=None)
# 11.class wtforms.validators.Optional(strip_whitespace=True)
# 12. class wtforms.validators.AnyOf(values, message=None, values_formatter=None)¶
# values – A sequence of valid inputs.
# message – Error message to raise in case of a validation error. %(values)s contains the list of values.
# values_formatter – Function used to format the list of values in the error message.
# 13. class wtforms.validators.NoneOf(values, message=None, values_formatter=None)¶
# 14.  class wtforms.validators.Regexp(regex, flags=0, message=None)
# Validates the field against a user provided regexp.

# Parameters:	
# regex – The regular expression string to use. Can also be a compiled regular expression pattern.
# flags – The regexp flags to use, for example re.IGNORECASE. Ignored if regex is not a string.
# message – Error message to raise in case of a validation error.

# 15. class wtforms.validators.URL(require_tld=True, message=None)
# Simple regexp based url validation. Much like the email validator, you probably want to validate the url later by other means if the url must resolve.

# Parameters:	
# require_tld – If true, then the domain-name portion of the URL must contain a .tld suffix. Set this to false if you want to allow domains like localhost.
# message – Error message to raise in case of a validation error.
# 16.class wtforms.validators.UUID(message=None)
# Validates a UUID.

# Parameters:	message – Error message to raise in case of a validation error.