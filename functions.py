from PIL import Image
import os, json

workin_d =os.getcwd()
workin_d = workin_d.replace('\\','/')

def open_img(picture_name):
    img_path = f"/static/img/{picture_name}"
    workin_d = workin_d.replace('\\','/')
    path= workin_d + img_path
  
    img = Image.open(path) 
    sizes = img.size
    

    return sizes, img


def upload_file(up_file):
    img = Image.open(up_file) 
    sizes = img.size



    return sizes, img

def resize_img(func_open_img, name_file):
   
    #------ save path  -------------------
    dir_save = workin_d + '/static/img/'
    #-------------------------------------

    sizes = func_open_img[0]
    img = func_open_img[1]

    width = sizes[0]
    length = sizes[1]
    objective_width = 100
    prop =0

    if width>length:
        prop = round(width/length, 2)
    elif width < length:
        prop = round(length/width,2)
    elif width == length:
        prop = 2
    elif width <= objective_width:
        new_width = width
        new_length = length


    new_width= width
    new_length= length


    run = True
    if width > objective_width:
        while run == True:
            new_width = int(round(new_width/prop))
            new_length= int(round(new_length/prop))
            print('test',new_width, new_length)
            
            if new_width<=objective_width:
                run = False

    out = img.resize([new_width, new_length])
    out.save(dir_save+f"{name_file}")

    return (new_width, new_length)


#----------- open json file -------------

def open_json():
    with open('profile_picture.json') as file:
        json_file = json.load(file)
   
    return json_file

def save_json(file, json_data):
    with open(file,'w') as file:
        file.write(json.dumps(json_data, indent=4))



