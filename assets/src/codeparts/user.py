import uuid
import hashlib

def get_hwid():
    return str(uuid.getnode())

hwid = get_hwid()
hwid_uuid = str(uuid.uuid1())

hash_object = hashlib.sha256(hwid.encode())
hashed_hwid = hash_object.hexdigest()

with open("C:\\Users\\comic\\Documents\\GitHub\\order\\assets\\data\\userdata.txt", "w") as f:
    f.write("HWID:" + hashed_hwid + "\n")
    f.write("UUID:" + hwid_uuid + "\n")

print("Note:HWID is hashed for privacy reasons")
