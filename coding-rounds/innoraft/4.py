if __name__ == "__main__":
    flag_invalid=0
    a_count=0
    b_count=0
    winner=0
    counter=0
    counter_var=''
    while(True):
        try:
            character=input()
        except:
            break
        if character=="\n":
            break
        if not (character=='A' or character=='B'):
            flag_invalid=1
        if character=="A":
            a_count+=1
        if character=="B":
            b_count+=1
        if a_count==b_count:
            counter_var=character
            counter+=1
        if counter_var!=character:
            counter=0
        elif counter==2 :
            winner=character
            counter=0
        if counter==0 and abs(a_count-b_count)>=2 and (a_count==4 or b_count==4):
            if a_count > b_count:
                winner="A"
            else:
                winner="B"
    if flag_invalid==1:
        print(">>>Invalid input!!!")
    print(f"Player {winner} wins")