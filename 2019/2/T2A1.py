def runProgramm(program):
    programmCounter = 0
    while (programmCounter < len(program)):
        optCode = int(program[programmCounter])
        if (optCode==99):
            return program
        else:
            inputIndex1 = int(program[programmCounter + 1])
            inputIndex2 = int(program[programmCounter + 2])
            resultIndex = int(program[programmCounter + 3])
            try:
                if (optCode==1):
                    program[resultIndex] = program[inputIndex1] + program[inputIndex2]
                elif (optCode==2):
                    program[resultIndex] = program[inputIndex1] * program[inputIndex2]
                else:
                    return program
            except IndexError:
                return program
        programmCounter+=4



fobj = open("input2.txt","r")
for line in fobj:
    program = line.split(",")
    for i in range(0, len(program)):
        program[i] = int(program[i])
    targetValue = 19690720

    for i in range(1000):
        for j in range(1000):
            noun = i
            verb = j
            program[1] = noun
            program[2] = verb
            result = runProgramm(program.copy())
            if (result[0]==targetValue):
                print("noun:", noun, " ,verb:", verb, "100 * noun + verb=", (100 * noun + verb))

fobj.close()
