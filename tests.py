import unittest
import xor

class TestForXor(unittest.TestCase):
    def test_get_ascii(self):
        num = xor.getAscii("H")
        self.assertEqual(num, 72)
    def test_convert_binary_one(self):
        bin = xor.decimalToBinary(1)
        self.assertEqual(bin, "00000001")
    def test_convert_binary_zero(self):
        bin = xor.decimalToBinary(0)
        self.assertEqual(bin, "00000000")
    def test_convert_binary_seventyTwo(self):
        bin = xor.decimalToBinary(72)
        self.assertEqual(bin, "01001000")
    def test_xor_letter_to_binary(self):
        xorLetter = xor.convertLetterToBinary("H")
        self.assertEqual(xorLetter, "01001000")
    def test_xor_zero(self):
        xorNum = xor.compare("00000000", "00000000")
        self.assertEqual(xorNum, "00000000")
    def test_xor_0_and_1(self):
        xorNum = xor.compare("00000000", "00000001")
        self.assertEqual(xorNum, "00000001")
    def test_xor_72_and_10(self):
        xorNum = xor.compare("01001000", "00001010")
        self.assertEqual(xorNum, "01000010")
    def test_binary_to_decimal_zero(self):
        decimal = xor.binaryToDecimal("00000000")
        self.assertEqual(decimal, 0)
    def test_binary_to_decimal_66(self):
        decimal = xor.binaryToDecimal("01000010")
        self.assertEqual(decimal, 66)
    def test_string_to_xor_one_letter_key_zero(self):
        xorOutput = xor.stringToXor("H", 0)
        self.assertEqual(xorOutput, [72])
    def test_string_to_xor_two_letters_key_zero(self):
        xorOutput = xor.stringToXor("Hi", 0)
        self.assertEqual(xorOutput, [72, 105])
    def test_string_to_xor_two_letters_key_ten(self):
        xorOutput = xor.stringToXor("Hi", 10)
        self.assertEqual(xorOutput, [66, 99])
    def test_string_to_xor_sentence_key_seventyThree(self):
        xorOutput = xor.stringToXor("Hello World", 73)
        self.assertEqual(xorOutput, [1,44,37,37,38,105,30,38,59,37,45])


unittest.main()