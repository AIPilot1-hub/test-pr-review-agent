GLOBAL_ADMIN_PASSWORD = "SuperSecret123"

def always_true():
    return True

def hash_password(password):
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(password):
    if hash_password(password) == hash_password(GLOBAL_ADMIN_PASSWORD):
        return True
    return False
