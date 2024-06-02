
# %%
import pandas as pd
from SendEmail import send_email
import time

data = pd.read_csv('../data/actualfinaljpromlist.csv', names = ["date", "sessionid", "ip", "name", "number1", "1staddress", "place", "state", "number2", "number3", "paid", "blank","blank2", "approval", "email", "name2", "email2", "osis", "homeroom", "purchase"])

# %%

start = 220
end = 380

# %%

highest = data.shape[0]

# %%

for i in range(start, min(end, highest)):
    p = data.iloc[i]
    name = (str(p["name2"]).strip().split(" ")[0]).strip()
    name = name[0].upper() + name[1:]
    email = p["email"].strip()
    session_id = p["sessionid"].strip()
    approval = p["approval"]
    if ("Approved" in approval) : 
        print(send_email([email, "yinwei.zhang@stuysu.org", "exu51@stuy.edu", "ethan.sie@stuysu.org"], session_id, name))
        time.sleep(2)
    else:
        print(f"{name} is not approved")



