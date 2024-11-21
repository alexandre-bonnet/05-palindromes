'''
this method returns 'true' or 'false' 
depending on if the string in parameter is a palindrome
'''
def ispalindrome(s):
    '''
    this method returns 'true' or 'false' 
    depending on if the string in parameter is a palindrome
    '''
    s = s.lower()
    accents = str.maketrans('àéèëêçûô','aeeeecuo')
    s = s.translate(accents)
    sprime = ""
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z')or(s[i]>='0' and s[i]<='9'):
            sprime += s[i]
    print(sprime)
    for i in range (int(len(sprime)/2)+1):
        if sprime[i] != sprime[-(i+1)]:
            return False
    return True

#### Fonction principale


def main():
    '''
    this method returns is calling the palindrome() one
    '''

    for s in ["radar", "kayak", "level", "rotor", "civique",]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
