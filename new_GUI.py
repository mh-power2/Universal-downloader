import tkinter as tk
from tkinter import messagebox, simpledialog

class UniversalDownloader:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Universal Downloader")

        # Set background color
        self.root.configure(bg='#F0F0F0')

        # Create main menu frame
        self.create_main_menu()

    def create_main_menu(self):
        # Destroy any existing frames
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create main menu frame
        main_menu_frame = tk.Frame(self.root, bg='#F0F0F0')
        main_menu_frame.pack(expand=True, fill='both', padx=50, pady=50)

        # Add buttons to the main menu with improved colors
        buttons = [
            ("Download Manager", self.show_download_manager, '#4CAF50'),
            ("Youtube Downloader", self.show_youtube_downloader, '#2196F3'),
            ("Soundcloud Downloader", self.show_soundcloud_downloader, '#FF9800'),
            ("Lightnovels Downloader", self.show_lightnovels_downloader, '#FFC107'),
            ("Spotify Downloader", self.show_spotify_downloader, '#E91E63'),
            ("Video Editing", self.show_video_editing, '#9C27B0'),
            ("Download Wallpapers", self.show_wallpapers_downloader, '#607D8B'),
            ("Google Drive Download", self.show_google_drive_downloader, '#795548'),
            ("Download Photos", self.show_photo_downloader, '#8BC34A'),
            ("Download Gimages", self.show_gimages_downloader, '#FF5722'),
            ("Advanced Options", self.show_advanced_options, '#03A9F4'),
            ("Quit", self.quit_program, '#FF0000')
        ]

        for text, command, color in buttons:
            button = tk.Button(main_menu_frame, text=text, command=command, width=20, bg=color, fg='white', font=('Arial', 10, 'bold'))
            button.pack(expand=True, fill='both', pady=5)

    def show_download_manager(self):
        # Destroy any existing frames
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create Download Manager frame
        download_manager_frame = tk.Frame(self.root, bg='#F0F0F0')
        download_manager_frame.pack(expand=True, fill='both', padx=50, pady=50)

        # Add buttons for Download Manager
        buttons = [
            ("Add Download", self.add_download, '#4CAF50'),
            ("Pause Download", self.pause_download, '#FF9800'),
            ("Resume Download", self.resume_download, '#2196F3'),
            ("Remove Download", self.remove_download, '#E91E63'),
            ("Schedule Link", self.schedule_link, '#FFC107'),
            ("Back", self.create_main_menu, '#607D8B'),
        ]

        for text, command, color in buttons:
            button = tk.Button(download_manager_frame, text=text, command=command, width=20, bg=color, fg='white', font=('Arial', 10, 'bold'))
            button.pack(expand=True, fill='both', pady=5)

    def add_download(self):
        url = simpledialog.askstring("Add Download", "Enter the URL:")
        if url:
            messagebox.showinfo("Download Added", f"Download added for URL: {url}")

    def pause_download(self):
        choice = messagebox.askquestion("Pause Download", "Choose an option:", 
                                       choices=["Pause All", "Selective Pause", "Go Back"])
        if choice == "Pause All":
            messagebox.showinfo("Pause Download", "All downloads paused")
        elif choice == "Selective Pause":
            messagebox.showinfo("Selective Pause", "Selective pause functionality goes here")
        # "Go Back" option does nothing for now

    def resume_download(self):
        choice = messagebox.askquestion("Resume Download", "Choose an option:",
                                       choices=["Resume All", "Selective Resume"])
        if choice == "Resume All":
            messagebox.showinfo("Resume Download", "All downloads resumed")
        elif choice == "Selective Resume":
            messagebox.showinfo("Selective Resume", "Selective resume functionality goes here")

    def remove_download(self):
        choice = messagebox.askquestion("Remove Download", "Choose an option:",
                                       choices=["Remove All", "Selective Remove"])
        if choice == "Remove All":
            messagebox.showinfo("Remove Download", "All downloads removed")
        elif choice == "Selective Remove":
            messagebox.showinfo("Selective Remove", "Selective remove functionality goes here")

    def schedule_link(self):
        url = simpledialog.askstring("Schedule Link", "Enter the URL:")
        if url:
            messagebox.showinfo("Schedule Link", f"Link scheduled for download: {url}")

    def show_youtube_downloader(self):
        messagebox.showinfo("YouTube Downloader", "Placeholder for YouTube Downloader")

    def show_soundcloud_downloader(self):
        messagebox.showinfo("Soundcloud Downloader", "Placeholder for Soundcloud Downloader")

    def show_lightnovels_downloader(self):
        messagebox.showinfo("Lightnovels Downloader", "Placeholder for Lightnovels Downloader")

    def show_spotify_downloader(self):
        messagebox.showinfo("Spotify Downloader", "Placeholder for Spotify Downloader")

    def show_video_editing(self):
        messagebox.showinfo("Video Editing", "Placeholder for Video Editing")

    def show_wallpapers_downloader(self):
        messagebox.showinfo("Download Wallpapers", "Placeholder for Wallpapers Downloader")

    def show_google_drive_downloader(self):
        messagebox.showinfo("Google Drive Download", "Placeholder for Google Drive Downloader")

    def show_photo_downloader(self):
        messagebox.showinfo("Download Photos", "Placeholder for Photo Downloader")

    def show_gimages_downloader(self):
        messagebox.showinfo("Download Gimages", "Placeholder for Gimages Downloader")

    def show_advanced_options(self):
        messagebox.showinfo("Advanced Options", "Placeholder for Advanced Options")

    def quit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# Create an instance of the UniversalDownloader class and run the program
universal_downloader = UniversalDownloader()
universal_downloader.run()