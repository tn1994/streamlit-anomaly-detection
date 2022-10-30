import rrcf
import numpy as np


class RandomCutForestService:
    """
    # random cut forest
    ref: https://qiita.com/DS27/items/af375c1b8fdf2610b8a4
    ref: https://klabum.github.io/rrcf/
    """

    data = np.concatenate([np.random.normal(0.7, 0.05, 300),
                           np.random.normal(1.5, 0.05, 300),
                           np.random.normal(0.6, 0.05, 300),
                           np.random.normal(1.3, 0.05, 300)])

    def set_data(self, data: np.ndarray):
        self.data = data.copy()

    def main(self) -> dict:
        # Set tree parameters
        num_trees = 40
        shingle_size = 4
        tree_size = 256

        # Create a forest of empty trees
        forest = []
        for _ in range(num_trees):
            tree = rrcf.RCTree()
            forest.append(tree)

        # Use the "shingle" generator to create rolling window
        # points = rrcf.shingle(sin, size=shingle_size)
        points = rrcf.shingle(self.data.copy(), size=shingle_size)

        # Create a dict to store anomaly score of each point
        avg_codisp = {}

        # For each shingle...
        for index, point in enumerate(points):
            # For each tree in the forest...
            for tree in forest:
                # If tree is above permitted size...
                if len(tree.leaves) > tree_size:
                    # Drop the oldest point (FIFO)
                    tree.forget_point(index - tree_size)
                # Insert the new point into the tree
                tree.insert_point(point, index=index)
                # Compute codisp on the new point...
                new_codisp = tree.codisp(index)
                # And take the average over all trees
                if index not in avg_codisp:
                    avg_codisp[index] = 0
                avg_codisp[index] += new_codisp / num_trees

        return avg_codisp
