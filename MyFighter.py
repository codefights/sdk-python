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
	if not opponents_last_move :	
		return Move().add_attack(Area.NOSE)
	
	return opponents_last_move
        

# DO NOT EDIT THE LINES BELOW!
if __name__ == '__main__':
    codefights.boilerplate.SDK.SDK.run(MyFighter, sys.argv)