import tkinter as tk
import tkinter.ttk as ttk
import json
"""system"""
i=0
e=0
answer=0
fonttext=("MSゴシック", "20", "bold")
yes=0
button2=""
button3=""
file1 = open('data.json', 'r',encoding="utf-8")#json read
jsons = json.load(file1)#json化
print(jsons)
def b1():
    global i,jsons,answer
    global button2,button3
    if i==0:
        answer+=1
        button2 = tk.Button(text=jsons[answer-1]["1"],width=20,height=6,command=b2)#ボタン
        button2.grid()
        button3 = tk.Button(text=jsons[answer-1]["2"],width=20,height=6,command=b3)#ボタン
        button3.grid()
        label2["text"] = str(answer)+"問目、"+jsons[0]["text"]
        i+=1
def b2():
    global jsons,answer,yes,e
    global button2,button3
    if not answer>=len(jsons):
        if e==0:
            if jsons[answer-1]["answer"]=="1" :
                yes+=1
        answer+=1
        print(answer)
        label2["text"] = str(answer)+"問目、"+jsons[answer-1]["text"]
        button2["text"]=jsons[answer-1]["1"]
        button3["text"]=jsons[answer-1]["2"]
    else:
        if e==0:
            if jsons[answer-1]["answer"]=="1":
                yes+=1
                print()
        answer+=1
        e=1
        if not yes==len(jsons):
            label2["text"] = "あなたの正解数は"+str(yes)+"もんです"
        else:
            label2["text"] = "全問正解!!あなたの正解数は"+str(yes)+"もんです"
def b3():
    global jsons,answer,yes,e
    global button2,button3
    print(answer,"あ")
    print(not answer>=len(jsons))
    if not answer>=len(jsons):
        if e==0:
            if jsons[answer-1]["answer"]=="2" :
                yes+=1
                print()
        answer+=1
        print(jsons[answer-1]["answer"])
        label2["text"] = str(answer)+"問目、"+jsons[answer-1]["text"]
        button2["text"]=jsons[answer-1]["1"]
        button3["text"]=jsons[answer-1]["2"]
    else:
        if e==0:
            if jsons[answer-1]["answer"]=="2":
                yes+=1
                print()
        answer+=1
        e=1
        if not yes==len(jsons):
            label2["text"] = "あなたの正解数は"+str(yes)+"もんです"
        else:
            label2["text"] = "全問正解!!あなたの正解数は"+str(yes)+"もんです"
    
        
"""GUI"""
root = tk.Tk()
root.title("教育アプリ:quipe(キピ)")#title
root.geometry("640x580")#size

"""gui main"""
label = tk.Label(root, text="quipe",font=("MSゴシック", "50", "bold"))#テキスト
label.grid()#表示する
button1 = tk.Button(text="start",width=20,height=6,command=b1)#ボタン
button1.grid()
label2 = tk.Label(root, text=None,font=fonttext)#テキスト
label2.grid()

root.mainloop()  
