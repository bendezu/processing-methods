from src.picture.Picture import Picture


def or_pic(pic1: Picture, pic2: Picture):
    return Picture(pic1.title + " | " + pic2.title, pic1.matrix | pic2.matrix)

def and_pic(pic1: Picture, pic2: Picture):
    return Picture(pic1.title + " & " + pic2.title, pic1.matrix & pic2.matrix)

def xor_pic(pic1: Picture, pic2: Picture):
    return Picture(pic1.title + " ^ " + pic2.title, pic1.matrix ^ pic2.matrix)

def plus_pic(pic1: Picture, pic2: Picture):
    return Picture(pic1.title + " + " + pic2.title, pic1.matrix + pic2.matrix)

def minus_pic(pic1: Picture, pic2: Picture):
    return Picture(pic1.title + " - " + pic2.title, pic1.matrix - pic2.matrix)
