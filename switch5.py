ch=input("Enter any Character : ")
match ch.lower():
      case 'a'|'e'|'i'|'o'|'u':
            print("Vowel")
      case _ :
            print("Consonant")
