import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.ensemble import IsolationForest


class IsolationForestService:
    """
    isolation forest
    ref: https://qiita.com/tchih11/items/d76a106e742eb8d92fb4
    """

    SEED: int = 42

    def main(self):
        sns.set()
        np.random.seed(self.SEED)

        # 平均と分散
        mean1 = np.array([2, 2])
        mean2 = np.array([-2, -2])
        cov = np.array([[1, 0], [0, 1]])

        # 正常データの生成(2つの正規分布から生成)
        norm1 = np.random.multivariate_normal(mean1, cov, size=100)
        norm2 = np.random.multivariate_normal(mean2, cov, size=100)

        # 異常データの生成(一様分布から生成)
        lower, upper = -10, 10
        anom = (upper - lower) * np.random.rand(10, 2) + lower

        df = np.vstack([norm1, norm2, anom])
        df = pd.DataFrame(df, columns=["feat1", "feat2"])

        # 可視化
        # sns.scatterplot(x="feat1", y="feat2", data=df)

        sk_df = df.copy()

        clf = IsolationForest(n_estimators=100, random_state=self.SEED)
        clf.fit(sk_df)
        sk_df["predict"] = clf.predict(sk_df)

        # 可視化
        # return sns.scatterplot(x="feat1", y="feat2", data=sk_df,
        # hue='predict', palette='bright')
        return sk_df
