from PIL import Image
import random
from bisect import bisect

def image_to_ascii(image_input, x, y):
    
    greyscale = [
            " ",
            " ",
            ".,-",
            "/|\\",
            "]/()[",
            "K4ZGNDXY5P*Q",
            "W8KMA",
            "#%$"
        ] #list of characters which represent different zonebounds
    
    BlackToWhite=[36,72,108,144,180,216,252] #setting the value of greyscale to the zonebounds
    
    im=Image.open(image_input) #open image
    im=im.resize((x, y),Image.BILINEAR) #resize image
    im=im.convert("L") # convert to mono
 
    str=""
    for y in range(0,im.size[1]):
        for x in range(0,im.size[0]): #defines areas of image
            lum=255-im.getpixel((x,y)) #finds out greyscale of areas in the image (0 is white)
            row=bisect(BlackToWhite,lum)
            possibles=greyscale[row] #converts greyscale to ascii
            str=str+possibles[random.randint(0,len(possibles)-1)] #puts the lines of ascii together
        str=str+"\n"
 
    return(str) #prints result

end_live = image_to_ascii("images/youlive.jpg", 80, 30)
end_die = image_to_ascii("images/youdied.jpg", 80, 30)
end_escape = image_to_ascii("images/youescaped.jpg", 110, 30)


# all possible endings
endings = {
"live": end_live,
"die": end_die,
"escape": end_escape
}