import unittest
from datetime import datetime
import re

class TestAccountCreation(unittest.TestCase):
    # Email validasyon testleri
    def test_email_validation(self):
        """Equivalence Partitioning: Geçerli/geçersiz email formatları"""
        valid_emails = [
            "testexample.com",
            "user.name+tag@domain.co",
            "a@b.co"  # Min format
        ]
        invalid_emails = [
            "user.com",              # @ yok
            "user@.com",             # domain yok
            "user@domain",           # TLD yok
            "a"*256 + "@example.com", # Çok uzun
            " user@example.com",     # Başta boşluk
            "user@example.com "      # Sonda boşluk
        ]
        
        for email in valid_emails:
            self.assertTrue(self.is_valid_email(email), f"Geçerli email reddedildi: {email}")
        for email in invalid_emails:
            self.assertFalse(self.is_valid_email(email), f"Geçersiz email kabul edildi: {email}")

    # Password testleri
    def test_password_strength(self):
        """Boundary Value Analysis: Şifre karmaşıklığı"""
        strong_passwords = [
            "A1!abcdef",    # Min uzunluk (8)
            "A1!@" + "a"*50 # Uzun şifre
        ]
        weak_passwords = [
            "A1!abc",       # 7 karakter (sınır değer)
            "abcdefgh",     # Sayı yok
            "12345678",     # Büyük harf yok
            "A1! abc",      # Boşluk içeriyor
            "パスワード"     # Unicode
        ]
        
        for pwd in strong_passwords:
            self.assertTrue(self.is_strong_password(pwd), f"Güçlü şifre reddedildi: {pwd}")
        for pwd in weak_passwords:
            self.assertFalse(self.is_strong_password(pwd), f"Zayıf şifre kabul edildi: {pwd}")

    # İsim testleri
    def test_name_validation(self):
        """Boundary Test: İsim sınır değerleri"""
        valid_names = ["A", "Ä", "A"*100]  # Min/Max uzunluk
        invalid_names = [
            "",             # Boş
            "John123",      # Sayı
            "A"*101,        # Çok uzun
            "John_Doe",     # Özel karakter
            "NULL"          # SQL keyword
        ]
        
        for name in valid_names:
            self.assertTrue(self.is_valid_name(name), f"Geçerli isim reddedildi: {name}")
        for name in invalid_names:
            self.assertFalse(self.is_valid_name(name), f"Geçersiz isim kabul edildi: {name}")

    # Doğum tarihi testleri
    def test_date_of_birth(self):
        """Equivalence Partitioning + Boundary: Tarih validasyonu"""
        valid_dates = [
            "01/01/1900",  # Min yıl
            "31/12/2023",  # Max yıl
            "15/06/2000"   # Normal
        ]
        invalid_dates = [
            "32/01/2000",  # Geçersiz gün
            "15/13/2000",  # Geçersiz ay
            "15/06/3000",  # Gelecek tarih
            "01-01-2000",  # Yanlış format
            "0"*100        # Buffer overflow
        ]
        
        for date in valid_dates:
            self.assertTrue(self.is_valid_dob(date), f"Geçerli tarih reddedildi: {date}")
        for date in invalid_dates:
            self.assertFalse(self.is_valid_dob(date), f"Geçersiz tarih kabul edildi: {date}")

    # Şifre eşleşme testi
    def test_password_match(self):
        """Confirm Password karşılaştırması"""
        self.assertTrue(self.is_password_match("Pass123!", "Pass123!"))
        self.assertFalse(self.is_password_match("Pass123!", "pass123!"))
        self.assertFalse(self.is_password_match("Pass123!", ""))

    # Güvenlik testleri
    def test_security(self):
        """SQL Injection ve XSS denemeleri"""
        attacks = [
            "' OR '1'='1",
            "<script>alert(1)</script>",
            "DROP TABLE users"
        ]
        for attack in attacks:
            # İsim, email ve şifre alanlarını test et
            self.assertFalse(self.is_valid_name(attack))
            self.assertFalse(self.is_valid_email(attack + "@example.com"))
            self.assertFalse(self.is_strong_password(attack))

    # Yardımcı fonksiyonlar
    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email)) and len(email) <= 255

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*" for c in password) and
                ' ' not in password)

    @staticmethod
    def is_valid_name(name):
        return (name.isalpha() and 
                1 <= len(name) <= 100 and 
                not any(keyword in name.upper() for keyword in ["SELECT", "DROP", "NULL"]))

    @staticmethod
    def is_valid_dob(dob):
        try:
            day, month, year = map(int, dob.split('/'))
            return (1 <= day <= 31 and 
                    1 <= month <= 12 and 
                    1900 <= year <= datetime.now().year)
        except:
            return False

    @staticmethod
    def is_password_match(password, confirm_password):
        return password == confirm_password

if __name__ == '__main__':
    unittest.main(verbosity=2)
