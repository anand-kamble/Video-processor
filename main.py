from Class.VIDEO_SUBTITLE_MAKER import VIDEO_SUBTITLE_MAKER
import tkinter
from tkinter import filedialog, Menu, Text, END, Label
from tkinter.messagebox import showinfo
from utils import openLogs, OpenFile


class MAIN:
    def __init__(self):
        self.VIDEO_SUBTITLE_MKR = VIDEO_SUBTITLE_MAKER()
        self.root = tkinter.Tk()
        self.root.title('Video Subtitle Maker')
        self.root.resizable(True, True)
        self.root.geometry('1280x720')
        menu = Menu(self.root)
        self.root.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="View Logs", command=openLogs)
        fileMenu.add_command(label="Exit", command=self.kill)
        menu.add_cascade(label="File", menu=fileMenu)
        link = Label(self.root, text="GitHub Repo", font=(
            'Helveticabold', 15), fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>",
                  lambda e: OpenFile("https://github.com/anand-kamble/Video-processor"))
        open_button = tkinter.Button(
            self.root,
            text='Open a File',
            command=self.select_file
        )
        open_button.pack(expand=True)
        T = Text(self.root, height=5, width=52)
        T.insert(END, "Our Github:\n@anand-kamble\n@Aniket-Tathe")
        T.pack()

        self.root.mainloop()

        pass

    def select_file(self):
        video_path = filedialog.askopenfilename(title='Select the video',
                                                filetypes=(('media files', "*.mp4"), ('All files', '*.*')))

        if (self.VIDEO_SUBTITLE_MKR.add_video(video_path=video_path)):
            self.VIDEO_SUBTITLE_MKR.prepare().generate_required_files()
            showinfo(
                title='Conversion Completed.',
                message="File saved to " + video_path
            )
            self.root.destroy()
        else:
            print("Failed to load video. Please check the path you entered\nExiting...")
            self.VIDEO_SUBTITLE_MKR.destoy()
            self.root.destroy()

    def kill(self):
        self.VIDEO_SUBTITLE_MKR.destoy()
        self.root.destroy()


MAIN()
