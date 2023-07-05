# Expected result indexes [0, 2, 5, 9]
# Target value 109681

from copy import deepcopy

# Global variable that store the values 
values: list[float] = [ 27880, 10527, 62875, 5571, 6970, 1798, 52104, 7928, 6151, 17128, 22593, 2926, 19324 ]

# Sum pairs to find possible values
def add_in_groups(group_list: list[list], target: float) -> list[int]:
    result: list[int] = []
    new_group: list[list] = []

    if len(group_list) < 1:
        return []
    
    for group in group_list:
        group_value: int = 0 
        for x in group:
            group_value += values[x]
        
        for j, num in enumerate(values):
            if j not in group:
                sum = group_value + num
                # Add the current index on group and return the awnser
                if sum == target:
                    group.append(j)
                    return group
                # Target not reached yet check again
                elif  sum < target:
                    group_copy = deepcopy(group)
                    group_copy.append(j)
                    new_group.append(group_copy)
                    print(new_group)
                else:
                    continue
                    
    # Each recursion add a possible new value to each group trying to find a given target
    result = add_in_groups(new_group, target)
    
    return result

# Iterate trougth array to find a possible addends combinations for target sum
def find_addends(target: float) -> list[int]:
    result: list[int] = []
    group_list: list[list] = []

    for i, value_x in enumerate(values):
        # Compare once just distinct values for 1 time each
        for j, value_y in enumerate(values):
            
            # One value satisfyes the target
            if value_y == target:
                return [i]
            # To avoid repeating indexes
            if j <= i:
                continue
            
            sum = value_x + value_y
            if sum == target:
                return [i, j]
            elif sum < target:
                group_list.append([i, j])
            else:
                continue
                
    result = add_in_groups(group_list, target)
    
    return result

# ↓ Execution ↓
target_sum = 109681

result = find_addends(target_sum)

if result:
    print(f"\nThe indexes { result } of values added results on the target sum {target_sum}.\n")
else:
    print("\nWasn't found any addednds combinations for the target sum\n.")
