alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encode and type 'decode' to decode:\n")
text = input("typeyour message:\n").lower()
shift= int(input("type the shift number:\n"))

def caesar(dir, plain_text, shift_number):
    new_text = ""
    for letter in plain_text:
        position = alphabet.index(letter) 
        if dir == "encode":
            newposition = position + shift_number  
        elif dir == "decode":
            newposition = position - shift_number
        newletter = alphabet[newposition]
        new_text += newletter
    print(new_text)
caesar(direction,text,shift)
