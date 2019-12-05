import pprint
def main():
    str = """ this is a long Line
    of code"""
    dict = {}
    for i in str:
        dict.setdefault( i , 0 )
        dict[i] = dict[i] + 1
    pprint.pprint(dict)    
main() 