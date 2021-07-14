def split_and_join(a):
    delimiter='-'
    a = a.split(" ") 
    a = delimiter.join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
