import os
from dotenv import load_dotenv

load_dotenv()

required_vars = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASS"]

emp = []
for name in required_vars:
    if not os.getenv(name):
        emp.append(name)
if emp:
    raise RuntimeError("Variables manquantes : " + ", ".join(emp))

values = {key: os.getenv(key) for key in required_vars}
values["DB_PORT"] = int(values["DB_PORT"])
