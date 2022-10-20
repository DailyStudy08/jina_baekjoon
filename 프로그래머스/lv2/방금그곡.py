m='ABCDEFG'
musicinfos=["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
import datetime 
def solution(m, musicinfos):
    answer = '(None)'
    for music in musicinfos:
        start,end,title,code=music.split(',')
        start=datetime.datetime.strptime(start,"%H:%M")
        end=datetime.datetime.strptime(end,"%H:%M")
        time=(end-start).seconds//60 #재생시간
        for c in code:
            if c=='#':
                time+=1
        play_code=''
        i=0
        len(code)
        while time>0:
            if i>len(code)-1:
                i=0
            play_code+=code[i]
            i+=1
            time-=1
        if code in play_code:
            answer=title
    return answer
print(solution(m,musicinfos))