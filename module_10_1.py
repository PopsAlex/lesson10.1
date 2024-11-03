import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = time.time()

print(f'Работа потоков: {time.strftime("%H:%M:%S", time.gmtime(end - start))}')

start = time.time()

thread1 = threading.Thread(target=write_words, args= (10, 'example5.txt',))
thread2 = threading.Thread(target=write_words, args= (30, 'example6.txt',))
thread3 = threading.Thread(target=write_words, args= (200, 'example7.txt',))
thread4 = threading.Thread(target=write_words, args= (100, 'example8.txt',))

funcs2 = [thread1, thread2, thread3, thread4]

for i in funcs2:
    i.start()
for j in funcs2:
    j.join()

end = time.time()

print(f'Работа потоков: {time.strftime("%H:%M:%S", time.gmtime(end - start))}')