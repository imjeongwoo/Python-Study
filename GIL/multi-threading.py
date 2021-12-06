import random, datetime, threading, time
 
 
def calc():
    max([random.random() for i in range(5000000)])
    max([random.random() for i in range(5000000)])                                 
    max([random.random() for i in range(5000000)])
 
 
# 1 Thread : 하나의 쓰레드에서 두 개의 함수를 연속적으로 실행
start_time = datetime.datetime.now()
calc()
calc()
end_time = datetime.datetime.now()
print(f'1 Thread : {end_time - start_time}')
 
 
# 2 Threads : 쓰레드 두 개를 생성해서 쓰레드에서 각각 하니씩 실행
start_time = datetime.datetime.now()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=calc))
    threads[-1].start()
 
for t in threads:
    t.join()
 
end_time = datetime.datetime.now()
print(f'2 Threads : {end_time - start_time}')