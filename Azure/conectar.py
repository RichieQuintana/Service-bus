from azure.servicebus import ServiceBusClient

def get_service_bus_client():
    connection_string = "Endpoint=sb://arquitectura.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=UpMx9gUbC0Zcl05sOZUv4tvSGO6XuLIyf+ASbDveWyE="
    client = ServiceBusClient.from_connection_string(connection_string)
    return client

if __name__ == "__main__":
    client = get_service_bus_client()
    print("Conexión establecida con el Service Bus.")
