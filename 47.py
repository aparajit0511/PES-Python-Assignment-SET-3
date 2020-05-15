def foo(tuples,lists):
    tuples = list(tuples)

    tuples.extend(lists)

    print(tuple(tuples))

foo((1,2,3),[4,5,6])