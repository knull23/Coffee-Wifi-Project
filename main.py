from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Create the CafeForm with SelectFields for ratings
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL(require_tld=True, message='Invalid URL')])
    opening_time = StringField('Open', validators=[DataRequired()])
    closing_time = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['✘', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Open the CSV file in append mode without extra newlines
        with open("cafe-data.csv", mode="a", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([
                form.cafe.data,
                form.location.data,
                form.opening_time.data,
                form.closing_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        # Separate headers and data rows
        headers = next(csv_data)
        list_of_rows = [row for row in csv_data]

    # Add unique ID (line number) to each row
    cafes_with_ids = [(index, row) for index, row in enumerate(list_of_rows)]
    return render_template('cafes.html', cafes=cafes_with_ids, headers=headers)


# Route to delete a specific cafe by its row index
@app.route('/delete/<int:row_id>', methods=["POST"])
def delete_cafe(row_id):
    # Read all rows from the CSV
    with open('cafe-data.csv', 'r', newline='', encoding='utf-8') as csvfile:
        rows = list(csv.reader(csvfile))

    # Keep the headers intact
    headers = rows[0]
    data_rows = rows[1:]

    # Remove the row at the given index
    if 0 <= row_id < len(data_rows):
        del data_rows[row_id]

    # Write the updated rows back to the CSV file
    with open('cafe-data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write headers first
        csv_writer.writerow(headers)
        # Write data rows
        csv_writer.writerows(data_rows)

    # Redirect back to the list of cafes
    return redirect(url_for('cafes'))


if __name__ == '__main__':
    app.run(debug=True)




