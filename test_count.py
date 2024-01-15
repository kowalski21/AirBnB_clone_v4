from models import storage
from models.user import User


print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(User)))

print(
    "User Object by ID: {}".format(
        storage.get(User, "2d808276-2897-4671-a993-9a628abfaf5d8")
    )
)
