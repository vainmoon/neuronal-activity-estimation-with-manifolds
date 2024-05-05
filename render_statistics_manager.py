import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class RenderStatisticsManager:
    def __init__(self):
        pass

    def render_neural_activity_map(self, data):
        plt.imshow(data)

    def render_neural_manifold(self, data):
        plt.suptitle('projections of the manifold')
        plt.figure(figsize=(15.0, 7.0))
        plt.subplots_adjust(left=0.13,
                            right=0.93,
                            top=1.0,
                            bottom=0.27,
                            wspace=0.6,
                            hspace=0.3)
        label_fontsize = 12
        scatter_params = {"marker": "o", "s": 20}

        plt.subplot(1, 3, 1)
        plt.scatter(data[:, 0], data[:, 1], **scatter_params)
        plt.xlabel("C1", fontsize=label_fontsize)
        plt.ylabel("C2", fontsize=label_fontsize)

        plt.subplot(1, 3, 2)
        plt.scatter(data[:, 0], data[:, 2], **scatter_params)
        plt.xlabel("C1", fontsize=label_fontsize)
        plt.ylabel("C3", fontsize=label_fontsize)

        plt.subplot(1, 3, 3)
        plt.scatter(data[:, 1], data[:, 2], **scatter_params)
        plt.xlabel("C2", fontsize=label_fontsize)
        plt.ylabel("C3", fontsize=label_fontsize)

        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], marker='o', s=10)
        ax.set_xlabel("C1", fontsize=label_fontsize)
        ax.set_ylabel("C2", fontsize=label_fontsize)
        ax.set_zlabel("C3", fontsize=label_fontsize)

