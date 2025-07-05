def split_and_join(line):
    sp = line.split()
    
    ans ="-".join(sp)
    return ans
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
