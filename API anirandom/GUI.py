import tkinter as tk
from tkinter import *
from utils import image_set
from apiLoader import get_random_anime
from PIL import Image, ImageTk
from io import BytesIO
import requests

class MyWindow:
    def __init__(self):
        self.window = tk.Tk()

    def create_window(self, title, size="768x800", bg="black"):
        # Set the window title
        self.window.title(title)
        # Set the window size
        self.window.geometry(size)
        # Set the background color
        self.window.configure(bg=bg)
        # Makes it unresizable
        self.window.resizable(False, False)

        icon_img = Image.open("日本动画片.jpeg")
        photo = ImageTk.PhotoImage(icon_img)
        self.window.wm_iconphoto(False, photo)

        # Canvas for my images
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Banner in my first screen (PNG Made by: Molz)
        self.banner_1 = image_set("rule_5banner.png", 768, 150)
        self.canvas.create_image(380, 135, image=self.banner_1)

        # Sets my title at top middle
        self.label_title = tk.Label(self.window,
                               text="Randomizer",
                               font=('Arial', 40, 'bold'),
                               fg='pink')
        self.label_title.place(x=260, y=5)

        # Info label
        self.label_info = tk.Label(self.window,
                              text="Preference Options",
                              font=('Arial', 40, 'bold'),
                              fg='pink')
        self.label_info.place(x=180, y=220)

        # Reference titles
        self.label_tlgenre = tk.Label(self.window, text="Genres", font=('Arial', 40, 'bold'), fg='pink')
        self.label_tlsources = tk.Label(self.window, text="Source", font=('Arial', 40, 'bold'), fg='pink')
        self.label_tlstatus = tk.Label(self.window, text="Status", font=('Arial', 40, 'bold'), fg='pink')

        self.label_tlgenre.place(x=40, y=280)
        self.label_tlsources.place(x=295, y=280)
        self.label_tlstatus.place(x=550, y=280)

        # Lists:
        genres_lst = ["Action", "Adventure", "Avant Garde", "Award Winning", "Boys Love", "Comedy", "Drama", "Fantasy",
                      "Girls Love", "Gourmet", "Horror", "Mystery", "Romance", "Sci-Fi", "Slice of Life", "Sports",
                      "Supernatural", "Suspense", "Ecchi", "Erotica", "Hentai"]

        source_lst = ["4-koma manga", "Book", "Card game", "Digital manga", "Game", "Light novel", "Manga",
                      "Mixed media", "Music", "Novel", "Original", "Other", "Picture book", "Radio", "Unknown",
                      "Visual novel", "Web manga"]
        status_lst = ["Finished Airing", "Not yet aired", "Currently Airing"]

        # Genre list box
        self.list_genre = tk.Listbox(self.window,
                                     font=('Arial', 20, 'bold'),
                                     fg='pink',
                                     width=15,
                                     selectmode=tk.MULTIPLE,
                                     exportselection=False)
        for x in genres_lst:
            self.list_genre.insert(tk.END, x)

        self.list_genre.place(x=40, y=350)
        self.list_genre.bind('<<ListboxSelect>>', lambda event: self.limit_selection(event, self.list_genre, 3))

        # Source list box
        self.list_sources = tk.Listbox(self.window,
                                       font=('Arial', 20, 'bold'),
                                       fg='pink',
                                       width=15,
                                       selectmode=tk.SINGLE,
                                       exportselection=False)
        for x in source_lst:
            self.list_sources.insert(tk.END, x)

        self.list_sources.place(x=295, y=350)

        # Status list box
        self.list_status = tk.Listbox(self.window,
                                      font=('Arial', 20, 'bold'),
                                      fg='pink',
                                      width=15,
                                      selectmode=tk.SINGLE,
                                      exportselection=False)
        for x in status_lst:
            self.list_status.insert(tk.END, x)

        self.list_status.place(x=550, y=350)

        submit_button = Button(self.window, text="Submit", command=self.submit, font=('Arial', 40, 'bold'), fg='pink')
        submit_button.place(x=313, y=650)

        # Run the main event loop to display the window
        self.window.mainloop()

    # Limits the selection
    def limit_selection(self, event, listbox, limit):
        selected_indices = listbox.curselection()
        if len(selected_indices) > limit:
            listbox.selection_clear(selected_indices[-1])

    def submit(self):
        selected_genres = [self.list_genre.get(i) for i in self.list_genre.curselection()]
        selected_sources = [self.list_sources.get(i) for i in self.list_sources.curselection()]
        selected_statuses = [self.list_status.get(i) for i in self.list_status.curselection()]

        user_preference = {
            "genres": selected_genres,
            "status": selected_statuses,
            "source": selected_sources
        }
        print("User Preferences:", user_preference)

        anime_data = []
        for anime_details in get_random_anime(user_preference):
            ani_name = anime_details["ani_name"]
            genres = anime_details["genres"]
            source = anime_details["source"]
            status = anime_details["status"]
            img_url = anime_details.get("img_url", "Unknown")  # Make sure to handle cases where img_url might not exist
            # Extract other fields as needed

            anime_data.append({
                "ani_name": ani_name,
                "genres": genres,
                "source": source,
                "status": status,
                "img_url": img_url,
                # Include other fields here
            })

        # Print or use the fetched anime data
        print("Fetched Anime Data:", anime_data)
        self.show_results_page(anime_data)

    def show_results_page(self, anime_data):
        self.canvas.pack_forget()
        self.label_title.place_forget()
        self.label_info.place_forget()
        self.label_tlgenre.place_forget()
        self.label_tlsources.place_forget()
        self.label_tlstatus.place_forget()
        self.list_genre.place_forget()
        self.list_sources.place_forget()
        self.list_status.place_forget()


        #all my aesthetic stuff
        self.new_page = tk.Frame(self.window, bg='white')
        self.new_page.pack(fill='both', expand=True)

        self.sec_canvas = tk.Canvas(self.new_page, width=800, height=600, bg="white")
        self.sec_canvas.pack(fill=tk.BOTH, expand=True)

        # Banner in my Second screen (PNG Made by: Taste)
        self.banner_2 = image_set("rule_5banner2.png", 768, 150)
        self.sec_canvas.create_image(380, 135, image=self.banner_2)

        self.label_title_2 = tk.Label(self.new_page,
                                    text="Results",
                                    font=('Arial', 40, 'bold'),
                                    fg='pink')
        self.label_title_2.place(x=310, y=5)

        # Display anime results
        self.x_textpos = 120
        self.x_position = 50  # Initial y position for the results
        for anime in anime_data:
            name = anime['ani_name']
            genre =','.join(anime['genres'])
            source = anime['source']
            status = anime['status']

            self.sec_canvas.create_text(self.x_textpos, 280, text=name, fill='pink',
                                        font=("Arial", 15, 'bold'))
            self.sec_canvas.create_text(self.x_textpos, 520, text=genre, fill='pink',
                                        font=("Arial", 15, 'bold'))
            self.sec_canvas.create_text(self.x_textpos, 540, text=source, fill='pink',
                                        font=("Arial", 15, 'bold'))
            self.sec_canvas.create_text(self.x_textpos, 560, text=status, fill='pink',
                                        font=("Arial", 15, 'bold'))

            if anime['img_url'] != "Unknown":
                # Download the image from the URL
                img_path = requests.get(anime['img_url'])

                if img_path.status_code == 200:
                    # Open the image using PIL
                    img = Image.open(BytesIO(img_path.content))

                    # Resize the image if necessary
                    resized_img = img.resize((150, 200))

                    # Convert the resized image to a PhotoImage object
                    img_final = ImageTk.PhotoImage(resized_img)
                    # Create a Label widget to display the image
                    img_label = tk.Label(self.new_page, image=img_final, bg='white')
                    img_label.image = img_final  # Keep a reference to avoid garbage collection
                    img_label.place(x=self.x_position,y=300 )

            self.x_position += 255
            self.x_textpos += 255

        # Back button
        back_button = tk.Button(self.new_page, text="Back", command=self.hide_new_page, font=('Arial', 40, 'bold'),
                                fg='pink')
        back_button.place(x=315, y=650)

    def hide_new_page(self):
        self.new_page.pack_forget()  # Hide the new page
        # Show all the previous widgets
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.label_title.place(x=260, y=5)
        self.label_info.place(x=180, y=220)
        self.label_tlgenre.place(x=40, y=280)
        self.label_tlsources.place(x=295, y=280)
        self.label_tlstatus.place(x=550, y=280)
        self.list_genre.place(x=40, y=350)
        self.list_sources.place(x=295, y=350)
        self.list_status.place(x=550, y=350)
