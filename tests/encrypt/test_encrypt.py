from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    def test_invalid_key_type():
        with pytest.raises(TypeError, match="tipo inválido para key"):
            encrypt_message("message", "a")

    def test_invalid_message_type():
        with pytest.raises(TypeError, match="tipo inválido para message"):
            encrypt_message(2, 1)

    def test_negative_key():
        message = "message"
        assert encrypt_message(message, -1) == message[::-1]

    def test_odd_key():
        message = "message"
        result = "egass_em"
        assert encrypt_message(message, 2) == result

    test_invalid_key_type()
    test_invalid_message_type()
    test_negative_key()
    test_odd_key()
