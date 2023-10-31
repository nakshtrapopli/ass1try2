import grpc
import inventory_pb2
import inventory_pb2_grpc

class InventoryClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')  # Replace with your server address and port
        self.stub = inventory_pb2_grpc.InventoryServiceStub(self.channel)

    def update(self, key_name, key_value, val_name, val_val_new):
        try:
            request = inventory_pb2.UpdateRequest(
                key_name=key_name,
                key_value=key_value,
                val_name=val_name,
                val_val_new=val_val_new
            )
            response = self.stub.update(request)
            if response.success:
                print(f"Successfully updated '{val_name}' of record '{key_value}' to '{val_val_new}'.")
            else:
                print(f"Record id '{key_value}' not found or '{val_name}' not found in the record, update failed.")
        except grpc.RpcError as e:
            print(f"Error: {e}")

    # Add other client methods for search, searchByID, getDistribution, etc. here...

if __name__ == '__main__':
    client = InventoryClient()

    # Example usage: Update unit_price of item "IN0001" to "60.00"
    key_name = "id"
    key_value = "IN0001"
    val_name = "unit_price"
    val_val_new = "80.00"

    client.update(key_name, key_value, val_name, val_val_new)