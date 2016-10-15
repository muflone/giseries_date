##
#     Project: giSeriesDate
# Description: Convert dates in iSeries format
#      Author: Fabio Castelli (Muflone) <muflone@vbsimple.net>
#   Copyright: 2016 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import os
import datetime

from gi.repository import Gtk
from gi.repository import Gdk

from giseries_date.constants import (
    APP_NAME, FILE_SETTINGS, FILE_WINDOWS_POSITION)
from giseries_date.functions import (
    get_ui_file, text, _)
import giseries_date.preferences as preferences
import giseries_date.settings as settings
from giseries_date.gtkbuilder_loader import GtkBuilderLoader

from giseries_date.ui.about import UIAbout

SECTION_WINDOW_NAME = 'main'


class UIMain(object):
    def __init__(self, application):
        self.application = application
        self.initial_ordinal = datetime.date(1899, 11, 29).toordinal()
        # Load settings
        settings.settings = settings.Settings(FILE_SETTINGS, False)
        settings.positions = settings.Settings(FILE_WINDOWS_POSITION, False)
        preferences.preferences = preferences.Preferences()
        self.loadUI()
        # Automatically select today
        today = datetime.date.today()
        self.ui.calendar_date.select_month(today.month - 1, today.year)
        self.ui.calendar_date.select_day(today.day)
        # Restore the saved size and position
        settings.positions.restore_window_position(
            self.ui.win_main, SECTION_WINDOW_NAME)

    def loadUI(self):
        """Load the interface UI"""
        self.ui = GtkBuilderLoader(get_ui_file('main.ui'))
        self.ui.win_main.set_application(self.application)
        self.ui.win_main.set_title(APP_NAME)
        # Initialize actions
        for widget in self.ui.get_objects_by_type(Gtk.Action):
            # Connect the actions accelerators
            widget.connect_accelerator()
            # Set labels
            widget.set_label(text(widget.get_label()))
        # Initialize tooltips
        for widget in self.ui.get_objects_by_type(Gtk.ToolButton):
            action = widget.get_related_action()
            if action:
                widget.set_tooltip_text(action.get_label().replace('_', ''))
        # Connect signals from the glade file to the module functions
        self.ui.connect_signals(self)

    def run(self):
        """Show the UI"""
        self.ui.win_main.show_all()

    def on_win_main_delete_event(self, widget, event):
        """Save the settings and close the application"""
        settings.positions.save_window_position(
            self.ui.win_main, SECTION_WINDOW_NAME)
        settings.positions.save()
        settings.settings.save()
        self.application.quit()

    def on_action_about_activate(self, action):
        """Show the about dialog"""
        dialog = UIAbout(self.ui.win_main)
        dialog.show()
        dialog.destroy()

    def on_action_quit_activate(self, action):
        """Close the application by closing the main window"""
        event = Gdk.Event()
        event.key.type = Gdk.EventType.DELETE
        self.ui.win_main.event(event)

    def on_calendar_date_day_selected(self, widget):
        """Convert date from normal to iseries"""
        selected_date = self.ui.calendar_date.get_date()
        ordinal_date = datetime.date(year=selected_date.year,
                                     month=selected_date.month + 1,
                                     day=selected_date.day).toordinal()
        self.ui.adjustment_date.set_value(ordinal_date - self.initial_ordinal)
        

    def on_spin_date_value_changed(self, widget):
        """Convert date from iseries to normal"""
        new_date = datetime.datetime.fromordinal(
            int(self.ui.spin_date.get_value()) + self.initial_ordinal)
        self.ui.calendar_date.select_month(new_date.month - 1, new_date.year)
        self.ui.calendar_date.select_day(new_date.day)
