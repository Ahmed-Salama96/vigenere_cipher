import re
import string

alphabets = "abcdefghijklmnopqrstuvwxyz" # this is the english letters
def encrypt(p, k):
    c = ""
    kpos = [] # return the index of characters ex: if k='d' then kpos= 3
    for x in k:
       # kpos += alphabets.find(x) #change the int value to string
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i] #find the number or index of the character and perform the shift with the key
      print(pos)
      if pos > 25:
          pos = pos-26               # check you exceed the limit
      c += alphabets[pos].capitalize()  #because the cipher text always capital letters
      i +=1
    return c

def decrypt(c, k):
    p = ""
    kpos = []
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in c:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x.lower()) - kpos[i]
      if pos < 0:
          pos = pos + 26
      p += alphabets[pos].lower()
      i +=1
    return p
try:
    print("Welcome to vigenere cipher.\n\n"
          "The text message should contain only characters and the key should be one character word \n"
          "Press 1 to Enrypt a message \npress 2 to Decrypt a message")
    choose = input("Choice: ")
    if choose == '1':
       p = input("enter the plain text: ")
       p = p.replace(" ", "")  # this will make sure that there is no space in the message
       if p.isalpha():
           k = input("Enter the key: ")
           k = k.strip()  # remove the white spaces from both sides
           if k.isalpha():
              # print(k)
               c = encrypt(p, k)
               print("The cipher text is: ", c)

           else:
               print(k)
               print("Enter valid key, key is only one character word!")
       else:
           print("only letters are allowed !!")

    elif choose == '2':
        c = input("enter the cipher text: ")
        c = c.replace(" ", "")
        if c.isalpha():
            k = input("Enter the key: ")
            if not k.isalpha():
                print("Enter valid key, key is only one character word!")
            else:
                p = decrypt(c, k)
                print("The plain text is: ", p)
        else:
            print("only letters are allowed!")

    else:
        print("Please enter a valid choice!")
except Exception as e:
    print(e)
    exit("Enter a valid text please! ")