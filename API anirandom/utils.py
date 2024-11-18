from PIL import Image, ImageTk


#image resizer method, returns the resized image

def image_set(image_path: str, x: int, y: int):
    pil_image = Image.open(image_path)
    resized_image = pil_image.resize((x, y), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    return tk_image
