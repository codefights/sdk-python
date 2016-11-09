# Codefights.net SDK for Python 2.7

### About
Visit [codefights.net](http://www.codefights.net/) to learn more about this fun project.

### Installation
#### Using PyPI
```
pip install codefights
```
or
```
easy_install codefights
```
#### Without using PyPI
Download this package to /your/desired/path.

Install it:
```
cd </your/desired/path/>sdk-python/
sudo python setup.py install
```

### Writing your first bot
Developing a simple bot for a Codefights.net tournament is really easy.

We have prepared a simple demo bot - save it as YourFighterName.py and you are ready!

```
from codefights.model.IFighter import *
import codefights.boilerplate.SDK
import sys

class MyFighter (IFighter):
    """
    analyze your opponent's last move and make your next move
    :returns fighter's next Move
    NOTE: rules allow max 3 actions per Move.
    I.e. attack nose (1), attack groin (2) and defend nose (3).
    The areas are:
    +------------+---------+
    | Area.NOSE  | (10pts) |
    |------------+---------|
    | Area.JAW   | (8pts)  |
    |------------+---------|
    | Area.BELLY | (6pts)  |
    |------------+---------|
    | Area.GROIN | (4pts)  |
    |------------+---------|
    | Area.LEGS  | (3pts)  |
    +------------+---------+
    """

    def make_next_move(self,
                       opponents_last_move=None,
                       my_last_score=0,
                       opponents_last_score=0):
        """
        You must implement make_next_move method in MyFighter class.
        Feel free to create helper classes in this file.
        """
        move = Move()

        move.add_attack(Area.NOSE).add_block(Area.GROIN).add_attack(Area.BELLY)

        return move


# DO NOT EDIT THE LINES BELOW!
if __name__ == '__main__':
    codefights.boilerplate.SDK.SDK.run(MyFighter, sys.argv)
```

### Testing your bot
Run it
```
python </path/to/fighter/>YourFighterName.py
```
and follow instructions.

---
©  Visma Lietuva
