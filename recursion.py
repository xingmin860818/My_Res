def func(N):
        if N <= 1:
                return 1
        else:
                return func(N-2)+func(N-1)
