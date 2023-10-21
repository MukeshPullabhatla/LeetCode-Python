from typing import List
def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    queue = []
    people.sort(key=lambda x: [-x[0], x[1]])
    for a in people:
        queue.insert(a[1],a)
    return queue

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))