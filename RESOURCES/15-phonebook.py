contacts = {
    "Dale": 99021,
    "Tim": 99117,
    "James": 98101,
    "Wilbur": 99093,
    "Thomas": 98872,
    "Kyle": 99807,
    "John": 99971,
    "Bob": 99137,
    "Tyler": 98201,
    "Smith": 99041,
    "Jack": 99116,
    "Vivas": 98103,
    "Josh": 99051
}

# get client's name
client = input("Search 🔎 ")

if client in contacts:
    # client exists
    print(client, contacts[client])
else:
    # client doesn't exists
    print(client, "not found!")