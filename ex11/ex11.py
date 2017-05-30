# Exercise 11, page 102
# Reads a file of states for an enum and creates a c file and a header file containing the names
import sys
def wrap(str):
    return '\"' + str + '\"'
if len(sys.argv) == 2:
    filename = sys.argv[1]
    lines = [line.rstrip('\n') for line in open(filename)]
    typename = lines[0]
    cfile = open(typename + '.c', 'w')
    hfile = open(typename + '.h', 'w') # TODO: check for erroneous filename characters
    typename_ups = typename.upper()
    sharedObject =  'const char* ' + typename_ups + '_' + typename + 's[]'
    cfile.write(sharedObject + ' = {\n')
    hfile.write('extern ' + sharedObject + ';\ntypedef enum {\n')
    if len(lines) > 1:
        hfile.write(lines[1])
        cfile.write(wrap(lines[1]))
        stop = ',\n'
        for i in range(2, len(lines)):
            line = lines[i]
            hfile.write(stop + line)
            cfile.write(stop + wrap(line))
        hfile.write('\n} ' + typename_ups + ';\n')
        cfile.write('\n};\n')
#
#    for i in range(1, len(lines)):
#
#else:
#    raise Exception('Please give me some input!')
