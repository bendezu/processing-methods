import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

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
            else:
                print("[" + drawable.title.upper() + "]")
                print(self.get_description(drawable))
            subplot.plot(drawable.x, drawable.y)
        fig.tight_layout()
        plt.show()
        return fig

    def get_description(self, drawable):
        is_stationary = "Стационарен" if drawable.is_stationary(intervals=10, delta_percent=0.05) else "Не стационарен"
        mean = str(drawable.getMean()) + " - Среднее значение"
        dispersion = str(drawable.getDispersion()) + " - Дисперсия"
        mean_square = str(drawable.meanSquare()) + " - Средний квадрат"
        stddev = str(drawable.getStdDev()) + " - Стандартное отклонение"
        mean_square_dev = str(drawable.meanSquareDev()) + " - Среднеквадратичное отклонение"
        midpoint_3 = str(drawable.m(power=3)) + " - Центральный момент 3го порядка"
        asymmetry_coeff = str(drawable.gamma1()) + " - Коэффициент асимметрии"
        midpoint_4 = str(drawable.m(power=4)) + " - Центральный момент 4го порядка"
        сultosis = str(drawable.gamma2()) + " - Культозис"
        minimum = str(drawable.minimum()) + " - Минимальное значение"
        maximum = str(drawable.maximum()) + " - Максимальное значение"
        stat = [is_stationary, mean, dispersion, mean_square, stddev, mean_square_dev, midpoint_3, asymmetry_coeff, midpoint_4, сultosis, minimum, maximum]
        return "\n".join(stat) + "\n\n"

    def plot_interactive_ito(self, ito):
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.25)
        l, = plt.plot(ito.x, ito.y, lw=2)
        ax.margins(x=0)
        ax_a = plt.axes([0.1, 0.14, 0.8, 0.02])
        ax_b = plt.axes([0.1, 0.1, 0.8, 0.02])
        ax_c = plt.axes([0.1, 0.06, 0.8, 0.02])
        ax_d = plt.axes([0.1, 0.02, 0.8, 0.02])
        a_slider = Slider(ax_a, 'A', -500, 500, valinit=ito.a, valstep=5)
        b_slide = Slider(ax_b, 'B', -0.01, 0.01, valinit=ito.b, valstep=0.00005, valfmt="%1.5f")
        c_slide = Slider(ax_c, 'C', -5, 5, valinit=ito.c, valstep=0.05)
        d_slide = Slider(ax_d, 'D', 1, 200, valinit=ito.d, valstep=1)

        def update(val):
            ito.a = a_slider.val
            ito.b = b_slide.val
            ito.c = c_slide.val
            ito.d = d_slide.val
            l.set_ydata(ito.calculateY())
            fig.canvas.draw_idle()

        a_slider.on_changed(update)
        b_slide.on_changed(update)
        c_slide.on_changed(update)
        d_slide.on_changed(update)
        plt.show()
