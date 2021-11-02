import hashlib
import unittest

from users.hash_generator import HashGenerator


class HashGeneratorTest(unittest.TestCase):
    def test_sha256_format(self):
        # arrange
        sha256_result = '36bbe50ed96841d10443bcb670d6554f0a34b761be67ec9c4a8ad2c0c44ca42c'
        # act
        hash_value = HashGenerator.generate_sha256_hash('abcde')
        # assert
        self.assertEqual(sha256_result, hash_value)

    def test_injectivity(self):
        # arrange
        hash_digest = hashlib.sha256("abcde".encode()).hexdigest()
        # act
        hash_value = HashGenerator.generate_sha256_hash("abcde")
        # assert
        self.assertEqual(hash_digest, hash_value)

    def test_collision(self):
        # act
        hash_digest = HashGenerator.generate_sha256_hash("abcde")
        hash_value = HashGenerator.generate_sha256_hash("abcdf")
        # assert
        self.assertNotEqual(hash_digest, hash_value)
