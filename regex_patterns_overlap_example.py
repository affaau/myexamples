import re

def patternGen(s) :
    convert = '^' + "".join([c if c!='*' else '.?.?.?.?' for c in list(s)]) + '$'
    print(convert)
    return re.compile(convert)

def patternOverlap(p, s):
    m = re.match(p, s)
    return True if m!=None else False
    
    
if __name__ == "__main__":
    s1 = "Shakes*e"
    s2 = "S*speare"
    print (patternOverlap(patternGen(s1), s2))