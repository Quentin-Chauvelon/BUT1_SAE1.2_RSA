def convert_msg(msg):
    return int(msg)

def encryption(n,priv,msg):
    ms = convert_msg(msg)
    msg = ms.split(step=3)
    for i in msg :
        i*priv%n
    return


encryption(6,5,"salut")