# Cafe Review Web App

A simple web application built with Flask that allows users to add, view, and delete cafes. The app stores cafe information in a CSV file and displays the data in a table format. Users can add new cafes with their details and ratings, and delete any existing cafe entry.

## Features

- Add new cafes with details like name, location (URL), opening and closing times, coffee rating, wifi rating, and power outlet availability.
- View all cafes in a table format with clickable links to the cafe locations.
- Delete cafes from the list, and the changes will be reflected in the CSV file.

## Tech Stack

- Python
- Flask
- Flask-Bootstrap
- Flask-WTF
- WTForms
- HTML/CSS (Bootstrap)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/cafe-review-web-app.git
    cd cafe-review-web-app
    ```

2. **Create a virtual environment and activate it:**

   - For Windows:
   
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - For MacOS/Linux:
   
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    flask run
    ```

    The app will be available at `http://127.0.0.1:5000/`.

## Usage

1. Navigate to the home page by visiting `http://127.0.0.1:5000/`.
2. To add a new cafe, click on "Add a new cafe" and fill in the form with the cafe details.
3. Click "Submit" to add the cafe to the list.
4. To view all cafes, click on "See all cafes" on the home page.
5. To delete a cafe, click the "Delete" button next to the cafe entry.

## Project Structure

├── app.py # Main application file ├── cafe-data.csv # CSV file to store cafe data ├── templates/ # HTML templates for the app │ ├── base.html # Base template │ ├── index.html # Home page template │ ├── add.html # Add cafe page template │ └── cafes.html # Cafes list page template ├── static/ # Static files (CSS, JS, images) ├── README.md # Project README file └── requirements.txt # Python dependencies


## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [WTForms](https://wtforms.readthedocs.io/) - For form handling and validation.
- [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/) - For Bootstrap integration with Flask.

---

Feel free to customize the README with any additional information or changes specific to your project.
