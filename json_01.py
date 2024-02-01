import json


user = {
    "id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "birthDate": "1973-01-22",
    "login": {
        "uuid": "1a0eed01-9430-4d68-901f-c0d4c1c3bf22",
        "username": "johndoe",
        "password": "jsonplaceholder.org",
        "md5": "c1328472c5794a25723600f71c1b4586",
        "sha1": "35544a31cc19bd6520af116554873167117f4d94",
        "registered": "2023-01-10T10:03:20.022Z"
    },
    "address": {
        "street": "123 Main Street",
        "suite": "Apt. 4",
        "city": "Anytown",
        "zipcode": "12345-6789",
        "geo": {
            "lat": "42.1234",
            "lng": "-71.2345"
        }
    },
    "phone": "(555) 555-1234",
    "website": "www.johndoe.com",
    "company": {
        "name": "ABC Company",
        "catchPhrase": "Innovative solutions for all your needs",
        "bs": "Marketing"
    }
}


try:
    with open('files/user_01.json', 'w') as file_writer:
        json.dump(user, file_writer, indent=4)

except Exception as ex:
    print(f'Dogodila se greska: {ex}')
