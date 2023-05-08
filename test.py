import tkinter as tk

# Create the Tkinter window
root = tk.Tk()

# Create a list to store the frames
frames = []

# Create a 3x3 grid of frames
for i in range(3):
    row = []
    for j in range(3):
        # Create a new frame
        frame = tk.Frame(root, width=100, height=100, borderwidth=1, relief="solid")
        frame.grid(row=i, column=j, sticky="nsew")

        # Set row and column weights for the frame
        for k in range(3):
            frame.grid_rowconfigure(k, weight=1)
            frame.grid_columnconfigure(k, weight=1)

            # Create a 3x3 grid of subframes in the frame
            subframes = []
            for l in range(3):
                subrow = []
                for m in range(3):
                    # Create a new subframe
                    subframe = tk.Frame(frame, width=30, height=30, borderwidth=1, relief="solid")
                    subframe.grid(row=l, column=m, sticky="nsew")
                    subrow.append(subframe)

                    # Set row and column weights for the subframe
                    subframe.grid_rowconfigure(0, weight=1)
                    subframe.grid_columnconfigure(0, weight=1)
                subframes.append(subrow)

            # Store the subframes in the frame
            frame.subframes = subframes

        row.append(frame)

    frames.append(row)

# Set row and column weights for the root window
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
