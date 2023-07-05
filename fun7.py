def demo(*data):
    print(data)
    print(data[2])


def demo1(**data):
    print(data)
    print(data['x'])


demo(11,22,33,44,55)

demo1(x=100,y=200,z=300)
