import smtplib
from azure.servicebus import ServiceBusClient, ServiceBusMessage

def send_email(subject, message_content, to_email):
    from_email = "holaquehace1209@gmail.com"
    password = "kujp litw pzbw oeig"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    msg = f"Subject: {subject}\n\n{message_content}"
    server.sendmail(from_email, to_email, msg)
    server.quit()

def send_message(queue_name, message_content):
    connection_string = "Endpoint=sb://arquitectura.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=UpMx9gUbC0Zcl05sOZUv4tvSGO6XuLIyf+ASbDveWyE="
    client = ServiceBusClient.from_connection_string(connection_string)

    with client:
        sender = client.get_queue_sender(queue_name)
        with sender:
            message = ServiceBusMessage(message_content)
            sender.send_messages(message)
            print(f"Se a detectado una amenaza '{queue_name}': {message_content}")
            send_email("Alerta de amenaza", f"Se a detectado una amenaza {queue_name}: {message_content}", "richi3quintana@gmail.com")

if __name__ == "__main__":
    queue_name = "antivirus"
    message_content = "Su base de datos de virus a sido actualizada"
    send_message(queue_name, message_content)
