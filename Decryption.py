# D121191071_Muhammad Arfani Asra
# 3th Program | Decryption of RSA Cryptosystem
import math

print("====== Decryption in RSA ======")
print(" ")
print("Please input d and n value! ")
d = int(input("-> Enter private key (d): "))
n = int(input("-> Enter modulo inverse (n): "))

# Decryption Function
def rsaDecryption(d, n, y): #d is the private key, n is the value of n in the public key, y is the encrypted message
    private_key = (d, n)
    text=y.split(',')
    x = ""                  # x is the encrypted message (string)
    m = 0                   # m is the encrypted message (int)
    # Generate the plaintext based on the y and key using y^d mod n
    for i in text:
        if(int(i) == 400):
            x+=' '
        else:
            m = (int(i)**d)%n
            m += 65
            c = chr(m)
            x += c
    return x

# Main Program
def main(): 
    y = input("Input encryption message using (,)):  ")
    print("\nYour decryption message:", y)
    
    encryption_message= rsaDecryption(d, n, y)

    print("\nHere is your Decryption Message: ", encryption_message)
    print("============ Done =============")
    
    return encryption_message

main()