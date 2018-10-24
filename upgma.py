from pandas import DataFrame, IndexSlice
from seaborn import light_palette

# 1. Initialize Dataframe
'''
The data shown below illustrates differences
in amino acids for Cytochrome C between
different animals
'''
upgma = DataFrame({
    "Turtle": (0, 19, 27, 8, 33, 18, 13),
    "Man": (19, 0, 31, 18, 36, 1, 13),
    "Tuna": (27, 31, 0, 26, 41, 32, 29),
    "Chicken": (8, 18, 26, 0, 31, 17, 14),
    "Moth": (33, 36, 41, 31, 0, 35, 28),
    "Monkey": (18, 1, 32, 17, 35, 0, 12),
    "Dog": (13, 13, 29, 14, 28, 12, 0)
},
                  index=("Turtle", "Man", "Tuna", "Chicken", "Moth", "Monkey",
                         "Dog"))

# 2. Initialize Phylogeney dictionary
phylogeny = {}

# 3. Get the non-zero minimum
'''
Use a dict comphrension to get the minimal
distance between each animal.

This is done by taking the two smallest values
per index, summing them, and
returning the overall minimum value.
'''
most_related = {
    animal: upgma[animal].nsmallest(n=2).sum()
    for animal in upgma.index
}
selected_min = min(most_related.values())

# 4. Add gradient
'''
The darkest values will cluster last,
while the lightest values besides zero will
cluster first.
'''
upgma_style = upgma.style.background_gradient(
    cmap=light_palette("indigo", as_cmap=True))

# 5. Get the indices for the minimum occurence
'''
Retrive the minimum index
'''
min_index = upgma[upgma == selected_min]
min_index.dropna(how="all", inplace=True)
min_index = min_index.index
min_pair = str(min_index[0]) + "-" + str(min_index[1])

# 6. Create a function that highlights the mins
'''
After getting the minimum difference
between each animal, highlight the cells that
match the overall minimum result.
'''
upgma_style.applymap(
    lambda x: "background-color: orange",
    subset=IndexSlice[min_index, min_index])

# 8. Join Man & Monkey, clustering them with their # differences / 2
'''
This will be saved to build the tree
'''
phylogeny[tuple(min_index)] = selected_min / 2

# 9 . Highlights indices to merge
'''
All parallel elements will be added together and
divided by 2.
'''
upgma_style.applymap(
    lambda x: "background-color: yellow", subset=IndexSlice[min_index, :])
upgma_style.applymap(
    lambda x: "background-color: yellow", subset=IndexSlice[:, min_index])

# 10. Update the upgma indices
'''
Update the dataframe with the clustered index
names, then drop the unclustered index names
'''
merged_results = upgma.loc[min_index, :].sum() / 2
merged_results.drop(min_index, inplace=True)
upgma.rename(
    columns={min_index[0]: min_pair},
    index={min_index[0]: min_pair},
    inplace=True)
upgma.drop(min_index[1], axis=0, inplace=True)
upgma.drop(min_index[1], axis=1, inplace=True)

# 11. Update the upgma values
'''
Now substitute the merged values along the clustered
axes
'''
upgma.loc[upgma[min_pair] > 0, min_pair] = merged_results
upgma.loc[min_pair, upgma[min_pair] > 0] = merged_results
