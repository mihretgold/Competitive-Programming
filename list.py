if __name__ == '__main__':
    N = int(input())
    list_command = []
    for index in range(N):
        command = input().split()
        if command[0] == 'insert':
            i = int(command[1])
            e = int(command[2])
            list_command.insert(i, e)
        elif command[0] == 'print':
            print(list_command)
        elif command[0] == 'remove':
            e = int(command[1])
            list_command.remove(e)
        elif command[0] == 'append':
            e = int(command[1])
            list_command.append(e)
        elif command[0] == 'sort':
            list_command.sort()
        elif command[0] == 'pop':
            list_command.pop()
        elif command[0] == 'reverse':
            list_command.reverse()
        
