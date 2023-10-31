import unittest
from unittest.mock import MagicMock
import inventory_pb2
import inventory_pb2_grpc
from client import InventoryClient  # Replace 'your_client_module' with the actual name of your client module

class TestInventoryClient(unittest.TestCase):
    def setUp(self):
        self.client = InventoryClient()

        # Mocking gRPC stub for testing purposes
        self.client.stub = MagicMock(spec=inventory_pb2_grpc.InventoryServiceStub)

    def test_search_by_id(self):
        # Prepare a mock response from the gRPC server
        expected_response = inventory_pb2.InventoryRecord(id="IN0001", name="Item 1", description="Sample Item")
        self.client.stub.searchByID.return_value = expected_response

        # Call the searchByID method with a mock ID
        response = self.client.searchByID("IN0001")

        # Assert that the gRPC stub's searchByID method was called with the correct argument
        self.client.stub.searchByID.assert_called_once_with(inventory_pb2.InventoryRequest(id="IN0001"))

        # Assert that the response from the client matches the expected response from the server
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()

