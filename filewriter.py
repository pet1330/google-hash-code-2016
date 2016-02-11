#commands is a list, st

def filewriter(commands):
    with open("ans", "w") as file:
        file.write(len(commands))
        for i in xrange(len(0, commands)):
            if commands[i][1] != "L" and commands[i][1] != "U" and commands[i][1] != "W" and commands[i][1] != "D":
                    raise ValueError("Invalid letter in command: " + str(i))
            file.write('%s %s %s %s %s' % i[0],i[1],i[2],i[3],i[4])
