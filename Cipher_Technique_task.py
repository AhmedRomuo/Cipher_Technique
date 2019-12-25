ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']


# encryption
def encryption(message, key, space_ch):
    if space_ch.lower() == "no":
        ls.insert(0, ' ')

    ls_message_cipher = []
    len_message = len(message)
    i = 0

    while i < len_message:
        if message[i] == ' ' and space_ch.lower() == "no":
            ls_message_cipher.append(ls[(key + ls.index(message[i])) % len(ls)])
            i += 1
        elif message[i] == ' ':
            i += 1
        else:
            ls_message_cipher.append(ls[(key + ls.index(message[i])) % len(ls)])
            i += 1
    message_str = ""

    for item in ls_message_cipher:
        message_str += item

    print("Cipher Text : " + message_str)
    # print(chr(key))
    # print(message, key, type(key))


# decryption
def decryption(message, key, space_ch):
    if space_ch.lower() == "no":
        ls.insert(0, ' ')

    ls_message_plain_text = []
    len_message = len(message)
    i = 0

    while i < len_message:
        ls_message_plain_text.append(ls[(ls.index(message[i]) - key) % len(ls)])
        i += 1
    message_str = ""

    for item in ls_message_plain_text:
        message_str += item

    print("Plain Text : " + message_str)


def main():
    type_message = int(input("1- Encryption\n2- Decryption\nEnter your choice : "))
    message = input("the message : ")
    key = int(input("key : "))
    space_ch = input("Ignore Space or not : ")
    print(space_ch)
    print("------------------------------")
    if type_message == 1:
        encryption(message, key, space_ch)
    elif type_message == 2:
        decryption(message, key, space_ch)


if __name__ == '__main__': main()
