from numpy import where
from pandas import DataFrame, IndexSlice
from seaborn import light_palette


class UPGMA:
    def __init__(self, upgma):
        # 2. Initialize phylogeny and record dictionaries.
        '''
        The constructor requires a dataframe.
        In addition, two dictionaries are created:

        1. upgma_records: Highlighted tables.
        2. phylogeny: Tree distance between clusters.
        '''
        self.upgma = upgma
        self.upgma_records, self.phylogeny = {}, {}

    def calc_most_related(self):
        # 3. Get the minimum two pair sums for each animal.
        '''
        Use a dict comphrension to get the minimal
        distance between each animal.

        This is done by taking the two smallest values
        per index and summing them.
        '''
        self.most_related = {
            animal: self.upgma[animal].nsmallest(n=2).sum()
            for animal in self.upgma.index
        }

    def calc_selected_min(self):
        # 4. Get the lowest minimum from the most related pairs.
        '''
        Return the lowest minimum value from the most related dict.
        '''
        self.selected_min = min(self.most_related.values())

    def add_upgma_gradient(self):
        # 5. Add gradient
        '''
        The darkest values will cluster last,
        while the lightest values besides zero will
        cluster first.
        '''
        self.upgma_style = self.upgma.copy().style.background_gradient(
            cmap=light_palette("indigo", as_cmap=True))

    def get_min_indices(self):
        # 6. Get the indices for the selected min.
        '''
        Retrive indices where the selected min exists.
        Also create a tuple of this index for future use
        as dictonary keys and dataframe indices.
        '''
        self.min_index = self.upgma.iloc[where(
            self.upgma == self.selected_min)].index
        self.min_pair = tuple(self.min_index)

    def update_phylogeny(self):
        # 7. Save the minimum pair to the phylogeny dictionary.
        '''
        This dictionary will be used to build the tree.
        The horizontal distance between the animals is calculated
        by dividing the lowest min by 2.
        '''
        self.phylogeny[self.min_pair] = self.selected_min / 2

    def highlight_merging_cells(self):
        # 8. Highlights indices to merge.
        '''
        All parallel elements will be added together and
        divided by 2.
        '''
        self.upgma_style.applymap(
            lambda x: "background-color: yellow",
            subset=IndexSlice[self.min_index, :])
        self.upgma_style.applymap(
            lambda x: "background-color: yellow",
            subset=IndexSlice[:, self.min_index])

    def highlight_min_cells(self):
        # 9. Highlights the mins.
        '''
        After getting the minimum difference
        between each animal, highlight the cells that
        match the overall minimum result.
        '''
        self.upgma_style.applymap(
            lambda x: "background-color: red",
            subset=IndexSlice[self.min_index, self.min_index])

    def update_upgma_records(self):
        # 10. Add the stylized frame to the style dictionary.
        '''
        All steps of the tabular process are recorded
        '''
        self.upgma_records[self.min_pair] = self.upgma_style

    def calc_upgma_cluster(self):
        # 11. Calculate the values for the affected cells.
        '''
        Perform vectorized addition between cells that will
        be merged then divide by two.
        '''
        self.merged_results = self.upgma.loc[self.min_index, :].sum() / 2
        self.merged_results.drop(self.min_index, inplace=True)

    def restruct_upgma(self):
        # 12. Restructure the upgma dataframe.
        '''
        Update the dataframe with the clustered index
        names, then drop the unclustered index names.
        '''
        self.upgma.rename(
            columns={self.min_index[0]: self.min_pair},
            index={self.min_index[0]: self.min_pair},
            inplace=True)
        self.upgma.drop(self.min_index[1], axis=0, inplace=True)
        self.upgma.drop(self.min_index[1], axis=1, inplace=True)

    def upgma_merge_cluster(self):
        # 13. Update the upgma values.
        '''
        Now substitute the merged values along the clustered
        axes.
        '''
        self.upgma.loc[self.upgma[self.min_pair] > 0, self.
                       min_pair] = self.merged_results
        self.upgma.loc[self.min_pair, self.
                       upgma[self.min_pair] > 0] = self.merged_results

    def run_upgma(self):
        # 14. Run the algorithm.
        '''
        All steps will be saved to their respective dictionaries.

        Indices will be tupled and nested to construct the tree
        in the phylogeny dictionary,
        while the final highlighted tables for each iteration
        are stored in the upgma_records dictionary.
        '''
        while self.upgma.shape != (1, 1):
            self.calc_most_related()
            self.calc_selected_min()
            self.add_upgma_gradient()
            self.get_min_indices()
            self.update_phylogeny()
            self.highlight_merging_cells()
            self.highlight_min_cells()
            self.update_upgma_records()
            self.calc_upgma_cluster()
            self.restruct_upgma()
            self.upgma_merge_cluster()


# 1. Initialize Dataframe.
'''
The data shown below illustrates differences
in amino acids for Cytochrome C between
different animals.
'''
cytochrome_c = DataFrame({
    "Turtle": (0, 19, 27, 8, 33, 18, 13),
    "Man": (19, 0, 31, 18, 36, 1, 13),
    "Tuna": (27, 31, 0, 26, 41, 32, 29),
    "Chicken": (8, 18, 26, 0, 31, 17, 14),
    "Moth": (33, 36, 41, 31, 0, 35, 28),
    "Monkey": (18, 1, 32, 17, 35, 0, 12),
    "Dog": (13, 13, 29, 14, 28, 12, 0)
},
                         index=("Turtle", "Man", "Tuna", "Chicken", "Moth",
                                "Monkey", "Dog"))
upgma = UPGMA(cytochrome_c)
upgma.run_upgma()
