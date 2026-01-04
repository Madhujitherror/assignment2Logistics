from data.orders import orders

def get_order(order_id: str):
    for order in orders:
        if order["order_id"] == order_id:
            return order
    return None
