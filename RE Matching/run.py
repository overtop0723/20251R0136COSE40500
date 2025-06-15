#!/usr/bin/python3

import os
import sys

###########################################
# Your regex pattern runs in this function!
# Return the matching result as a string
###########################################
def regex_play(str, prob_idx):
    result = ""
    if prob_idx == '1':
        print("==problem1==")
        temp = re.findall("^[hH][tT][tT][pP][sS]?:\/\/[wW][wW][wW][.][cC][yY][wW][oO][rR][lL][dD][.][cC][oO][mM]\/[A-Za-z]*[A-Za-z]$|^[hH][tT][tT][pP][sS]?:\/\/[wW][wW][wW][.][fF][aA][cC][eE][bB][oO][oO][kK][.][cC][oO][mM]\/[A-Za-z]*[A-Za-z]$|^[hH][tT][tT][pP][sS]?:\/\/[wW][wW][wW][.][iI][nN][sS][tT][aA][gG][rR][aA][mM][.][cC][oO][mM]\/[A-Za-z]*[A-Za-z]$|^[hH][tT][tT][pP][sS]?:\/\/[wW][wW][wW][.][tT][wW][iI][tT][tT][eE][rR][.][cC][oO][mM]\/[A-Za-z]*[A-Za-z]$", str) 
        if temp: result = temp.pop() 
    elif prob_idx =='2':
        print("==problem2==")
        temp = re.findall("^(?:(?:1[0-9][0-9]|2[0-4][0-9]|25[0-5]|[1-9]?[0-9])[.]){3}(?:(?:1[0-9][0-9]|2[0-4][0-9]|25[0-4]|[1-9]?[0-9])$)|^(?:(?:[0-9]{4})-){3}(?:[0-9]{4})$|^[A-Za-z][A-Za-z0-9_.]*@[a-z]+[.](?:ac[.]kr|com|net|co[.]kr)$", str) 
        if temp: result = temp.pop() 
    elif prob_idx =='3':
        print("==problem3==")
        temp = re.findall("^((?![~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?0-9A-Za-z]*(1{3,}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}|0{3}|a{3}|b{3}|c{3}|d{3}|e{3}|f{3}|g{3}|h{3}|i{3}|j{3}|k{3}|l{3}|m{3}|n{3}|o{3}|p{3}|q{3}|r{3}|s{3}|t{3}|u{3}|v{3}|w{3}|x{3}|y{3}|z{3}|A{3}|B{3}|C{3}|D{3}|E{3}|F{3}|G{3}|H{3}|I{3}|J{3}|K{3}|L{3}|M{3}|N{3}|O{3}|P{3}|Q{3}|R{3}|S{3}|T{3}|U{3}|V{3}|W{3}|X{3}|Y{3}|Z{3}|[~]{3}|[`]{3}|[!]{3}|[@]{3}|[#]{3}|[$]{3}|[%]{3}|[\^]{3}|[&]{3}|[*]{3}|[(]{3}|[)]{3}|[\-]{3}|[_]{3}|[+]{3}|[=]{3}|[{]{3}|[}]{3}|[\[]{3}|[\]]{3}|[|]{3}|[\\]{3}|[\/]{3}|[:]{3}|[;]{3}|[\"]{3}|[']{3}|[<]{3}|[>]{3}|[,]{3}|[.]{3}|[?]{3}|^[A-za-z]*$|^[0-9]*$|^[~`!@#$%^&*()\_+={}\[\]|\\\/:;\"'<>,.?]*$)[~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?0-9A-Za-z]*)([~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?0-9A-Za-z]{8,}))|^((?![~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?0-9A-Za-z]*(1{3,}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}|0{3}|a{3}|b{3}|c{3}|d{3}|e{3}|f{3}|g{3}|h{3}|i{3}|j{3}|k{3}|l{3}|m{3}|n{3}|o{3}|p{3}|q{3}|r{3}|s{3}|t{3}|u{3}|v{3}|w{3}|x{3}|y{3}|z{3}|A{3}|B{3}|C{3}|D{3}|E{3}|F{3}|G{3}|H{3}|I{3}|J{3}|K{3}|L{3}|M{3}|N{3}|O{3}|P{3}|Q{3}|R{3}|S{3}|T{3}|U{3}|V{3}|W{3}|X{3}|Y{3}|Z{3}|[~]{3}|[`]{3}|[!]{3}|[@]{3}|[#]{3}|[$]{3}|[%]{3}|[\^]{3}|[&]{3}|[*]{3}|[(]{3}|[)]{3}|[\-]{3}|[_]{3}|[+]{3}|[=]{3}|[{]{3}|[}]{3}|[\[]{3}|[\]]{3}|[|]{3}|[\\]{3}|[\/]{3}|[:]{3}|[;]{3}|[\"]{3}|[']{3}|[<]{3}|[>]{3}|[,]{3}|[.]{3}|[?]{3})[~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?0-9A-Za-z]*)([~`!@#$%^&*()\-_+={}\[\]|\\\/:;\"'<>,.?]{10,}|[A-Za-z]{10,}))", str) 
        if temp: 
            for i in range(len(temp[0])): 
                if temp[0][i] != "": 
                    result = temp[0][i][:] 
                    break
    else:
        print("[ERROR] WRONG PROBLEM NUMBER")
        exit(1)

    return result

def main(file, prob_idx):
    result  = []
    # open problem file 
    try:
        with open(file, 'r') as f: 
            data = f.read()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    split_data = data.splitlines()

    #Run the regex_play function line by line
    for line in split_data:
        result.append(regex_play(line,prob_idx))
    result = list(filter(None, result))
    w_data = '\n'.join(result)
    
    try:
        with open('output_'+prob_idx+'.txt', 'w', -1, "utf-8") as file: 
            file.write(w_data)
            file.close()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    print(w_data)
    

if __name__ == '__main__':
    if(not sys.argv[1]):
    	print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    if(not sys.argv[2]):
        print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    file = sys.argv[1]
    prob_idx = sys.argv[2]
    main(file, prob_idx)
