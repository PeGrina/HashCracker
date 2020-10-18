#!usr/bin/python3
# -*- coding utf-8 -*-

# =========================== Hash cracker.py ==========================
# |                          Made by: CBStudio                         |
# |                Cracking some hashes with bruteforce                |
# |                                                                    |
# |                            Commands:                               |
# |  crack (c) -t <type of hash> -h <hash> -w <path to wordlist>       |
# |  add (a) -w <path to wordlist> -d <dictionary> -l <length>         |
# ======================================================================

global S, N, Out, In
S, N, Out, In = ["", 0, [], []]

import sys
import time
import hashlib
argv0 = sys.argv[1:]
start = float(time.time())
command = argv0[0]

# -*- MD5 hex func -*-
def hashing(s, type):
    if(type == 'md5'):
        return hashlib.md5(s.encode('ascii')).hexdigest()

# -*- Recursing all strings of global S: string to global Out: dict -*-
def rec(idx: int):
    if idx == N:
        Out.append("".join(In))
        return
    else:
        for i in S:
            In[idx] = i
            rec(idx + 1)

if command == 'help':
    print('=========================== Hash cracker.py ==========================')
    print('|                          Made by: CBStudio                         |')
    print('|                Cracking some hashes with bruteforce                |')
    print('|                                                                    |')
    print('|                            Commands:                               |')
    print('|  crack (c) -t <type of hash> -h <hash> -w <path to wordlist>       |')
    print('|  add (a) -w <path to wordlist> -d <dictionary> -l <length>         |')
    print('|  hash (h) -t <type of hash> -w <word>                              |')
    print('======================================================================')

if command in ['hash', 'h']:
    argv0, word, type = [argv0[1:], "", ""]

    for arg in argv0:
        if arg == '-w':
            next_arg = 'word'
            continue
        elif arg == '-t':
            next_arg = 'type'
            continue
        if next_arg == 'word':
            word = arg
        elif next_arg == 'type':
            type = arg

    print(hashing(word, type))

if command in ['add', 'a']:
    argv0, path, d, l = [argv0[1:], "", "", 0]


    for arg in argv0:
        if arg == '-w':
            next_arg = 'path'
            continue
        elif arg == '-d':
            next_arg = 'dict'
            continue
        elif arg == '-l':
            next_arg = 'length'
            continue
        if next_arg == 'path':
            path = arg
        elif next_arg == 'dict':
            d = arg
        elif next_arg == 'length':
            l = int(arg)

    wordlist = open(path, 'a')
    S, N = [d, l]
    In = [d[0]] * l
    rec(0)
    wordlist.write("\n".join(Out))
    print("===========================")
    print("Appended files: {}".format(len(Out)))
    end = float(time.time())
    print("Time wasted: {} sec.".format(round((end-start)*100)/100))

if command in ['crack', 'c']:
    argv0, type, hash, path = [argv0[1:], "", "", ""]


    for arg in argv0:
        if arg == '-t':
            next_arg = 'type'
            continue
        elif arg == '-h':
            next_arg = 'hash'
            continue
        elif arg == '-w':
            next_arg = 'path'
            continue
        if next_arg == 'type':
            type = arg
        elif next_arg == 'hash':
            hash = arg
        elif next_arg == 'path':
            path = arg

    ans = False
    wordlist = open(path, 'r+').read().split('\n')
    hashes = open('hashes.txt', 'a')
    hashe = open('hashes.txt', 'r+').read().split('\n')
    for line in hashe:
        if(line.split(':')[0] == hash):
            ans = line.split(':')[1]
            break
    if not(ans):
        for line in wordlist:
            if line == '\n':
                continue
            elif hashing(line, type) == hash:
                ans = line
                hashes.write(hash + ":" + line + "\n")
                break

    print("===========================")
    if(ans):
        print("Hash: {}".format(ans))
    else:
        print("Hash don't cracked")
    print("Checked words: {}".format(len(wordlist)))
    end = float(time.time())
    print("Time wasted: {} sec.".format(round((end-start)*100)/100))
