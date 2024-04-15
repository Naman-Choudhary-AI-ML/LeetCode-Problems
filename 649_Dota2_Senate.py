"""
Problem Statement: 

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        ans = [True] * len(senate)
        rs = senate.count("R")
        ds = len(senate) - rs
        curr = 0

        def ban(toban, start, lst) :
            point = start
            while True :
                if senate[point] == toban and lst[point] == True:
                    lst[point] = False
                    break
                point = (point + 1) % len(senate)


        while rs > 0 and ds > 0 :
            if ans[curr] == True and senate[curr] == "R" :
                ban("D", (curr + 1) % len(senate), ans)
                ds -= 1
            elif ans[curr] == True and senate[curr] == "D":
                ban("R", (curr + 1) % len(senate), ans)
                rs -= 1
            curr = (curr + 1) % len(senate)
        
        return "Radiant" if ds == 0 else "Dire"