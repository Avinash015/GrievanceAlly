DEMO Example Design : https://avinash015.github.io/GrievanceAlly/
# GrievanceAlly
Complaint Management System facilitates registering and tracking complaints across various ministries. It utilizes Google Translate API for multilingual support and MySQL databases for data storage. Additionally, it can be further enhanced into a user-friendly web application using Flask.
# Complaint Management System

This is a Python-based Complaint Management System that allows users to register complaints related to different ministries such as Water, Electricity, Roads, etc. The system can detect the appropriate ministry based on the complaint description and forward the complaint to the respective ministry for resolution. It also provides functionality to check the status of a registered complaint.

## Features

- Register complaints in multiple languages using Google Translate API.
- Detect the appropriate ministry based on the complaint description.
- Store complaints in respective ministry databases as well as a common database.
- Generate unique tokens for each complaint.
- Check the status of a registered complaint using the token ID.

## Installation

1. Clone the repository: https://github.com/Avinash015/GrievanceAlly.git
   
2. Install the required dependencies:
pip install -r requirements.txt


3. Set up a MySQL database and configure the connection parameters in the code.

## Usage
in your google app script write this following code :

          // Example Google Apps Script code
        function sendEmail(recipient, subject, body) {
          var sender = Session.getActiveUser().getEmail();
          GmailApp.sendEmail(sender, subject, body);
        }

now generate web_url and api_key from app script for this function and replace the key in your code .


1. Run the `App.py` script:
python App.py

2. Follow the prompts to choose your preferred language, enter your pincode, Aadhar number, and choose an action (register a complaint or check complaint status).

3. Register a complaint by providing a description. The system will detect the appropriate ministry, forward the complaint, and generate a unique token.

4. Check the status of a registered complaint by providing the token ID.

## Enhancements and Converting to a Website using Flask

This project can be enhanced further by converting it into a web application using Flask. By doing so, users can access the complaint management system through a web browser, providing a more user-friendly and accessible interface. Additionally, features such as user authentication, administration dashboard, and real-time updates can be implemented to improve the functionality and usability of the system.

To convert this project into a web application using Flask, follow these steps:

1. Set up Flask by installing the Flask library:

pip install Flask


2. Create Flask routes to handle different functionalities such as registering complaints, checking complaint status, etc.

3. Implement HTML templates to create the user interface for the web application.

4. Use Flask forms to handle user inputs and validate data.

5. Configure a MySQL database for storing complaint data and integrate it with Flask using SQLAlchemy or similar libraries.

6. Deploy the Flask application on a web server to make it accessible to users.

By converting this project into a web application, you can reach a wider audience and provide a more convenient way for users to register complaints and track their status.

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, feel free to open an issue or create a pull request.





