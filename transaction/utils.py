import uuid

def generate_trans_id():
    trans_id = str(uuid.uuid4()).replace("-", "")[:8]
    return trans_id