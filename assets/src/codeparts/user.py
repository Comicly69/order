import uuid

def get_hwid():
    return str(uuid.getnode())

hwid = get_hwid()
hwid_uuid = str(uuid.uuid1())

with open("/workspaces/order/assets/data/userdata.txt", "w") as f:
    f.write("HWID:" + hwid + "\n")
    f.write("UUID:" + hwid_uuid + "\n")
