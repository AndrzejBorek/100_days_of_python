from pickle import FALSE, TRUE


t = TRUE
f = FALSE

if t and f == TRUE:
    print("true")
else:
    print("false")

if t or f == TRUE:
    print("true")
else:
    print("false")

if not t and f == TRUE:
    print("true")
else:
    print("false")

if not t and not f == TRUE:
    print("true")
else:
    print("false")