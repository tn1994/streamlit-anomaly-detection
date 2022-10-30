import changefinder
import numpy as np


class ChangeFinderService:
    """
    ref:
    https://qiita.com/deaikei/items/af728ab0d43ca97bc1f6
    https://qiita.com/anntoque/items/8f230744760dd4cee938
    https://qiita.com/DS27/items/af375c1b8fdf2610b8a4
    """

    @staticmethod
    def analysis(data: np.ndarray, r: float, order: int, smooth: int) -> list:
        if not isinstance(data, np.ndarray):
            raise TypeError
        cf = changefinder.ChangeFinder(r=r, order=order, smooth=smooth)

        ret = []
        for i in data:
            score = cf.update(i)
            ret.append(score)
        return ret


def generate_example_data() -> np.ndarray:
    return np.concatenate([
        np.random.normal(0.7, 0.05, 300),
        np.random.normal(1.5, 0.05, 300),
        np.random.normal(0.6, 0.05, 300),
        np.random.normal(1.3, 0.05, 300)])
