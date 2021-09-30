import os.path
import shlex
import re,pdb
code_file="cpp_code.txt"
f = open('3.txt','w')
brace = 0
TYPE=0
NAME=1
DEFAULT_VAL=2
COMMENT=3
parsed_line=[None]*4

lines_to_file=[]

for line in open(code_file).readlines():
    # comments
    striped_line=shlex.split(line)
    # print(len(striped_line), striped_line)
    if len(striped_line)<3:
        continue
    # stop_chars=['{','}','define']
    # res = any(ele in stop_chars for ele in striped_line)
    # if res:
    #     continue
    if '//' or '/*' in line:
        for i,word in enumerate(striped_line):
            # parse comments

            if word=='//' or word=='/*':
                parsed_line[COMMENT]=' '.join(striped_line[i+1:])
                # continue with the left part only
                striped_line=striped_line[0:i]
                continue


    else:
        parsed_line[COMMENT]='No comments'

    for i,word in enumerate(striped_line):
        # parse default values
        if '=' in word:
            # print(word,striped_line)
            parsed_line[NAME]=striped_line[i-1]
            parsed_line[DEFAULT_VAL]=striped_line[i+1]
            parsed_line[TYPE]=' '.join(striped_line[:i-2])

    else:
        # print(parsed_line)
        parsed_line[NAME]=striped_line[-1]
        if len(striped_line[:-1])>1:
            parsed_line[TYPE]=' '.join(striped_line[:-1])
        parsed_line[TYPE]=' '.join(striped_line[:-1])

    print('type: {}\tname: {}\tdef {}\tcomments {}'.format(parsed_line[0],parsed_line[1],parsed_line[2],parsed_line[3]))
    lines_to_file.append(parsed_line)
    # reset array
    parsed_line=[None]*4

head, tail = os.path.split(code_file)
tail=os.path.splitext(tail)[0]
tail="parsed_{}.csv".format(tail)
outputfile=os.path.join(head,tail)
print(lines_to_file)

outF = open(outputfile, "w")
for line in lines_to_file:
    # write line to output file
    outF.write(str(line))
    outF.write("\n")
outF.close()