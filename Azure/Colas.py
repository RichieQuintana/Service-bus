from azure.servicebus.management import ServiceBusAdministrationClient
from azure.core.exceptions import ResourceNotFoundError, ClientAuthenticationError

def create_queue(queue_name):
    connection_string = "Endpoint=sb://arquitectura.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=UpMx9gUbC0Zcl05sOZUv4tvSGO6XuLIyf+ASbDveWyE="
    admin_client = ServiceBusAdministrationClient.from_connection_string(connection_string)

    try:
        # Check if the queue already exists
        admin_client.get_queue(queue_name)
        print(f"La cola '{queue_name}' ya existe.")
    except ResourceNotFoundError:
        try:
            # If the queue does not exist, create it
            admin_client.create_queue(queue_name)
            print(f"Cola '{queue_name}' creada exitosamente.")
        except ClientAuthenticationError as auth_error:
            print(f"Error de autenticación: {auth_error}")
        except Exception as e:
            print(f"Error al crear la cola: {e}")
    except ClientAuthenticationError as auth_error:
        print(f"Error de autenticación: {auth_error}")
    except Exception as e:
        print(f"Error al verificar la cola: {e}")

if __name__ == "__main__":
    queue_name = "antivirus"
    create_queue(queue_name)

