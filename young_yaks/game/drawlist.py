from collections import UserList


class DrawList(UserList):
    """ A custom list tweaked to work with objects
    that implement the draw method."""
    def draw(self):
        """ Draw all the items."""
        for item in self.data:
            item.draw()
