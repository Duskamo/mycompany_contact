from flask import Flask, request
import os
import json
from src.EmailClient import EmailClient
app = Flask(__name__)

# Data POST Requests
@app.route('/contact', methods=['POST'])
def send_contact():
	# Gather Data
	contactInfo = json.loads(request.json)

	# Send email to dlandry email server using client contact info
	emailClient = EmailClient()

	emailClient.addUserEmail(contactInfo['email'])
	emailClient.addUserName(contactInfo['name'])
	emailClient.addPhone(contactInfo['phone'])
	emailClient.addMessage(contactInfo['message'])

	emailClient.send()

	# Return status code
	return "200"

# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port)
