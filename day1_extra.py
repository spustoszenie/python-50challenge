def longest_value(fruits):
    longest = max(fruits.values(), key=len)
    print(longest)
    
fruits = {'fruit':'apple','color':'green'}
longest_value(fruits)