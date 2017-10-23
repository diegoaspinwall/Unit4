#Diego Aspinwall
#10-22-17
#stringIntersect.py

def stringIntersect(word1,word2):
    ans = ''
    for ch in word1:
        if ch in word2:
            ans += ch
    print(ans)

stringIntersect('Mississippi','Pennsylvania')
