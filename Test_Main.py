from cryptography.fernet import Fernet
from Main import key_generate, encryption, decryption

def test_key_generate():
    key1 = key_generate()
    key2 = key_generate()
    assert isinstance(key1, bytes)
    assert isinstance(key2, bytes)
    assert key1 != key2

def test_encryption_decryption():
    custom_message = "Hello, World!"
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encrypted_message = encryption(fernet, custom_message)
    decrypted_message = decryption(fernet, encrypted_message)

    assert isinstance(encrypted_message, bytes)
    assert decrypted_message.decode() == custom_message

def test_invalid_decryption():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_message = b'Invalid Encrypted Message'
    
    try:
        decrypted_message = decryption(fernet, encrypted_message)
    except Exception as e:
        assert isinstance(e, Exception)
