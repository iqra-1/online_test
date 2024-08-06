import secrets

# Generate a secure random string of bytes
secret_key = secrets.token_urlsafe(32)
print(secret_key)
