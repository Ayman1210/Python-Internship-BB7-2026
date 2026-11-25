
# Base class
class Notification:
    def send(self):
        print("Sending a notification")

# Child class 1
class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

# Child class 2
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

# Create objects
n1 = Notification()
n2 = EmailNotification()
n3 = SMSNotification()

# Store objects in list
notifications = [n1, n2, n3]

# Send all notifications
for notification in notifications:
    notification.send()
