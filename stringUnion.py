#Diego Aspinwall
#10-20-17
#stringUnion.py

def stringUnion(word1,word2):
    ans = ''
    megaword = str.lower(word1+word2)
    for ch in megaword:
        if ch not in ans:
            ans += ch
    print(ans)

stringUnion('Mississippi','Pennsylvania')