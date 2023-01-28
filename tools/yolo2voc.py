# 将txt格式转换成xml格式数据集
from xml.dom.minidom import Document
import os
import cv2


def yolo_to_voc(pic_path, txt_path, xml_path):
  dic = ['餐盘', '鲜橙多', '冰红茶', '奶茶', '米饭', '番茄炒蛋', '肉米蒸蛋', '耗油生菜', '香酥鸡米花', '麻婆豆腐',
         '青椒土豆丝', '芝士牛肉饼', '孜然鸭胸', '肉米炖蛋', '香辣大鸡块', '辣子鸡', '彩椒猪柳', '杏鲍菇豇豆肉丝',
         '吉士翅根', '炸臭豆腐', '俄罗斯大肉串', '双色卷心菜', '本帮酱鸭', '刀豆土豆', '炒青菜', '炒杭白菜', '彩椒牛柳',
         '炸鸡柳', '干锅千叶豆腐', '牛排薯条', '咖喱鸡块', '香酥鸭', '蚝油生菜', '川芹腿排', '香烤鸡块', '避风塘大虾',
         '虾皮卷心菜', '杏鲍菇牛仔粒', '肉多多烤肠', '菠萝小酥肉', '梅干菜烧肉', '咖喱牛肉', '炸鸡腿', '菌菇烩豆腐',
         '蒜泥油麦菜', '莴笋肉丝', '炸响铃', '冬瓜毛豆肉片', '排骨年糕', '椒盐咕咾肉', '烂糊肉丝', '炸细薯条',
         '葱爆鸭胸', '卤汁豆腐干', '萝卜牛肉', '虎皮凤爪', '胡萝卜花菜肉片', '鱼香肉丝', '香干烧鸭块', '藤椒鸡柳',
         '鱼香茄子', '香酥鱼米花', '川香鸡柳', '炸猪排', '肉丝粉丝', '酸辣大白菜', '港式盐焗鸡', '红烧大排',
         '葱爆五花肉', '葱油莴笋丝', '双菇土豆肉片', '地锅鸡', '百叶结烧肉', '地三鲜', '青椒茭白肉丝', '油豆腐烧肉',
         '回锅肉', '炒塔菜', '椒盐小酥肉', '农家小炒肉', '红烩牛肉', '奶香霸王鱼条', '鱼香海带丝', '菌菇面筋肉片',
         '虾皮牛心菜', '翡翠银芽肉丝', '宫保鸡丁', '手撕包菜', '蒜香排条', '葱油鸡腿', '水晶虾仁', '有机花菜肉片',
         '黑椒鸡块', '香炸猪排', '樱花果木烤翅', '香干烧肉', '莴笋肉片', '孜然鱿鱼条']
  files = os.listdir(txt_path)
  for i, name in enumerate(files):
    xml_builder = Document()
    annotation = xml_builder.createElement("annotation")  # 创建annotation标签
    xml_builder.appendChild(annotation)
    txt_file = open(txt_path + name)
    txt_list = txt_file.readlines()
    img = cv2.imread(pic_path + name[0:-4] + ".jpg")  # 注意这里的图片后缀，.jpg/.png
    p_height, p_width, p_depth = img.shape

    folder = xml_builder.createElement("folder")  # folder标签
    folder_content = xml_builder.createTextNode("datasetRGB")
    folder.appendChild(folder_content)
    annotation.appendChild(folder)

    filename = xml_builder.createElement("filename")  # filename标签
    filename_content = xml_builder.createTextNode(name[0:-4] + ".jpg")
    filename.appendChild(filename_content)
    annotation.appendChild(filename)

    size = xml_builder.createElement("size")  # size标签
    width = xml_builder.createElement("width")  # size子标签width
    width_content = xml_builder.createTextNode(str(p_width))
    width.appendChild(width_content)
    size.appendChild(width)

    height = xml_builder.createElement("height")  # size子标签height
    height_content = xml_builder.createTextNode(str(p_height))
    height.appendChild(height_content)
    size.appendChild(height)

    depth = xml_builder.createElement("depth")  # size子标签depth
    depth_content = xml_builder.createTextNode(str(p_depth))
    depth.appendChild(depth_content)
    size.appendChild(depth)

    annotation.appendChild(size)

    for j in txt_list:
      oneline = j.strip().split(" ")
      object_tag = xml_builder.createElement("object")  # object 标签
      pic_name = xml_builder.createElement("name")  # name标签
      name_content = xml_builder.createTextNode(dic[int(oneline[0])])
      pic_name.appendChild(name_content)
      object_tag.appendChild(pic_name)

      pose = xml_builder.createElement("pose")  # pose标签
      pose_content = xml_builder.createTextNode("Unspecified")
      pose.appendChild(pose_content)
      object_tag.appendChild(pose)

      truncated = xml_builder.createElement("truncated")  # truncated标签
      truncated_content = xml_builder.createTextNode("0")
      truncated.appendChild(truncated_content)
      object_tag.appendChild(truncated)

      difficult = xml_builder.createElement("difficult")  # difficult标签
      difficult_content = xml_builder.createTextNode("0")
      difficult.appendChild(difficult_content)
      object_tag.appendChild(difficult)

      bnd_box = xml_builder.createElement("bndbox")
      xmin = xml_builder.createElement("xmin")  # xmin标签
      math_data = int(((float(oneline[1])) * p_width + 1) - (float(oneline[3])) * 0.5 * p_width)
      xmin_content = xml_builder.createTextNode(str(math_data))
      xmin.appendChild(xmin_content)
      bnd_box.appendChild(xmin)

      ymin = xml_builder.createElement("ymin")
      math_data = int(((float(oneline[2])) * p_height + 1) - (float(oneline[4])) * 0.5 * p_height)
      ymin_content = xml_builder.createTextNode(str(math_data))
      ymin.appendChild(ymin_content)
      bnd_box.appendChild(ymin)

      xmax = xml_builder.createElement("xmax")
      math_data = int(((float(oneline[1])) * p_width + 1) + (float(oneline[3])) * 0.5 * p_width)
      xmax_content = xml_builder.createTextNode(str(math_data))
      xmax.appendChild(xmax_content)
      bnd_box.appendChild(xmax)

      ymax = xml_builder.createElement("ymax")
      math_data = int(((float(oneline[2])) * p_height + 1) + (float(oneline[4])) * 0.5 * p_height)
      ymax_content = xml_builder.createTextNode(str(math_data))
      ymax.appendChild(ymax_content)
      bnd_box.appendChild(ymax)

      object_tag.appendChild(bnd_box)

      annotation.appendChild(object_tag)

    f = open(xml_path + name[0:-4] + ".xml", 'w')
    xml_builder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
    print(xml_path + name[0:-4] + ".xml")
    f.close()


if __name__ == "__main__":
  pic_path = "D:\\EAC-DATA-YOLO\\images\\"
  txt_path = "D:\\EAC-DATA-YOLO\\labels\\"
  xml_path = "D:\\EAC-DATA-YOLO\\xml\\"
  yolo_to_voc(pic_path, txt_path, xml_path)
