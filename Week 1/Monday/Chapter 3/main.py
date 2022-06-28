from manager import Manager
from service import ITService, Project

manager = Manager()
it_id = manager.register(ITService)
proj_id = manager.register(Project)

manager.give_offer("Philips", it_id)
print("Philips offers:", manager.get_service("Philips"))
print(
    "Philips update:",
    manager.check_response("Philips", "no"),
)
print(
    "Philips update:",
    manager.check_response("Philips", "yes"),
)

print(manager.customer_summary("Philips"))

manager.give_offer("Philips", proj_id)
print("Philips offers:", manager.get_service("Philips"))
print(
    "Philips update:",
    manager.check_response("Philips", "no"),
)
print(
    "Philips update:",
    manager.check_response("Philips", "yes"),
)

print(
    "Philips update:",
    manager.check_response("Philips", "yes"),
)

print(manager.customer_summary("Philips"))







