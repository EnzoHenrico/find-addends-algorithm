# find-addends-algorithm

This is an algorithm that i made to find a sum in the list of values, these values ​​being the possible addends.

> It was a challenging and fun challenge to make these algorithm, the need for this algorithm arose from a specific problem at the company where I am and this solution is helping a lot on a daily basis!

### Logic:
- The code has a static global variable called "values" that represent a list of float numbers
- The variable "target_sum" is the sum the code are trying to find.
### find_addends(target: float) -> list
- First "find_addends" are called receving the "target" by parametter.
- Loop over the values tryng find pairs of addends to the given target sum.
- - If the algorithm find a sum that matches target he will return the index of each addend in a list.
- If made all pairs groups and not found any possible addends, may these groups need more members to reach the sum, so is called "add_in_groups".
### add_in_groups (group_list: list, target: float) -> list
- Receives "group_list" and "target", the group list are an array of indexes that reprents the possibles combinations of addends to reach target.
- Add a new index to each group, never repeating values.
- If the algorithm find a sum that matches target he will return the index of each addend in a list.
- If not found after all iterations, recursevelly calls itself passing the new list of groups, now with one more value on each group.
- Returns the result when found or an empity list if don't.

## Improve points
- Memory efficience