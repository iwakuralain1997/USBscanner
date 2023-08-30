import tkinter as tk
from tkinter import ttk
import usb.core

class USBScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lain's USB scanner")

        self.tree = ttk.Treeview(self.root, columns=("Device", "Vendor ID", "Product ID"))
        self.tree.heading("#1", text="Device")
        self.tree.heading("#2", text="Vendor ID")
        self.tree.heading("#3", text="Product ID")
        self.tree.pack(padx=10, pady=10)

        self.scan_button = tk.Button(self.root, text="Scan USB Devices", command=self.scan_devices)
        self.scan_button.pack(pady=5)

    def scan_devices(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing entries

        devices = usb.core.find(find_all=True)

        for device in devices:
            self.tree.insert("", "end", values=(device, "0x{:04x}".format(device.idVendor), "0x{:04x}".format(device.idProduct)))

def main():
    root = tk.Tk()
    app = USBScannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
