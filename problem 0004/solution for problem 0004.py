def count():
    name = raw_input("Enter file:")
    if len(name) < 1 : name = "mehran.txt"
    handle = open(name)
    count_words=list()
    for line in handle:
        count_words+=line.split()
    return len(count_words)
print count()