def main():

    rev_string = ''
    string = input('Please provide a string to reverse: ')
    str_len = len(string)
    for i in range(str_len - 1, -1, -1):
        rev_string += string[i]
    print(rev_string)


if __name__ == '__main__':
    main()
