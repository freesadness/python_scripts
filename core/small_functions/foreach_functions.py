

def foreach(function, collection):
    for i in collection:
        function(i)

def foreach_yield(function, collection):
    for i in collection:
        yield function(i)
