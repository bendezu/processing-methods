import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
from src.line.Line import Line

PLOT_SIZE = 10

class Canvas:

    def add_plotable(self, plotable):
        self.plotables.append(plotable)

    def set_plotables(self, plotables):
        self.plotables = plotables

    def plot(self, show_desc=False, show_console=False):
        rows, cols = self.plotables.shape
        fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(PLOT_SIZE, PLOT_SIZE))
        for i in range(rows):
            for j in range(cols):
                plotable = self.plotables[i, j]
                subplot = axes[i][j]
                subplot.set_title(plotable.get_title())
                # if show_desc:
                #     subplot.set(xlabel=self.get_description(plotable))
                # if show_console:
                #     print("[" + plotable.title.upper() + "]")
                #     print(self.get_description(plotable))
                plotable.plot_on(subplot)
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
        c_slide = Slider(ax_c, 'C', -0.01, 0.01, valinit=ito.c, valstep=0.0005, valfmt="%1.4f")
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

    def plot_interactive_wiener(self):
        from src.line.wienerprocess import wiener
        offset = 2000
        length = 758
        first_val = 120

        def build_y(wiener, value):
            y = wiener.calculateY()[offset:]
            y = y - y[0] + value
            print(self.get_description(Line("", y=y)))
            return y

        wiener = wiener(s0=0, n=offset + length)
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.25)
        l, = plt.plot(np.arange(0, length, 1), build_y(wiener, first_val), lw=2)
        ax_c = plt.axes([0.1, 0.1, 0.8, 0.02])
        ax_s0 = plt.axes([0.1, 0.06, 0.8, 0.02])
        ax_gen = plt.axes([0.1, 0.02, 0.8, 0.02])
        c_slide = Slider(ax_c, 'C', 0, 50, valinit=wiener.c, valstep=0.05)
        s0_slide = Slider(ax_s0, 'S0', 50, 130, valinit=first_val, valstep=0.5)
        gen_btn = Button(ax_gen, 'Generate')

        def update(val):
            wiener.c = c_slide.val
            l.set_ydata(build_y(wiener, s0_slide.val))
            fig.canvas.draw_idle()

        c_slide.on_changed(update)
        s0_slide.on_changed(update)
        gen_btn.on_clicked(update)
        plt.show()
