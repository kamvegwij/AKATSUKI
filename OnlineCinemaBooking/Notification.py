from twilio.rest import Client

class Notification:
    def __init__(self, customer):
        self.customer = customer


    def sms_notification(self):
        if self.customer.get_booking_status:
            account_sid = "AC9be70d13260f274fa5bd052d6f630d84"
            auth_token = "c74f434fa374cc6c768a33c51bf918c6"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                from_='+18148852106',
                to='+27660990075'
            )


            print(message.status)