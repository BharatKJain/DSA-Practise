def check(word, main_word):
    index_list=[-1 for element in word]
    for index in range(0,len(word)):
        if word[index]==main_word[index]:
            index_list[index]=1
    return index_list

def find_answer(index_list,word,main_word,list_of_words,mem):
    minimum_ans=-1
    answer=0
    final_word=""
    # print(f"word {word}, main_word {main_word}")
    for index in range(len(word)):
        if index_list[index]==-1:
            modified_string=list(word)
            modified_string[index]=main_word[index]
            # print("".join(modified_string))
            copy_index_list=index_list.copy()
            copy_index_list[index]=1
            # print("".join(modified_string))
            if "".join(modified_string) == main_word:
                return 1
            if "".join(modified_string) in mem:
                return mem["".join(modified_string)]
            if "".join(modified_string) in list_of_words :
                fetch_data=find_answer(copy_index_list,"".join(modified_string),main_word,list_of_words,mem)
                mem["".join(modified_string)]=fetch_data
                # print(f"fetch data value={fetch_data}")
                # print("".join(modified_string))
                if fetch_data<minimum_ans or minimum_ans==-1:
                    minimum_ans=fetch_data+1
                    # print("".join(modified_string))
    return minimum_ans
if __name__=="__main__":
    word=input()

    actual_word=input()
    n=input()
    for _ in range(n):
        list_of_words.append(input())
    ################
    # word="git"
    # actual_word="dog"
    # list_of_words=["got","dot","log","fot","mot","pkm"]
    ############
    mem={}
    if word==actual_word:
        print(0)
    else:
        list_data=check(word,actual_word)
        print(find_answer(list_data,word,actual_word,list_of_words,mem))
