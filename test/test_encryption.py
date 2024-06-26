from cryptography.encryption import *
def test_encrypt():
    actual = encrypt("ABC")
    expected = "CDE"
    assert actual == expected

def test_decrypt():
    actual = decrypt("CDE")
    expected = "ABC"
    assert actual == expected    