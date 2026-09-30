import tkinter as tk


class RollingPlotter:
    """ Manages the plotting window. """

    def __init__(self, raw: list[float], smooth: list[float], 
                 left: int, top: int, width: int, height: int) -> None:
        """ Initializes the root Tkinter window and creates a drawing canvas. """
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.raw_data = raw
        self.smoothed_data = smooth
        self.draw_raw = True
        self.draw_smooth = False
        self.root = tk.Tk()
        self.root.title("Rolling Average")
        frame = tk.Frame(self.root)
        frame.pack()    # Make frame fill entire window
        self.root.geometry(f'{width + 10}x{height + 10}+5+5')
        self.canvas = tk.Canvas(frame, width=width, height=height)
        self.canvas.bind_all('<Key>', self.key_pressed)
        self.canvas.pack() 
        self.plot()
        self.root.mainloop()


    def plot(self) -> None:
        """ Plots the curves. """
        self.root.focus_set()
        # Compute the vertical size of the data
        min_val = min(self.raw_data) - 5
        max_val = max(self.raw_data) + 5
        width_scale = self.width/(len(self.raw_data) - 1)
        height_scale = self.height/(max_val - min_val)

        # Draw baseline at y = 0
        y_zero = self.height + min_val*height_scale
        self.canvas.create_line(0, y_zero, self.width, y_zero, fill='cyan')
    
        if self.raw_data and self.draw_raw:
            # Plot raw data
            print(f'Raw length: {len(self.raw_data)}')
            for i in range(1, len(self.raw_data)):
                x0 = (i - 1) * width_scale
                y0 = self.height - (self.raw_data[i - 1] - min_val)*height_scale
                x1 = i * width_scale
                y1 = self.height - (self.raw_data[i] - min_val)*height_scale
                self.canvas.create_line(x0, y0, x1, y1, fill='blue')

        smooth_offset = (len(self.raw_data) - len(self.smoothed_data))/2
        if self.smoothed_data and self.draw_smooth:
            # Plot smoothed data
            # Compute the vertical size of the data
            #min_val = min(self.smoothed_data) - 5
            #max_val = max(self.smoothed_data) + 5
            print(f'Smoothed length: {len(self.smoothed_data)}')
            #width_scale = self.width/(len(self.smoothed_data) - 1)
            #height_scale = self.height/(max_val - min_val)
            for i in range(1, len(self.smoothed_data)):
                x0 = (smooth_offset + (i - 1)) * width_scale 
                y0 = self.height - (self.smoothed_data[i - 1] - min_val)*height_scale
                x1 = (smooth_offset + i) * width_scale #+ length_adjustment
                y1 = self.height - (self.smoothed_data[i] - min_val)*height_scale
                self.canvas.create_line(x0, y0, x1, y1, fill='red')
            self.root.mainloop()


    def replot(self) -> None:
        """ Rerenders the canvas to plot the curves. """
        self.canvas.delete(tk.ALL)
        self.plot()


    def key_pressed(self, event: tk.Event) -> None:
        """ Responds to the user's keypress:
            R -- Draws the raw curve
            S -- Draws the smoothed curve 
            B -- Toggles drawing both curves """
        match event.keysym:
            case 'R' | 'r':
                self.draw_raw = True
                self.draw_smooth = False
            case 'S' | 's':
                self.draw_raw = False
                self.draw_smooth = True
            case 'B' | 'b':
                if self.draw_raw and not self.draw_smooth:
                    self.draw_smooth = True   # Activate the smooth curve
                elif not self.draw_raw and self.draw_smooth:
                    self.draw_raw = True      # Activate the raw curve
                else:
                    self.draw_raw = True      # Only the raw curve is active
                    self.draw_smooth = False
        self.replot()


if __name__ == '__main__':
    plotter = RollingPlotter([10, -10, 5, -5], [15, -15, 3, -3], 100, 100, 300, 150)
    plotter.plot()
