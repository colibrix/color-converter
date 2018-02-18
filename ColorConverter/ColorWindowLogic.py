import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor

from ColorsWindow import Ui_ColorsConverterWindow
from Constants import *


class ColorLogic(QtWidgets.QMainWindow, Ui_ColorsConverterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.order = 0

        self.R = self.G = self.B = 0

        self.C = self.M = self.Y = self.K = 0

        self.H = self.S = self.L = 0

        self.color_frame.setStyleSheet(self.get_change_rectangle_color())

        self.rgb_r_slider.sliderMoved.connect(self.rgb_turn)
        self.rgb_r_slider.valueChanged.connect(self.set_rgb_red)

        self.rgb_b_slider.sliderMoved.connect(self.rgb_turn)
        self.rgb_b_slider.valueChanged.connect(self.set_rgb_blue)

        self.rgb_g_slider.sliderMoved.connect(self.rgb_turn)
        self.rgb_g_slider.valueChanged.connect(self.set_rgb_green)

        self.cmyk_c_slider.sliderMoved.connect(self.cmyk_turn)
        self.cmyk_c_slider.valueChanged.connect(self.set_cmyk_cyan)

        self.cmyk_m_slider.sliderMoved.connect(self.cmyk_turn)
        self.cmyk_m_slider.valueChanged.connect(self.set_cmyk_magenta)

        self.cmyk_y_slider.sliderMoved.connect(self.cmyk_turn)
        self.cmyk_y_slider.valueChanged.connect(self.set_cmyk_yellow)

        self.cmyk_k_slider.sliderMoved.connect(self.cmyk_turn)
        self.cmyk_k_slider.valueChanged.connect(self.set_cmyk_key)

        self.hsl_h_slider.sliderMoved.connect(self.hsl_turn)
        self.hsl_h_slider.valueChanged.connect(self.set_hsl_hue)

        self.hsl_s_slider.sliderMoved.connect(self.hsl_turn)
        self.hsl_s_slider.valueChanged.connect(self.set_hsl_sat)

        self.hsl_l_slider.sliderMoved.connect(self.hsl_turn)
        self.hsl_l_slider.valueChanged.connect(self.set_hsl_light)

        self.show()

    def change_cmyk_sliders(self):
        self.cmyk_c_slider.setValue(self.C * CMYK_SCALE)
        self.cmyk_m_slider.setValue(self.M * CMYK_SCALE)
        self.cmyk_y_slider.setValue(self.Y * CMYK_SCALE)
        self.cmyk_k_slider.setValue(self.K * CMYK_SCALE)

    def change_hsl_sliders(self):
        self.hsl_h_slider.setValue(self.H)
        self.hsl_s_slider.setValue(self.S * HSL_SCALE)
        self.hsl_l_slider.setValue(self.L * HSL_SCALE)

    def change_rgb_sliders(self):
        self.rgb_r_slider.setValue(self.R)
        self.rgb_g_slider.setValue(self.G)
        self.rgb_b_slider.setValue(self.B)

    def rgb_changes(self):
        self.rgb_to_cmyk()
        self.rgb_to_hsl()
        self.change_cmyk_sliders()
        self.change_hsl_sliders()

    def set_rgb_red(self):

        if self.order == 0:
            self.R = self.rgb_r_slider.value()
            self.rgb_changes()

        elif self.order == 1:
            self.change_hsl_sliders()

        elif self.order == 2:
            self.change_cmyk_sliders()
        self.rgb_red_line.setText(str(self.R))
        self.change_rectangle_color()

    def set_rgb_green(self):

        if self.order == 0:
            self.G = self.rgb_g_slider.value()
            self.rgb_changes()
        elif self.order == 1:
            self.change_hsl_sliders()
        elif self.order == 2:
            self.change_cmyk_sliders()
        self.rgb_green_line.setText(str(self.G))
        self.change_rectangle_color()

    def set_rgb_blue(self):

        if self.order == 0:
            self.B = self.rgb_b_slider.value()
            self.change_rectangle_color()
            self.rgb_changes()

        elif self.order == 1:
            self.change_hsl_sliders()

        elif self.order == 2:
            self.change_cmyk_sliders()
        self.rgb_blue_line.setText(str(self.B))
        self.change_rectangle_color()

    def set_cmyk_cyan(self):

        if self.order == 1:
            self.C = self.cmyk_c_slider.value() / CMYK_SCALE
            self.cmyk_to_rgb()
            self.rgb_to_hsl()
            self.change_rgb_sliders()
        self.cmyk_c_line.setText(str(self.C))

    def set_cmyk_magenta(self):

        if self.order == 1:
            self.M = self.cmyk_m_slider.value() / CMYK_SCALE
            self.cmyk_to_rgb()
            self.rgb_to_hsl()
            self.change_rgb_sliders()
        self.cmyk_m_line.setText(str(self.M))

    def set_cmyk_yellow(self):

        if self.order == 1:
            self.Y = self.cmyk_y_slider.value() / CMYK_SCALE
            self.cmyk_to_rgb()
            self.rgb_to_hsl()
            self.change_rgb_sliders()
        self.cmyk_y_line.setText(str(self.Y))

    def set_cmyk_key(self):

        if self.order == 1:
            self.K = self.cmyk_k_slider.value() / CMYK_SCALE
            self.cmyk_to_rgb()
            self.rgb_to_hsl()
            self.change_rgb_sliders()
        self.cmyk_k_line.setText(str(self.K))

    def set_hsl_hue(self):

        if self.order == 2:
            self.H = self.hsl_h_slider.value()
            self.hsl_to_rgb()
            self.rgb_to_cmyk()
            self.change_rgb_sliders()
        self.hsl_hue_line.setText(str(self.H))


    def set_hsl_sat(self):

        if self.order == 2:
            self.S = self.hsl_s_slider.value() / HSL_SCALE
            self.hsl_to_rgb()
            self.rgb_to_cmyk()
            self.change_rgb_sliders()
        self.hsl_sat_line.setText(str(self.S))

    def set_hsl_light(self):

        if self.order == 2:
            self.L = self.hsl_l_slider.value() / HSL_SCALE
            self.hsl_to_rgb()
            self.rgb_to_cmyk()
            self.change_rgb_sliders()
        self.hsl_light_line.setText(str(self.L))

    def rgb_turn(self):
        self.order = 0

    def cmyk_turn(self):
        self.order = 1

    def hsl_turn(self):
        self.order = 2

    ##########################################################
    ##########################################################
    def change_rectangle_color(self):
        req = self.get_change_rectangle_color()
        self.color_frame.setStyleSheet(req)

    def get_change_rectangle_color(self):
        request = background_rgb + str(self.R) + ", " + str(self.G) + ", " + str(self.B) + last_symbol
        return request

    ##########################################################

    def set_new_rgb_line(self):
        self.rgb_lineEdit.setText("(" + str(self.R) + ", " + str(self.G) + ", " + str(self.B) + ")")

    def set_new_cmyk_line(self):
        self.cmyk_lineEdit.setText(
            "(" + str(self.C) + ", " + str(self.M) + ", " + str(self.Y) + ", " + str(self.K) + ")")

    def set_new_hsl_line(self):
        self.hsl_lineEdit.setText("(" + str(self.H) + ", " + str(self.S) + ", " + str(self.L) + ")")

    ##########################################################

    # algorithms

    def rgb_to_cmyk(self):
        r = self.R / RGB_SCALE
        g = self.G / RGB_SCALE
        b = self.B / RGB_SCALE

        max1 = max(r, g, b)
        self.K = round(1 - max1, 2)
        if self.K == 1:
            self.C = 0
            self.M = 0
            self.Y = 0
        else:
            self.C = round((1 - r - self.K) / (1 - self.K), ACCURACY)
            if self.C < 0 or str(self.C)[0] == '-' or self.C < 1e-2:
                self.C = 0
            self.M = round((1 - g - self.K) / (1 - self.K), ACCURACY)
            if self.M < 0 or str(self.M)[0] == '-' or self.M < 1e-2:
                self.M = 0
            self.Y = round((1 - b - self.K) / (1 - self.K), ACCURACY)
            if self.Y < 0 or str(self.Y)[0] == '-' or self.Y < 1e-2:
                self.Y = 0

    def cmyk_to_rgb(self):
        self.R = math.ceil(RGB_SCALE - ((min(1, self.C * (1 - self.K) + self.K)) * RGB_SCALE))
        self.G = math.ceil(RGB_SCALE - ((min(1, self.M * (1 - self.K) + self.K)) * RGB_SCALE))
        self.B = math.ceil(RGB_SCALE - ((min(1, self.Y * (1 - self.K) + self.K)) * RGB_SCALE))

    def rgb_to_hsl(self):
        r, g, b = self.R, self.G, self.B

        r /= RGB_SCALE
        g /= RGB_SCALE
        b /= RGB_SCALE

        maximum = max(r, g, b)
        minimum = min(r, g, b)
        val = (maximum + minimum) / 2
        h, s, l = 0, 0, val

        if (maximum == minimum):
            h = s = 0
        else:
            d = maximum - minimum
            if l > 0.5:
                s = d / (2 - maximum - minimum)
            else:
                s = d / (maximum + minimum)
            if maximum == r:
                h = (g - b) / d
                if g < b:
                    h = h + 6

            elif maximum == g:
                h = (b - r) / d + 2
            elif maximum == b:
                h = (r - g) / d + 4

        h *= 60
        self.H = math.ceil(h)
        self.S = round(s, 2)
        self.L = round(l, 2)

    def hsl_to_rgb(self):
        c = (1.0 - math.fabs(2 * self.L - 1.0)) * self.S
        x = c * (1.0 - math.fabs(self.H / 60 % 2 - 1.0))
        m = self.L - c / 2.0
        r, g, b = self.to_rgb(c, x)
        self.R = math.ceil((r + m) * RGB_SCALE)
        self.G = math.ceil((g + m) * RGB_SCALE)
        self.B = math.ceil((b + m) * RGB_SCALE)

    def to_rgb(self, c, x):
        h = self.H
        r = g = b = 0
        if 0 <= h < DEG60:
            r = c
            g = x
            b = 0
        elif DEG60 <= h < 2 * DEG60:
            r = x
            g = c
            b = 0
        elif 2 * DEG60 <= h < 3 * DEG60:
            r = 0
            g = c
            b = x
        elif 3 * DEG60 <= h < 4 * DEG60:
            r = 0
            g = x
            b = c
        elif 4 * DEG60 <= h < 5 * DEG60:
            r = x
            g = 0
            b = c
        elif 5 * DEG60 <= h < 6 * DEG60:
            r = c
            g = 0
            b = x

        return r, g, b
