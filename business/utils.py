import uuid

def generate_trans_id():
    transact_id = str(uuid.uuid4()).replace("-", "")[:8]
    return transact_id