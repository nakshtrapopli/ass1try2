# InventoryRecord.py
class InventoryRecord:
    def __init__(self, id, name, description, unit_price, quantity_in_stock, inventory_value, reorder_level, reorder_time_in_days, quantity_in_reorder, discontinued):
        self.id = id
        self.name = name
        self.description = description
        self.unit_price = unit_price
        self.quantity_in_stock = quantity_in_stock
        self.inventory_value = inventory_value
        self.reorder_level = reorder_level
        self.reorder_time_in_days = reorder_time_in_days
        self.quantity_in_reorder = quantity_in_reorder
        self.discontinued = discontinued


inventory_list = [
    InventoryRecord("IN0001", "Item 1", "Desc 1", 51.00, 25, 1275.00, 29, 13, 50, False),
    InventoryRecord("IN0002", "Item 2", "Desc 2", 93.00, 132, 12276.00, 231, 4, 50, False),
    # ... add more InventoryRecord objects as needed
]