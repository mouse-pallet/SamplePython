def IsPalindrome(word):
 count =0
 num=0
 li=list(word)
 reli=list(reversed(word))
 for num in range(0,len(li)):
    if li[num]!=reli[num]:
        return (''.join(reli))+(':False')
 return 'Trne'



print(IsPalindrome('moom'))   
print(IsPalindrome('dog')) 
