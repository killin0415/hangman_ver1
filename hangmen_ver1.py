import random
import os
import time

def answer_library(key):#題庫
    hard="pneumonoultramicroscopicsilicovolcanoconiosis,rythem,fertilizer,phelebotomist,authority,synchronize,ligase,primase,photosynthesis,philosophy,oblivion,abstract,volume"
    answer_dict={
        1:[None],#簡單
        2:[None],#中等
        3:hard.split(","),#困難
        4:['female','region','regional','forbid','continue','continous','education','educational','educate','principal','equal','equality','control','annoy','threaten','threat','surgery','recover','recovery','sign','persuade','persuasion','persuasive','adopt','policy','ensure','establish','establishment','recieve','honor','honorable','weapon'],#課內
        5:[None]#雜誌
    }
    return answer_dict[key]
def display_hangmen(tries):#圖像輸出(目前別動
    hangmen=["""
            ------﹁
            |      
            |    
            |      
            |     
            |
           ---
            """,  
            """
            ------﹁
            |      O
            |    
            |      
            |     
            |
           ---
            """,    
            """   
            ------﹁
            |      O
            |      | 
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | 
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     /
            |
           ---
            """,
            """    
            ------﹁
            |      O
            |    \\ | /
            |      |
            |     / \\
            |
           ---
            """  
    ]
    return hangmen[tries]
def play():#遊玩主程式
    global depend
    global Answer_list
    Try=0
    answer_list=list(answer)
    display_answer=["_ "for i in range(len(answer))]
    letter_list=[]

    while Try<6:
        final_answer="".join(display_answer)

        if final_answer.isalpha() and final_answer==answer:
            os.system("cls")
            print("Congradulation,you have solved the qustion")
            print("the answer is " ,answer)
            os.system("pause")
            break
        os.system("cls")
        print("you have finished these word:{}".format(",".join(Answer_list)))
        print("your score is {}".format(score))
        if len(letter_list)>0:
            print("you have guessed these word:"+",".join(letter_list))
        print(display_hangmen(Try))
        print("".join(display_answer))
        respond=input("please input a letter or word: ")
        if respond.isalpha() and len(respond)==1:
            if respond not in answer_list:
                print(respond,"is not in word,please try it again")
                Try+=1
                letter_list.append(respond)
                print("\n")
                time.sleep(0.3)
                os.system("pause")
            
            else:
                while respond in answer_list:
                    display_answer[answer_list.index(respond)]=respond
                    answer_list[answer_list.index(respond)]=0
                print (respond.upper(),"is in the answer")
                letter_list.append(respond)
                print("\n")
                time.sleep(0.3)
                os.system("pause")

        elif respond.isalpha() and len(respond)==len(answer):
            if respond==answer:
                
                print("Congradulation,you have solved the qustion")
                print("the answer is " ,answer)
                os.system("pause")
                break

            else:
                print("you guess the wrong answer,plese try it again ")
                Try+=1
                time.sleep(0.3)
                os.system("pause")

        else:
            print("this input is not valid...please input again!")

    if Try==6:
        os.system("cls")
        print(display_hangmen(Try))        
        print("the hangmen is dead...I feel sorry about that,god bless you")
        print("the answer is " ,answer)
        os.system("pause")
        depend=0
score=0
depend=1
while True:
    Answer_list=["nothing"]
    print("please enter the level that you want to play.")
    choice=int(input("(1):easy (2):normal (3):hard (4):text book (5):magazine"))
    answer_copy=answer_library(choice)
    while True:
        os.system("cls")
        answer=random.choice(answer_copy)
        print(display_hangmen(0))
        print("_ "*len(answer))
        play()
        answer_copy.remove(answer)
        if depend==0:
            break
        else:
            score+=1
            if score==1:
                Answer_list[0]=answer
            else:
                Answer_list.append(answer)
        if len(answer_copy)==0:
            print("Congradulation!you have solved all the questions in this level")
            break
    print("your score is {}".format(score))