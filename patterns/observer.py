"""
Intent
    Observer is a behavioral design pattern
    Lets you define a subscription mechanism to notify multiple objects about any events that happen
    to the object they’re observing.

Example
    Someone who subscribe to a newspaper or magazine, no longer need to go to the store to
    check if the next issue is available. Instead, the publisher sends new issues directly
    to his mailbox right after publication or even in advance.

Pros
    Open/Closed Principle.
    You can introduce new subscriber classes without having to change the publisher’s code
    You can establish relations between objects at runtime.

Cons
    Subscribers are notified in random order.

Reference
    https://refactoring.guru/design-patterns/observer
    https://www.protechtraining.com/blog/post/tutorial-the-observer-pattern-in-python-879

"""


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Publisher:
    def __init__(self, events):
        self.events = {event: dict()
                       for event in events}

    def get_subscribers(self, event):
        return self.events[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


def main():
    pub = Publisher(['lunch', 'dinner', 'breakfast'])
    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')

    pub.register("lunch", bob)
    pub.register("dinner", alice)
    pub.register("lunch", john)
    pub.register("dinner", john)

    pub.dispatch("lunch", "It's lunchtime!")
    pub.dispatch("dinner", "Dinner is served")


if __name__ == '__main__':
    main()
