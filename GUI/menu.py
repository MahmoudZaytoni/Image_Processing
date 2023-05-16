import customtkinter as ctk
from panels import *

class Menu(ctk.CTkTabview):
    def __init__(self, parent, tab1_vars, tab2_vars, tab3_vars, process_func, export_image):
        super().__init__(master = parent)
        self.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        #tabs 
        self.add('Tab1')
        self.add('Tab2')
        self.add('Tab3')
        self.add('Export')
        
        # widgets
        Tab1Frame(self.tab('Tab1'), tab1_vars, process_func)
        Tab2Frame(self.tab('Tab2'), tab2_vars, process_func)
        Tab3Frame(self.tab('Tab3'), tab3_vars, process_func)
        ExportFrame(self.tab('Export'), export_image)

class Tab1Frame(ctk.CTkFrame):
    def __init__(self, parent, tab_vars, process_func):
        super().__init__(master = parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')
        
        SliderPanel(self, 'Position', tab_vars['rotate'], 0, 360, lambda:process_func('here'))
        SegmentPanel(self, 'Some Option' , tab_vars['flip'], FLIP_OPTIONS)
        RevertButton(self,
                (tab_vars['rotate'], ROTATE_DEFAULT),
                (tab_vars['flip'], FLIP_OPTIONS[0]))

class Tab2Frame(ctk.CTkFrame):
    def __init__(self, parent, tab_vars, process_func):
        super().__init__(master = parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        SwitchPanel(self, (tab_vars['grayscale'], 'B/W'), (tab_vars['invert'], 'invert'), (tab_vars['histogram_equalization'], 'hist'))
        SliderPanel(self, 'Brightness Offset', tab_vars['brightness'], 0, 100, lambda:process_func('Brightness'))
        SliderPanel(self, 'Power Low gamma', tab_vars['gamma'], 1, 5, lambda:process_func('power_trans'))

class Tab3Frame(ctk.CTkFrame):
    def __init__(self, parent, tab_vars, process_func):
        super().__init__(master = parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')
        
        DropDownPanel(self, tab_vars['effect'], EFFECT_OPTIONS)
        SliderPanel(self, 'Blur', tab_vars['blur'], 1, 5, process_func)
        SliderPanel(self, 'Contrast', tab_vars['contrast'], 1, 10, process_func)

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent, export_image):
        super().__init__(master = parent, fg_color = 'transparent')
        self.pack(expand = True, fill = 'both')

        self.name_string = ctk.StringVar()
        self.format_string = ctk.StringVar(value = 'jpg')
        self.path_string = ctk.StringVar()

        FileNamePanel(self, self.name_string, self.format_string)
        FilePathPanel(self, self.path_string)
        SaveButton(self, export_image, self.name_string, self.format_string, self.path_string)
