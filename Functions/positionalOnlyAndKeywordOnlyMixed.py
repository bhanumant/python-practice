

# Positional only and keyword only arguments mixed type of arguments

def fun(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

    print(fun(5,10, c=15, d=20, e=77, f=88))




    def fun3(a, b, c , /, * , d, e, f ):
        print(a, b, c, d, e, f )

        fun3()

