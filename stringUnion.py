#Diego Aspinwall
#10-20-17
#stringUnion.py

def stringUnion(word1,word2):
    ans = ''
    megaword = word1+word2
    for ch in megaword:
        if ch not in megaword:
            ans += ch
    print(ans)

stringUnion('yo','momma')