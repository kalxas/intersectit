# -----------------------------------------------------------
#
# Intersect It is a QGIS plugin to place observations (distance or orientation)
# with their corresponding precision, intersect them using a least-squares solution
# and save dimensions in a dedicated layer to produce maps.
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
# -----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# ---------------------------------------------------------------------

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from qgis.gui import QgsRubberBand

from ..core.mysettings import MySettings
from ..ui.ui_place_distance import Ui_place_distance


class DistanceDialog(QDialog, Ui_place_distance):
    def __init__(self, distance, canvas):
        QDialog.__init__(self)
        self.setupUi(self)
        self.settings = MySettings()

        # this is a reference, distance observation is modified in outer class
        self.distance = distance

        self.rubber = QgsRubberBand(canvas)
        self.rubber.setColor(self.settings.value("rubberColor"))
        self.rubber.setIconSize(self.settings.value("rubberSize"))

        self.x.setText("%.3f" % distance.point.x())
        self.y.setText("%.3f" % distance.point.y())
        self.observation.setValue(distance.observation)
        self.precision.setValue(distance.precision)
        self.observation.selectAll()

    @pyqtSignature("on_observation_valueChanged(double)")
    def on_observation_valueChanged(self, v):
        self.distance.observation = v
        self.rubber.setToGeometry(self.distance.geometry(), None)

    @pyqtSignature("on_precision_valueChanged(double)")
    def on_precision_valueChanged(self, v):
        self.distance.precision = v

    def accept(self):
        self.rubber.reset()
        QDialog.accept(self)

    def reject(self):
        self.rubber.reset()
        QDialog.reject(self)

    def closeEvent(self, e):
        self.rubber.reset()


