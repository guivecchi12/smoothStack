# Coding Exercise 3
def main():
    # 1. write a string that returns the letter 'r' from 'Hello World"
    'Hello World'[8]

    # 2. String slicing to grab the word 'ink' from the word 'thinker'
    'thinker'[slice(2,5)]

    # S='hello', what is the output of h[1]
        # you would get an error since h is not defines, S[1] would give you 'e'

    # 3. S='Sammy' what is the output of s[2:]
        # this would also give you an error since variables are case sensitive and we declaired S as our variable and not s. On the other hand S[2:] would return 'mmy'.

    # 4. With a single set function can you turn the word 'Mississippi' to distinct character word.
    set('Mississippi')

    # 5. Check for palindrome
    def palindrom(a):
        answer = []
        for s in a:
            if type(s) is not int:
                check = str(s).replace(" ", "").replace(',', '').replace('!', '').lower()
                print(check)

                if check == check[::-1]:
                    answer.append('Y')
                else:
                    answer.append('N')
        return answer
    
    print(palindrom([3, 'Stars', 'O, a kak Uwakov lil vo kawu kakao!', 'Some men interpret nine memos']))

main()