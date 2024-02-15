// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('grievanceForm').style.backgroundColor = 'rgba(255, 255, 255, 0.6)';
    document.getElementById('grievanceForm').style.color = '#000';
    document.getElementById('grievanceForm').style.padding = '20px';
    document.getElementById('grievanceForm').style.borderRadius = '10px';
    document.getElementById('grievanceForm').style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
});

function nextStep(step) {
    document.getElementById(`step${step}`).style.display = 'none';
    step++;
    if (step <= 6) {
        document.getElementById(`step${step-1}`).style.display = 'block';
    }
}

function submitForm(event) {
    event.preventDefault();
    var formData = new FormData(document.getElementById('grievanceForm'));
    formData.append('subject', 'Grievance Submission');
    formData.append('body', 'A new grievance has been submitted.');
    send_email(formData);
}

function send_email(formData) {
    fetch('http://127.0.0.1:5000/send_email_endpoint', {  // Replace with your actual Flask app URL
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log('Email sent successfully!');
        } else {
            console.error(`Error sending email. Status Code: ${response.status}, Response Text: ${response.statusText}`);
        }
    })
    .catch(error => {
        console.error('Error sending email:', error);
    });
}
