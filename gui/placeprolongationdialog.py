#-----------------------------------------------------------
#
# Intersect It is a QGIS plugin to place observations (distance or orientation)
# with their corresponding precision, intersect them using a least-squares solution
# and save dimensions in a dedicated layer to produce maps.
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
#-----------------------------------------------------------
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
#---------------------------------------------------------------------

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from ..core.mysettings import MySettings

from ..ui.ui_place_prolongation import Ui_PlaceProlongation


class PlaceProlongationDialog(QDialog, Ui_PlaceProlongation):
    def __init__(self, prolongation, rubber):
        QDialog.__init__(self)
        self.setupUi(self)

        self.prolongation = prolongation
        self.rubber = rubber

        settings = MySettings()
        self.length.setValue(settings.value("obsProlongationLength"))
        self.precision.setValue(settings.value("obsDefaultPrecisionProlongation"))

    @pyqtSignature("on_length_valueChanged(double)")
    def on_length_valueChanged(self, v):
        self.prolongation.length = v
        self.rubber.setToGeometry(self.prolongation.geometry(), None)

    @pyqtSignature("on_precision_valueChanged(int)")
    def on_precision_valueChanged(self, v):
        self.prolongation.precision = v
        print self.prolongation.precision