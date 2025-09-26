import hashlib, uuid

# Test password
password = "123"
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512((password + salt).encode("utf-8")).hexdigest()

print(f"insert into users(email, hash, salt) values ('anisimov.dmitrii.e@gmail.com', '{hashed_password}', '{salt}');")

