# This program performs set operations on vegetarian and non-vegetarian dishes.

# Defining sets
vegetarian_dishes = {"Paneer Tikka", "Veg Biryani", "Dal Makhani", "Aloo Paratha"}
non_vegetarian_dishes = {"Chicken Biryani", "Mutton Curry", "Paneer Tikka", "Fish Fry"}

# Union - All available dishes
all_dishes = vegetarian_dishes.union(non_vegetarian_dishes)
print("All available dishes:", all_dishes)

# Intersection - Common dishes in both sets
common_dishes = vegetarian_dishes.intersection(non_vegetarian_dishes)
print("Common dishes in both categories:", common_dishes)

# Subset check
is_subset = vegetarian_dishes.issubset(non_vegetarian_dishes)
print("Is vegetarian_dishes a subset of non_vegetarian_dishes?", is_subset)
