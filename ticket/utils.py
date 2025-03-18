import uuid

def generate_ticket_id():
    ticket_id = str(uuid.uuid4()).replace("-", "")[:6]
    return ticket_id