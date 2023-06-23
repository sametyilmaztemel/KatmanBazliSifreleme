def encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def decode(text, shift):
    return encode(text, -shift)

choice = input("Şifreleme (1) veya Çözme (2) seçin: ")

if choice == "1":
    plaintext = input("Şifrelenecek metni girin: ")
    shift = int(input("Kaç kez şifrelemek istediğinizi girin: "))
    ciphertext = plaintext
    for _ in range(shift):
        ciphertext = encode(ciphertext, 1)
    print("Şifrelenmiş Metin:", ciphertext)
elif choice == "2":
    ciphertext = input("Çözülecek metni girin: ")
    shift = int(input("Kaç kez çözmek istediğinizi girin: "))
    plaintext = ciphertext
    for _ in range(shift):
        plaintext = decode(plaintext, 1)
    print("Çözülmüş Metin:", plaintext)
else:
    print("Geçersiz seçim.")
