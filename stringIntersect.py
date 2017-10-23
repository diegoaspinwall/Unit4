#Diego Aspinwall
#10-22-17
#stringIntersect.py

def stringIntersect(word1,word2):
    ans = ''
    for ch in str.lower(word1):
        if ch in str.lower(word2) and ch not in ans:
            ans += ch
    print(ans)

stringIntersect('Mississippi','Pennsylvania')
