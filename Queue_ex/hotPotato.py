from myapp.structure import Queue


def hotpotato(names: list, num: int) -> str:
    """通过队列解决热土豆问题"""
    contingent = Queue()
    for name in names:
        contingent.enqueue(name)

    for time in range(num):
        contingent.enqueue(contingent.dequeue())

    while not contingent.size() > 1:
        contingent.dequeue()

    return contingent.dequeue()


if __name__ == '__main__':
    print(hotpotato(['Tom', 'Jake', 'Jhon', 'Ben'], 7))
