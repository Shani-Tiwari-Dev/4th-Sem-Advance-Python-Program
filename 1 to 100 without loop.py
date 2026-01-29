def loop(n):
    if n > 100:
        return
    print(n)
    loop(n+1)


loop(1)
