from tailrecurse import *


def create_tuple(n):
    if n == 0:
        return ()
    return create_tuple(n-1) + (n,)

#print(create_tuple(995))



def create_tuple_tail(n):
    @tail_call_optimized
    def Tcreate_tuple_tail(n, t):
        if n == 0:
            return t
        return Tcreate_tuple_tail(n-1, t + (n,))
    return Tcreate_tuple_tail(n, ())


print(create_tuple_tail(1000))
tuple1000 = create_tuple_tail(1000)


