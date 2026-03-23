import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import serial
import json
import os 
from PIL import Image, ImageTk

# setting up uart config 
try:
    uart_conf = serial.Serial("/dev/serial0", 9600, timeout=1)
except:
    print("port error or smth")

class speedometer(ttk.Frame):

    def __init__(self, master, max_speed=51, size=1000):
        super().__init__(master)

        self.max_speed = max_speed
        self.size = size

        self.canvas = tk.Canvas(self, width=size, height=size, bg="black", highlightthickness=0)
        self.canvas.pack()

        padding = 250

        self.brake_overlay = self.canvas.create_rectangle(
            0, 0, size, size,
            fill="red",
            state="hidden"
        )

        self.power_bar = self.canvas.create_rectangle(
            0, 0,
            size, size,  # starts with 0 width
            fill="#00f2ff", outline=""
        )


        # speedometer back
        self.speedometer_back = self.canvas.create_oval(
            padding, padding,
            size-padding, size-padding,
            outline="#763c0c",
            width=20
        )

        # speedometer front
        self.speedometer_front = self.canvas.create_arc(
            padding, padding,
            size-padding, size-padding,
            start=90,
            extent=0,
            style="arc",
            outline="#fd7e14",
            width=20
        )

        # current
        self.current_text = self.canvas.create_text(
            15, size - 40,
            text="Current: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="nw"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "car-battery.png")
        self.current_icon = Image.open(icon_path)
        self.current_icon_tk = ImageTk.PhotoImage(self.current_icon)
        self.current_img = self.canvas.create_image(10, size - 130, image=self.current_icon_tk, anchor="nw")

        # motor mode
        self.mode_text = self.canvas.create_text(
            size - 15, size - 40,
            text="Mode: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="ne"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "fast-forward.png")
        self.mmode_icon = Image.open(icon_path)
        self.mmode_icon_tk = ImageTk.PhotoImage(self.mmode_icon)
        self.mmode_img = self.canvas.create_image(size - 110, size - 130, image=self.mmode_icon_tk, anchor="nw")

        # speed
        self.speed_text = self.canvas.create_text(
            size/2, size/2,
            text="",
            fill="#56cc9d",
            font=("Space Grotesk", 32, "bold")
        )

        # temps
        self.temp_text = self.canvas.create_text(
            size/2, 130,
            text="Temp: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="center"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "thermometer-simple.png")
        self.temp_icon = Image.open(icon_path)
        self.temp_icon_tk = ImageTk.PhotoImage(self.temp_icon)
        self.temp_img = self.canvas.create_image(size/2, 10, image=self.temp_icon_tk, anchor="n")

        # battery
        self.battery_text = self.canvas.create_text(
            size - 15, 120,
            text="Battery: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="ne"
        ) ## loading image
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "battery-charging-vertical.png")
        self.battery_icon = Image.open(icon_path)
        self.battery_icon_tk = ImageTk.PhotoImage(self.battery_icon)
        self.battery_img = self.canvas.create_image(size - 90, 10, image=self.battery_icon_tk, anchor="nw")

        # power percent
        self.power_percent = self.canvas.create_text(
            size/2, size - 25,
            text="Power: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="center"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "lightning.png")
        self.lightning_icon = Image.open(icon_path)
        self.lightning_icon_tk = ImageTk.PhotoImage(self.lightning_icon)
        self.power_img = self.canvas.create_image(size/2, size - 96, image=self.lightning_icon_tk, anchor="center")

        # lights
        self.lights = self.canvas.create_text(
            15, 120,
            text="Lights: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="nw"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "lightbulb.png")
        self.lighting_icon = Image.open(icon_path)
        self.lighting_icon_tk = ImageTk.PhotoImage(self.lighting_icon)
        self.light_img = self.canvas.create_image(0, 10, image=self.lighting_icon_tk, anchor="nw")

        # err_code
        self.err_code = self.canvas.create_text(
            20, 105,
            text="Error code: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="nw"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "warning.png")
        self.err_code_icon = Image.open(icon_path)
        self.err_code_icon_tk = ImageTk.PhotoImage(self.err_code_icon)
        self.err_code_img = self.canvas.create_image(15, 10, image=self.err_code_icon_tk, anchor="nw")

        # keys
        self.key_state = self.canvas.create_text(
            size - 20, size - 40,
            text="Key: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="ne"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "key.png")
        self.key_icon = Image.open(icon_path)
        self.key_icon_tk = ImageTk.PhotoImage(self.key_icon)
        self.key_img = self.canvas.create_image(size - 110, size - 140, image=self.key_icon_tk, anchor="nw")

        # emergency stop
        self.e_stop = self.canvas.create_text(
            size - 20, 120,
            text="Emergency stop: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="ne"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "prohibit-inset.png")
        self.estop_icon = Image.open(icon_path)
        self.estop_icon_tk = ImageTk.PhotoImage(self.estop_icon)
        self.estop_img = self.canvas.create_image(size - 110, 10, image=self.estop_icon_tk, anchor="nw")

        # brakes
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "prohibit1.png")
        self.brake_icon = Image.open(icon_path)
        self.brake_icon_tk = ImageTk.PhotoImage(self.brake_icon)
        self.brake_img = self.canvas.create_image(size/2, size/2, image=self.brake_icon_tk, anchor="center")
        
        # firmware version
        self.fwver = self.canvas.create_text(
            20, size - 40,
            text="Firmware Version: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="nw"
        )
        base_path = os.path.dirname(__file__)
        icon_path = os.path.join(base_path, "icons", "terminal.png")
        self.fwver_icon = Image.open(icon_path)
        self.fwver_icon_tk = ImageTk.PhotoImage(self.fwver_icon)
        self.fwver_img = self.canvas.create_image(15, size - 150, image=self.fwver_icon_tk, anchor="nw")

        # hardware version
        self.hwver = self.canvas.create_text(
            20, size - 60,
            text="Hardware Version: --",
            fill="#56cc9d",
            font=("Space Grotesk", 10, "bold"),
            anchor="nw"
        )

        # system state
        self.sysstate = self.canvas.create_text(
            size/2, size/2 + 60,
            text="",
            fill="#56cc9d",
            font=("Space Grotesk", 24, "bold")
        )

    def set_power(self, power_percent):
        brightness = int((50 * power_percent / 100) + 35)  
        r = int(0x56 * brightness / 255)
        g = int(0xcc * brightness / 255)
        b = int(0x9d * brightness / 225)
        color = f"#{r:02x}{g:02x}{b:02x}"
        self.canvas.itemconfig(self.power_bar, fill=color)

    # speedometer and speed data packing
    def set_speed(self, speed):
        ratio = speed / self.max_speed
        extent = -360 * ratio   # clockwise needs negative values 

        self.canvas.itemconfig(self.speedometer_front, extent=extent)
        self.canvas.itemconfig(self.speed_text, text=str(speed))

    # data packing
    def show_data_drive(self, temps, battery, motor_current, motor_mode, power_percent, lights, state):
        # hiding irrelevant data 
        self.canvas.itemconfig(self.brake_overlay, state="hidden")
        self.canvas.itemconfig(self.err_code, state="hidden")
        self.canvas.itemconfig(self.key_state, state="hidden")
        self.canvas.itemconfig(self.e_stop, state="hidden")
        self.canvas.itemconfig(self.estop_img, state="hidden")
        self.canvas.itemconfig(self.err_code_img, state="hidden")
        self.canvas.itemconfig(self.key_img, state="hidden")
        self.canvas.itemconfig(self.brake_img, state="hidden")
        self.canvas.itemconfig(self.fwver_img, state="hidden")
        self.canvas.itemconfig(self.fwver, state="hidden")
        self.canvas.itemconfig(self.hwver, state="hidden")

        self.set_power(power_percent)

        # showing relevant data
        self.canvas.itemconfig(self.temp_text, text=f"Temp: {temps}°C", state="normal")
        self.canvas.itemconfig(self.battery_text, text=f"Battery: {battery}%", state="normal")
        self.canvas.itemconfig(self.current_text, text=f"Current: {motor_current}A", state="normal")
        self.canvas.itemconfig(self.mode_text, text=f"Mode: {motor_mode}", state="normal")
        self.canvas.itemconfig(self.power_percent, text=f"Power: {power_percent}%", state="normal")
        self.canvas.itemconfig(self.lights, text=f"Lights: {lights}", state="normal")
        self.canvas.itemconfig(self.lights, text=f"Lights: {lights}", state="normal")
        self.canvas.itemconfig(self.sysstate, text=f"{state}", state="normal")
        self.canvas.itemconfig(self.light_img, state="normal")
        self.canvas.itemconfig(self.current_img, state="normal")
        self.canvas.itemconfig(self.battery_img, state="normal")
        self.canvas.itemconfig(self.temp_img, state="normal")
        self.canvas.itemconfig(self.mmode_img, state="normal")
        self.canvas.itemconfig(self.power_img, state="normal")                
        self.canvas.itemconfig(self.speedometer_back, state="normal")
        self.canvas.itemconfig(self.speedometer_front, state="normal")
        self.canvas.itemconfig(self.speed_text, state="normal")
        
    
    def show_data_other(self, error_code, key_state, e_stop, state, fwver, hwver):
        # hiding irrelevant data 
        self.canvas.itemconfig(self.brake_overlay, state="hidden")
        self.canvas.itemconfig(self.temp_text, state="hidden")
        self.canvas.itemconfig(self.battery_text, state="hidden")
        self.canvas.itemconfig(self.current_text, state="hidden")
        self.canvas.itemconfig(self.mode_text, state="hidden")
        self.canvas.itemconfig(self.power_percent, state="hidden")
        self.canvas.itemconfig(self.lights, state="hidden")
        self.canvas.itemconfig(self.light_img, state="hidden")
        self.canvas.itemconfig(self.power_img, state="hidden")
        self.canvas.itemconfig(self.mmode_img, state="hidden")
        self.canvas.itemconfig(self.battery_img, state="hidden")
        self.canvas.itemconfig(self.temp_img, state="hidden")
        self.canvas.itemconfig(self.brake_img, state="hidden")
        self.canvas.itemconfig(self.current_img, state="hidden")
        self.canvas.itemconfig(self.speedometer_back, state="hidden")
        self.canvas.itemconfig(self.speedometer_front, state="hidden")
        self.canvas.itemconfig(self.speed_text, state="hidden")

        self.set_power(0)

        # showing relevant data
        self.canvas.itemconfig(self.err_code, text=f"Error code: {error_code}", state="normal")
        self.canvas.itemconfig(self.key_state, text=f"Key: {key_state}", state="normal")
        self.canvas.itemconfig(self.e_stop, text=f"Emergency break: {e_stop}", state="normal")
        self.canvas.itemconfig(self.fwver, text=f"Firmware version: {fwver}", state="normal")
        self.canvas.itemconfig(self.hwver, text=f"Hardware: {hwver}", state="normal")
        self.canvas.itemconfig(self.sysstate, text=f"{state}", state="normal")
        self.canvas.itemconfig(self.estop_img, state="normal")
        self.canvas.itemconfig(self.err_code_img, state="normal")
        self.canvas.itemconfig(self.key_img, state="normal")
        self.canvas.itemconfig(self.fwver_img, state="normal")
    
    def show_break_screen(self):
        self.canvas.itemconfig(self.brake_overlay, state="normal")
        self.canvas.tag_raise(self.brake_overlay)
        self.canvas.itemconfig(self.brake_img, state="normal")
        self.canvas.tag_raise(self.brake_img)
        
    def read_UART(self):
        global uart_conf

        try:
            # Try UART first
            line = uart_conf.readline().decode().strip()
            data = json.loads(line)

        except:
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, "temp_info.json")

            with open(file_path, "r") as file:
                data = json.load(file)


        if (data["ctrl"]["state"] == "DRIVE"):
            if (data["ctrl"]["break_active"] == "true"):
                self.show_break_screen()
            else:
                self.set_speed(data["drive"]["speed"])
                self.show_data_drive(
                    data["drive"]["temperature"], 
                    data["drive"]["battery_percentage"], 
                    data["drive"]["motor_current"], 
                    data["drive"]["motor_mode"],
                    data["ctrl"]["cmd"],
                    data["ctrl"]["light_active"],
                    "Drive")
        elif (data["ctrl"]["state"] == "ERROR" or data["ctrl"]["state"] == "INIT"):
            if (data["ctrl"]["state"] == "ERROR"):
                sysstate = "Error"
            elif (data["ctrl"]["state"] == "INIT"):
                sysstate = "Initialisation"
            self.show_data_other(data["ctrl"]["fault_code"], 
                                 data["ctrl"]["enable_active"], 
                                 data["ctrl"]["estop_active"],
                                 sysstate,
                                 data["FW_ver"],
                                 data["HW_ver"]
                                 )

# init window
main_window = ttk.Window(themename="solar")
main_window.title("Speedometer")

ui = speedometer(main_window)
ui.pack()

# main loop for UART updates
def main_loop():
    ui.read_UART()
    main_window.after(100, main_loop)

main_loop()
main_window.mainloop()