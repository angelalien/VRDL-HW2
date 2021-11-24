# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:22:02 2021
@author: Lien
"""
# 嘗試直接從mat轉txt
import os
import h5py
import mmcv


def get_box_data(index, hdf5_data):
    """
    get `left, top, width, height` of each picture
    :param index:
    :param hdf5_data:
    :return:
    """
    meta_data = dict()
    meta_data["height"] = []
    meta_data["label"] = []
    meta_data["left"] = []
    meta_data["top"] = []
    meta_data["width"] = []

    def print_attrs(name, obj):
        vals = []
        if obj.shape[0] == 1:
            vals.append(obj[0][0])
        else:
            for k in range(obj.shape[0]):
                vals.append(int(hdf5_data[obj[k][0]][0][0]))
        meta_data[name] = vals

    box = hdf5_data["/digitStruct/bbox"][index]
    hdf5_data[box[0]].visititems(print_attrs)
    return meta_data


def get_name(index, hdf5_data):
    name = hdf5_data["/digitStruct/name"]
    return "".join([chr(v[0]) for v in hdf5_data[name[index][0]]])


def convert_mat_to_txt(image_list):
    for idx, image_name in enumerate(image_list):
        out_file = open(
            "data/labels/%s.txt" % (image_name[:-4]), "w", encoding="utf-8"
        )
        image = mmcv.imread("data/images/" + image_name)
        height, width = image.shape[:2]

        bboxes = get_box_data(int(image_name[:-4]) - 1, mat_data)
        for i in range(len(bboxes["height"])):
            cls_id = int(bboxes["label"][i])
            if cls_id == 10:
                cls_id = 0
            x = (2.0 * bboxes["left"][i] + bboxes["width"][i]) / (2.0 * width)
            y = (2.0 * bboxes["top"][i] + bboxes["height"][i]) / (2.0 * height)
            w = bboxes["width"][i] / width
            h = bboxes["height"][i] / height
            bb = [x, y, w, h]
            out_file.write(
                str(cls_id) + " " + " ".join([str(a) for a in bb]) + "\n"
            )


mat_data = h5py.File("data/images/digitStruct.mat", "r")
mat_data_size = mat_data["/digitStruct/name"].size

data_listdir = os.listdir("data/images")
for image_set in data_listdir:
    if image_set[-1] == "g":
        convert_mat_to_txt(data_listdir)
