import tkinter as tk
from tkinter import *
import surf
import tksheet

# create tk
root = tk.Tk()
root.title("Equivalent fire severity calculator")

frames = []
for i in range(5):
    for j in range(5):
        Frame = tk.Frame(root, borderwidth=1)
        Frame.grid(row=i, column=j)

        frames.append(Frame)


def check_entries(*args):
    if FLD_entry.get() and H_entry.get() and corr_entry.get() and conv_entry.get() and fa_entry.get():
        print(1)


#     calc_button.configure(state=ACTIVE)
# else:
#     calc_button.configure(state=DISABLED)


def calculate():
    nums = []
    areas = []
    fld = float(FLD_entry.get())
    conv_f = float(conv_entry.get())
    corr_f = float(corr_entry.get())
    fa = float(fa_entry.get())
    H = float(H_entry.get())
    a_h = 0

    for col in range(11):
        for row in range(3):
            num = input_sheet.MT.data[row][col]
            if isinstance(num, float):
                nums.append(num)
            elif num.isdigit():
                nums.append(float(num))
    for i in range(0, len(nums), 2):
        area = nums[i]*nums[i+1]
        areas.append(area)
    print(areas)
    area_sum = sum(areas)
    print(area_sum)

    a_v = area_sum / fa
    b_v = 12.5 * (1 + (10 * a_v) - (a_v**2))
    w_f = ((6/H)**0.3)*(0.62+(90*(0.4-a_v)**4)/(1+a_h*b_v))
    t_e = fld * corr_f * conv_f * w_f
    print(f"av:{a_v}, b_v:{b_v}, w_f:{w_f}, te:{t_e}")

    # update output sheet
    output_sheet.set_sheet_data(input_sheet.get_sheet_data(return_copy=1))
    output_sheet.set_all_column_widths(75)
    output_sheet.column_width(0, 30)
    output_sheet.highlight_columns(0, bg='SystemButtonFace')
    output_sheet.highlight_rows(0, bg='SystemButtonFace')
    output_sheet.align_columns(0, align='center')
    output_sheet.insert_row(["a_v:", a_v, "a_h:", a_h, "b_v:", b_v, "w_f:", w_f, "t_e:", t_e])
    output_sheet.highlight_cells(3, 0, bg='SystemButtonFace')
    output_sheet.highlight_cells(3, 2, bg='SystemButtonFace',)
    output_sheet.highlight_cells(3, 4, bg='SystemButtonFace')
    output_sheet.highlight_cells(3, 6, bg='SystemButtonFace')
    output_sheet.highlight_cells(3, 8, bg='SystemButtonFace')
    output_sheet.insert_row()
    output_sheet.highlight_rows(4, bg="black")
    output_sheet.pack()



def presets(event):
    FLD_entry.config(state="normal")
    FLD_entry.delete(0, END)

    conv_entry.config(state="normal")
    conv_entry.delete(0, END)

    corr_entry.config(state="normal")
    corr_entry.delete(0, END)

    fa_entry.config(state="normal")
    fa_entry.delete(0, END)

    H_entry.config(state="normal")
    H_entry.delete(0, END)

    if dropdown.get() == "Test 1":
        FLD_text.set(630)
        # FLD_entry.config(state="disabled")

        conv_text.set(0.07)
        # conv_entry.config(state="disabled")

        corr_text.set(1)
        # corr_entry.config(state="disabled")

        fa_text.set(59.1)
        # fa_entry.config(state="disabled")

        H_text.set(3.17)
        # H_entry.config(state="disabled")

        input_sheet.set_column_data(1, ("Window 1", 2.4, 2.4))
        input_sheet.set_column_data(2, ("Window 2", 2.2, 2.4))
        input_sheet.set_column_data(3, ("Window 3", 1.4, 2.4))
        input_sheet.set_column_data(4, ("Window 4", 1.15, 2.4), redraw=True)


# create title
frames[0].configure(relief=tk.RAISED, borderwidth=5)
frames[0].grid(row=0, column=0, columnspan=2, sticky=EW)
title_label = tk.Label(master=frames[0], text="Equivalent fire severity\ncalculator", font="non 16 bold")
title_label.pack(fill=tk.BOTH, expand=1)

