
import smtplib, ssl
from .Data import Data

class EmailClient:
	def __init__(self):
		self.port = 465
		self.smtp_server = "smtp.gmail.com"
		self.dlandryClientEmail = Data.clientEmail
		self.dlandryClientPassword = Data.clientPassword
		self.dlandryServerEmail = Data.serverEmail
		

	def addUserEmail(self, userEmail):
		self.userEmail = userEmail

	def addUserName(self, userName):
		self.userName = userName

	def addPhone(self, phone):
		self.phone = phone

	def addMessage(self, message):
		emailSubject = "Subject: MyCompany Contact Request"
		emailMessage = "\"{}\"".format(self.userName) + " with email address: " + "\"{}\"".format(self.userEmail) + " and phone number: " + "\"{}\"".format(self.phone) + " sent you the below message. \n\n" + message

		self.message = emailSubject + "\n\n" + emailMessage

	def send(self):
		
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
		    server.login(self.dlandryClientEmail, self.dlandryClientPassword)
		    server.sendmail(self.dlandryClientEmail, self.dlandryServerEmail, self.message)
