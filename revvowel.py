x=raw_input()
y=raw_input()
def anti_vowel(text):
    for i in "aeiouAEIOU":
        text=text.replace(i,' ')
    return text
z=anti_vowel(y)
w=z[::-1]
print(w)
