import requests
from googletrans import Translator
import random
import string
import mysql.connector
from mysql.connector import Error


web_app_url = 'Your_appScript_web_url'
api_key = "api_key_from_app_script"

ministry_db_configs = {
    "Ministry of Water": {"database": "water_ministry_db"},
    "Ministry of Electricity": {"database": "electricity_ministry_db"},
    "Ministry of Roads": {"database": "roads_ministry_db"},
    # Add more ministries and their respective databases
}

def send_email(recipient, subject, body):
    # Prepare the payload for the POST request
    payload = {
        'r': recipient,
        's': subject,
        'b': body
    }

    try:
        # Make an HTTP POST request to the Google Apps Script web app
        response = requests.get(web_app_url, params=payload)

        # Check the response status
        if response.status_code == 200:
            print('Email sent successfully!')
        else:
            print(f'Error sending email. Status Code: {response.status_code}, Response Text: {response.text}')

    except requests.RequestException as e:
        print(f'Error making HTTP request: {e}')

def get_ministry_connection(ministry):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=ministry_db_configs[ministry]["database"]
        )
        return connection
    except Error as e:
        print(f"Error connecting to the {ministry} database: {e}")
        return None

def insert_complaint_into_ministry(complaint_description, ministry, token_id, language, pincode, aadhar_number):
    try:
        connection = get_ministry_connection(ministry)
        if connection:
            cursor = connection.cursor()

            # Insert the complaint into the ministry's table
            insert_query = "INSERT INTO ministry_complaints (complaint_description, token_id, language, pincode, aadhar_number) VALUES (%s, %s, %s, %s, %s)"
            data = (complaint_description, token_id, language, pincode, aadhar_number)
            cursor.execute(insert_query, data)
            connection.commit()
            print(f"Complaint data stored in {ministry} database successfully.")
    except Error as e:
        print(f"Error inserting data into {ministry} database: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def store_complaint_in_databases(complaint_description, ministry, token_id, language, pincode, aadhar_number):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='all_ministries_db'  # Common database
        )
        if connection:
            cursor = connection.cursor()

            # Insert the complaint into the 'all_complaints' table
            insert_query = "INSERT INTO all_complaints (complaint_description, ministry, token_id, language, pincode, aadhar_number) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (complaint_description, ministry, token_id, language, pincode, aadhar_number)
            cursor.execute(insert_query, data)
            connection.commit()
            print("Complaint data stored in the 'all_ministries_db' database successfully.")
    except Error as e:
        print(f"Error inserting data into 'all_ministries_db' database: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def generate_unique_token():
    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    return token

def detect_and_translate(input_text, input_language, target_language='en'):
    try:
        translator = Translator()
        translated_input = translator.translate(input_text, src=input_language, dest='en').text
        ministry, contact_email = determine_ministry(translated_input, fake_ministries)

        if ministry:
            problem_statement = translated_input
            while True:
                response = f"Do you want to send your complaint to {ministry}? (yes=1/no=0): "
                translated_response = translator.translate(response, src='en', dest=input_language).text
                confirmation = input(translated_response.strip().lower())

                if confirmation.lower() == '1':
                    recipient = contact_email  # Set the recipient based on the detected ministry's contact email
                    subject = f'Complaint for {ministry}'
                    body = problem_statement
                    send_email(recipient, subject, body)
                    subject = translator.translate(f'Complaint for {ministry}', src='en', dest=input_language).text
                    body = translator.translate(problem_statement, src='en', dest=input_language).text
                    send_email(recipient, subject, body)


                    token_id = generate_unique_token()
                    insert_complaint_into_ministry(input_text, ministry, token_id, input_language, pincode, aadhar_number)
                    store_complaint_in_databases(input_text, ministry, token_id, input_language, pincode, aadhar_number)
                    token = f"Your complaint's token number is: {token_id}"
                    translated_token = translator.translate(token, src='en', dest=input_language).text
                    print(translated_token)
                    print(translator.translate("Thank you for using the chatbot.", src='en', dest=input_language).text)
                    return
                elif confirmation.lower() == '0':
                    
                    new_description = input(
                        translator.translate("Please describe your complaint again: ", src='en', dest=input_language).text)
                    translated_input = translator.translate(new_description, src=input_language, dest='en').text
                    ministry = determine_ministry(translated_input)
                    if ministry:
                        continue
                    else:
                        response = "Sorry, we couldn't determine the appropriate ministry for your complaint."
                        translated_response = translator.translate(response, src='en', dest=input_language).text
                        print(translated_response)
                else:
                    response = "Invalid input. Please enter '1' or '0'."
                    translated_response = translator.translate(response, src='en', dest=input_language).text
                    print(translated_response)
        else:
            response = "Sorry, we couldn't determine the appropriate ministry for your complaint."
            translated_response = translator.translate(response, src='en', dest=input_language).text
            print(translated_response)
    except Exception as e:
        response = "An error occurred: "
        translated_response = translator.translate(response, src='en', dest=input_language).text
        print(translated_response + str(e))

def choose_language():
    print("Choose your preferred language:")
    print("1 - English")
    print("2 - हिंदी")
    print("3 - ગુજરાતી")
    print('4- ਪੰਜਾਬੀ')
    print('5-मराठी')
    print('6-বাঙ্গালি')
    print('7-ಕನ್ನಡ')
    print('8-తెలుగు')
    print('9-اردو')
    print('0-தமிழ்')

    l = ['en', 'hi', 'gu', 'pa', 'mr', 'bn', 'kn', 'te', 'ur', 'ta']
    c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    while True:
        language_choice = input('Enter the number of your preferred language:')

        language_choice = int(language_choice)

        if language_choice in c:
            index = c.index(language_choice)
            return l[index]
        else:
            print("Invalid choice. Please enter a valid number.")

def get_valid_pincode(input_language):
    while True:
        pincode = input(translator.translate("Please enter your pincode:", src='en', dest=input_language).text)
        if len(pincode) == 6 and pincode.isdigit():
            return pincode
        else:
            print(translator.translate("Invalid PIN code. Please enter a 6-digit PIN code.", src='en', dest=input_language).text)

def get_valid_aadhar_number(input_language):
    while True:
        aadhar_number = input(translator.translate("Please enter your Aadhar number:", src='en', dest=input_language).text)
        if len(aadhar_number) == 12 and aadhar_number.isdigit():
            return aadhar_number
        else:
            print(translator.translate("Invalid Aadhar number. Please enter a 16-digit Aadhar number.", src='en', dest=input_language).text)

def choose_action(input_language):
    print(translator.translate("Choose an action:", src='en', dest=input_language).text)
    print(translator.translate("1 - Register a Complaint", src='en', dest=input_language).text)
    print(translator.translate("2 - Check Complaint Status", src='en', dest=input_language).text)
    while True:
        action_choice = input(translator.translate("Enter the number of your preferred action: ", src='en', dest=input_language).text)
        if action_choice == '1':
            return 'register'
        elif action_choice == '2':
            return 'check_status'
        else:
            print(translator.translate("Invalid choice. Please enter 1 or 2.", src='en', dest=input_language).text)
def determine_ministry(complaint, ministries):
    for ministry, data in ministries.items():
        keywords = data["keywords"]
        for keyword in keywords:
            if keyword in complaint.lower():
                return ministry, data["contact"]
    return None, None
fake_ministries = {
    "Ministry of Water": {"keywords": ["water", "drinking water", "sanitation", "water supply", "water quality", "water treatment",
                                       "water conservation", "water resources", "water management", "water infrastructure"],
                          "contact": "245121733002@mvsrec.edu.in"},
    "Ministry of Electricity": {
        "keywords": ["electricity", "power", "energy", "electrical supply", "power generation", "electric grid",
                     "power outage", "renewable energy", "electricity rates", "energy efficiency"],
        "contact": "245121733002@mvsrec.edu.in"},
      "Ministry of Roads": {"keywords": ["roads", "infrastructure", "transportation", "road maintenance", "road construction", "traffic management", "road safety", "highways",
                                         "street lighting", "public transportation"],
                            "contact": "245121733002@mvsrec.edu.in"},
    # Add more ministries with keywords and contact information
}



def check_complaint_status(token_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='all_ministries_db'
        )
        if connection:
            cursor = connection.cursor()

            query = "SELECT * FROM all_complaints WHERE token_id = %s"
            cursor.execute(query, (token_id,))
            complaint = cursor.fetchone()

            if complaint:
                ministry = complaint[2]
                complaint_description = complaint[1]
                print(f"Complaint Status:\nMinistry: {ministry}\nDescription: {complaint_description}")
            else:
                print("Invalid Token ID. Please check the token ID and try again.")

    except Error as e:
        print(f"Error checking complaint status: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

input_language = choose_language()
translator = Translator()
pincode = get_valid_pincode(input_language)
aadhar_number = get_valid_aadhar_number(input_language)

while True:
    user_action = choose_action(input_language)

    if user_action == 'register':
        complaint_description = input(
            translator.translate("Please describe your complaint:", src='en', dest=input_language).text)
        detect_and_translate(complaint_description, input_language)
    elif user_action == 'check_status':
        token_id_to_check = input(translator.translate("Enter your token ID to check the complaint status: ", src='en',
                                                       dest=input_language).text)
        check_complaint_status(token_id_to_check)
        print(translator.translate("Checking complaint status...", src='en', dest=input_language).text)
    else:
        print(translator.translate("Invalid action. Please try again.", src='en', dest=input_language).text)
