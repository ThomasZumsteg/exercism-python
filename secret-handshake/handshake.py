
def handshake(secret):

    cipher = [(list.append, ("wink",)),
              (list.append, ("double blink",)),
              (list.append, ("close your eyes",)),
              (list.append, ("jump",)),
              (list.reverse, ()),
             ]
    to_do = []
    for bit, (func, param) in zip(bin_num, cipher):
        if bit == "1":
            func(to_do, *param)
    return to_do
        
def code(shake):
    pass