# create preset list
OPTIONS = ["Custom", "Test 1"]
dropdown = StringVar(root)
dropdown.set("Presets")
dd = OptionMenu(frames[0], dropdown, *OPTIONS, command=presets)
dd.configure(relief=tk.RAISED, borderwidth=3)
dd.pack()

# create surface button
surf_button = tk.Button(frames[20], text="Show surface plot")
surf_button.pack(fill=tk.BOTH, expand=1)
surf_button.configure(command=surf.surface)

# create inputs
frames[5].configure(relief=tk.RAISED, borderwidth=5)
frames[5].grid(row=1, column=0, sticky=EW)

FLD_label = tk.Label(frames[5], text="Enter design fire load density: ")
FLD_label.pack()

conv_label = tk.Label(frames[5], text="Enter conversion factor: ")
conv_label.pack()

corr_label = tk.Label(frames[5], text="Enter correction factor: ")
corr_label.pack()

fa_label = tk.Label(frames[5], text="Enter floor area: ")
fa_label.pack()

H_label = tk.Label(frames[5], text="Enter height: ")
H_label.pack()

# create entry boxes
FLD_text = tk.StringVar(root)
FLD_entry = tk.Entry(frames[6], textvariable=FLD_text)
FLD_entry.pack(pady=1)
FLD_text.trace_variable("w", check_entries)

conv_text = tk.StringVar(root)
conv_entry = tk.Entry(frames[6], textvariable=conv_text)
conv_entry.pack(pady=1)
conv_text.trace_variable("w", check_entries)

corr_text = tk.StringVar(root)
corr_entry = tk.Entry(frames[6], textvariable=corr_text)
corr_entry.pack(pady=1)
corr_text.trace_variable("w", check_entries)

fa_text = tk.StringVar(root)
fa_entry = tk.Entry(frames[6], textvariable=fa_text)
fa_entry.pack(pady=1)
corr_text.trace_variable("w", check_entries)

H_text = tk.StringVar(root)
H_entry = tk.Entry(frames[6], textvariable=H_text)
H_entry.pack(pady=1)
H_text.trace_variable("w", check_entries)

# create input sheet
frames[10].grid(columnspan=2)
input_sheet = tksheet.Sheet(frames[10], width=450, height=110, show_y_scrollbar=False)
input_sheet.pack()
input_sheet.set_options(total_columns=11, total_rows=3)
input_sheet.insert_row([" ", "Window 1", "Window 2", "Window 3", "Window 4", "Window 5",
                     "Window 6", "Window 7", "Window 8", "Window 9", "Window 10"])
#input_sheet.headers([" ", "Window 1", "Window 2", "Window 3", "Window 4", "Window 5",
                    # "Window 6", "Window 7", "Window 8", "Window 9", "Window 10"])
input_sheet.set_all_column_widths(75)
input_sheet.enable_bindings(("single_select",

                             "drag_select",

                             "row_select",

                             "column_width_resize",

                             "arrowkeys",

                             "right_click_popup_menu",

                             "rc_select",

                             # "rc_insert_row",

                             # "rc_delete_row",

                             "copy",

                             # "cut",

                             # "paste",

                             # "delete",

                             # "undo",

                             "edit_cell"
                             ))
input_sheet.set_column_data(0, (" ","H", "W"))
input_sheet.column_width(0, 30)
input_sheet.highlight_columns(0, bg='SystemButtonFace')
input_sheet.highlight_rows(0, bg='SystemButtonFace')
input_sheet.align_columns(0, align='center')

# create calculate button
calc_button = tk.Button(frames[20], text="Calculate")
calc_button.pack(fill=tk.BOTH, expand=1)
calc_button.configure(command=calculate)

# create output sheet
frames[7].grid(padx=5, columnspan=4)
output_sheet = tksheet.Sheet(frames[2], width=700)
output_sheet.set_options(total_columns=11)
#output_sheet.headers([" ", "Window 1", "Window 2", "Window 3", "Window 4", "Window 5",
                    # "Window 6", "Window 7", "Window 8", "Window 9", "Window 10"])



root.mainloop()
