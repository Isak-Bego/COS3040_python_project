from time import sleep

def get_unique_orders(order_items):
    """Returns a list of unique order_ids without using set."""
    unique_order_ids = []
    for item in order_items:
        if item:  # Skip empty lines if any
            order_id = item[0]  # order_id is at index 0
            if order_id not in unique_order_ids:
                unique_order_ids.append(order_id)
    return unique_order_ids