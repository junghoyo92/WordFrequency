def stop_words(file_stop):
    stop = []
    for line in file_stop:
        stop += [line.strip('\n')]
    print(stop)


file_stop = open('stopWords.txt')
stop_words(file_stop)
