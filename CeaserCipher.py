from cryptography.fernet import Fernet

# Generate a key for encryption and decryption using Ceasercipher
key = Fernet.generate_key()
cipher=Fernet(key)

#Encrypt 
def ceasercipher(text,shift=3):
    result=""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        elif char.isdigit():
            result += str((int(char)+shift)%10)
        else:
            result += chr(char)
    return result
def ceaserdecipher(text,shift=3):
    return ceasercipher(text,-shift)

while True:
    print("\n choose from the following")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")
    
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        text=input("Enter input for the encryption:")
        shift = int(input("Enter shift value(default is 3):") or 3)
        encrypted_text = ceasercipher(text,shift)
        print("\nEncrypted text:", encrypted_text)
    elif choice == 2:
        text=input("Enter input for the decryption:")
        shift = int(input("Enter shift value(default is 3):") or 3)
        decrypted_text = ceaserdecipher(text,shift)
        print("\nDecrypted text:", decrypted_text)
    elif choice == 3:
        print("\nExiting...")
        break
    else: 
        print("\nInvalid choice. Please try again.")