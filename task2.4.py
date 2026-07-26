#For each scenario, name which structure you'd use (`list`, `tuple`, `dict`, or
#`set`) and why:

#- a) The RGB value of a single fixed color.
#- b) A phone book (name → number).
#- c) The list of tags on a blog post, where duplicates make no sense.
#- d) A to-do list you'll reorder and add to all day.

# a uses a `tuple` because the RGB value is a fixed set of three values that should not change
# b uses a `dict` because it allows for key-value pairs where the name is the key and the number is the value
# c uses a `set` because it automatically removes duplicates and is unordered which is suitable for tags
# d uses a `list` because it allows for dynamic reordering and modification of items