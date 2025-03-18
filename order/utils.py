import uuid

def generate_order_id():
    order_id = str(uuid.uuid4()).replace("-", "")[:8]
    return order_id