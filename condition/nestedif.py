# Nested if statemet

a = ''
b = 2
c = "good"
d = 4
level_count = 0

# Nesting in action
if a == 1:
    level_count += 1
    if b == 2:
        level_count += 1
        if c == "good":
            level_count += 1
            print("We are {} level deep".format(level_count))
else:
    print("a needs to be one to see nested if statements in action")
    print("We are level %d" % (level_count))
