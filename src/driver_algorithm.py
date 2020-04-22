from boyer_moore import *
from kmp import *

pattern = "aba"
text = "abacbacbabacbabcabaabcabcbabcbbacbacacacbababababa"

pattern = "lol"
text = "lolaalolblololclol"

print(kmp(pattern,text))
print(boyer_moore(pattern,text))