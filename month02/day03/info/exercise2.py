def find_words(word):
    d = open("dict.txt")
    for line in d:
        w = line.split(" ")[0]
        if w > word:
            print("单词不存在")
            break
        if w == word:
            print(line)
            break
    else:
        print("单词不存在")
    d.close()


if __name__ == "__main__":
    word = input("word:")
    find_words(word)
