import string
import random
with open('sponge2.txt', encoding='utf-8') as f:
    text=f.read()
    f.close()
def main(text, wordMax):
    word_dict={}
    translation=str.maketrans('','','"#$%&()*+-/<=>?@[\']^_`{|}~')
    text=text.translate(translation)
    arr=text.split()
    word_dict['']=arr[0]
    for i in range(0,len(arr)-1):
        if arr[i] not in word_dict.keys():
            word_dict[arr[i]]=[]
        word_dict[arr[i]].append(arr[i+1])
    str_out=[arr[0]]
    print(word_dict['because'])
    for i in range(wordMax):
        if str_out[-1]==arr[-1]:
            break
        str_out.append(random.choice(word_dict[str_out[-1]]))
    for word in str_out:
        if word[-1]==':':
            print('\n{0}'.format(word),end=' ')
        else:
            print(word, end=' ')

main(text,200)