import matplotlib.pyplot as plt

PLOT_SIZE = 10


class Canvas:
    drawables = []

    def add_drawable(self, drawable):
        self.drawables.append(drawable)

    def plot(self, show_desc=False):
        fig, axes = plt.subplots(nrows=round(len(self.drawables) / 2), ncols=2, figsize=(PLOT_SIZE, PLOT_SIZE))
        for i, drawable in enumerate(self.drawables):
            subplot = axes[int(i / 2)][i % 2]
            subplot.set_title(drawable.title)
            if show_desc:
                subplot.set(xlabel=self.get_description(drawable))
            subplot.plot(drawable.x, drawable.y)
        fig.tight_layout()
        plt.show()
        return fig

    def get_description(self, drawable):
        is_stationary = "Стационарен" if drawable.is_stationary(intervals=10, delta_percent=0.05) else "Не стационарен"
        stddev = "Стандартное отклонение " + str(drawable.getStdDev())
        return is_stationary + "\n" + stddev + "\n\n"
