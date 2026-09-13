import hashlib
import uuid

def generate_recipient_keys(recipients):
    keys = {}
    for recipient in recipients:
        unique_id = str(uuid.uuid4())
        key = hashlib.sha256(unique_id.encode()).hexdigest()
        keys[recipient] = key
    return keys

# Example usage
recipient_list = ["Recipient_A", "Recipient_B", "Recipient_C"]
assigned_keys = generate_recipient_keys(recipient_list)

for user, secret_key in assigned_keys.items():
    print(f"User: {user} | Key: {secret_key}")
