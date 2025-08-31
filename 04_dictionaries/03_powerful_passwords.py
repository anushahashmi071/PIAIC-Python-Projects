import hashlib


def hash_password(password: str) -> str:
    """Returns the SHA-256 hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()


def login(username: str, password_to_check: str, stored_value: dict) -> bool:
    if username not in stored_value:
        return False

    stored_login = stored_value[username]
    return stored_login == hash_password(password_to_check)


stored_value = {
    "alice@example.com": hash_password("mypassword123"),
    "bob@example.com": hash_password("secure456"),
}

print(login("alice@example.com", "mypassword123", stored_value))
print(login("alice@example.com", "wrongpass", stored_value))
print(login("bob@example.com", "secure456", stored_value))
print(login("charlie@example.com", "test", stored_value))
