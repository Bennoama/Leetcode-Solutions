// https://leetcode.com/problems/finding-the-users-active-minutes

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # create integer array of length k with values of 0.
        # create a dictionary that maps between ID and SET of action times
        # go over all logs
        # for each log:
            # if user already in map -> add to set the time of the action
            # else - add the user and create a new set with that time
        # from i = 0 to k:
            # go over all IDs in map, for that ID:
                # if the SET of action times contains i, increase array[i] by 1.

        #return the array.
        uams = [0] * k
        myDict = {}
        temp = []
        for log in logs:
            if (log[0] not in myDict):
                myDict[log[0]] = set()
            myDict[log[0]].add(log[1])
        for user, setOfActions in myDict.items():
             temp.append(len(setOfActions))
        for i in temp:
             uams[i-1] += 1
        
        return uams
            