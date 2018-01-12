#! usr/bin/python3


tictac={'l-t':' ','m-t':' ','r-t':' '
        'l-m':' ','m-m':' ','r-m':' '
        'l-b':' ','m-b':' ','r-b':' '}
def board(x)
    print(x['l-t']|x['m-t']|x['r-t']) 
    print("--------------")                                         
    print(x['l-m']|x['m-m']|x['r-m'])
    print("--------------")
    print(x['l-b']|x['m-b']|x['r-b'])
board(tictac)