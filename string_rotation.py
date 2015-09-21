def str(N):
        if isinstance(N,int):
                return 'wrong type,please input a sting'
        strings = N[::-1]
        if strings == N:
                return True
        else:
                return False
