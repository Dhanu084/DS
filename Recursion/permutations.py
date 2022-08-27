from typing import DefaultDict


def permutations(arr,temp,permutes,used:dict):
    # print(temp)
    if len(temp) == len(arr):
        permutes.append(temp[0:])
        return


    for i in range(0,len(arr)):
        if i not in used or used[i] == False:
            # print(used)
            temp.append(arr[i])
            used[i] = True
            permutations(arr,temp,permutes,used)
            temp.pop()
            used[i] = False

if __name__=="__main__":
    arr = [1,2,3]
    permutates = []
    used = dict()
    permutations(arr,[],permutates,used)

    for permuts in permutates:
        print(permuts)
    