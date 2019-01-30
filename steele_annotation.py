import json
from collections import defaultdict

name_box_id = defaultdict(list)
id_name = dict()
f = open(
    "/home/eli/Downloads/steele/annotations/annotations_train_2018.json",
    encoding='utf-8')
data = json.load(f)

def process_images(images_json_list):
    images_dict = dict()
    for image in images_json_list:
        images_dict[image["id"]] = image["file_name"]
    return images_dict
    
images = process_images(data['images'])

annotations = data['annotations']
for ant in annotations:
    id = ant['image_id']
    name = "/home/eli/Downloads/steele/images/%s"%(images[id])
    cat = ant['category_id']
    name_box_id[name].append([ant['bbox'], cat])

f = open('train.txt', 'w')
for key in name_box_id.keys():
    f.write(key)
    box_infos = name_box_id[key]
    for info in box_infos:
        x_min = int(info[0][0])
        y_min = int(info[0][1])
        x_max = x_min + int(info[0][2])
        y_max = y_min + int(info[0][3])

        box_info = " %d,%d,%d,%d,%d" % (
            x_min, y_min, x_max, y_max, int(info[1]))
        f.write(box_info)
    f.write('\n')
f.close()
