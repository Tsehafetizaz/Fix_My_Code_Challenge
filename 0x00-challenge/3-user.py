import os


def set_password(self, password):
    salt = os.urandom(32)  # Generate a random salt
    password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    self._password_hash = salt.hex() + password_hash


def is_valid_password(self, password):
    salt = self._password_hash[:64]  # Extract salt from stored hash
    password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return self._password_hash[64:] == password_hash
