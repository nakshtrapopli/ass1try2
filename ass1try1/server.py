import grpc
from concurrent import futures
import inventory_pb2
import inventory_pb2_grpc

class InventoryServicer(inventory_pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        self.inventory_data = {
            "IN0001": {
                "id": "IN0001",
                "name": "Item 1",
                "description": "Desc 1",
                "unit_price": 51.00,
                "quantity_in_stock": 25,
                "inventory_value": 1275.00,
                "reorder_level": 29,
                "reorder_time_in_days": 13,
                "quantity_in_reorder": 50,
                "discontinued": False
            }, 
            "IN0002": {
                "id": "IN0002",
                "name": "Item 2",
                "description": "Desc 2",
                "unit_price": 93.00,
                "quantity_in_stock": 132,
                "inventory_value": 12276.00,
                "reorder_level": 231,
                "reorder_time_in_days": 4,
                "quantity_in_reorder": 50,
                "discontinued": False
            }
            
            # Add more inventory records as needed
        }

    def update(self, request, context):
        key_name = request.key_name
        key_value = request.key_value
        val_name = request.val_name
        val_val_new = request.val_val_new

        if key_value in self.inventory_data and val_name in self.inventory_data[key_value]:
            self.inventory_data[key_value][val_name] = float(val_val_new)  # Assuming val_val_new should be a float
            response = inventory_pb2.UpdateResponse(success=True)
        else:
            response = inventory_pb2.UpdateResponse(success=False)

        return response

    # Add other service methods for searchByID, search, searchRange, getDistribution, etc. here...

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

