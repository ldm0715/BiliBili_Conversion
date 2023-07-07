import os
import sys
import json
import shutil
import subprocess

# 项目基础路径
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))


def open_file(folder_path, temp_path):
    files = os.listdir(folder_path)
    files_list = list()
    # print(files)
    for i in range(len(files)):
        file = files[i]
        extension = file.split(".")[-1]
        if extension == "m4s":
            files_list.append(file)
    file_size = dict()

    for i in range(len(files_list)):
        file = files_list[i]
        file_size[f"{file}"] = os.path.getsize(os.path.join(folder_path, file))

    sorted_keys = sorted(file_size.keys(), reverse=True)
    shutil.copy(os.path.join(folder_path, sorted_keys[1]), os.path.join(temp_path, "audio.m4s"))
    shutil.copy(os.path.join(folder_path, sorted_keys[0]), os.path.join(temp_path, "video.m4s"))
    files_list = [os.path.join(temp_path, i) for i in os.listdir(temp_path)]
    print(files_list)
    return files_list


def delete(files_path):
    for file in files_path:
        with open(file, "rb+") as f:
            data = f.read()
            result = b''
            for i in range(0, len(data)):
                temp_str = data[0:i]
                try:
                    # print(temp_str[-1])
                    if (temp_str[-1] == 0) & (len(temp_str) > 0):
                        result = data[i - 1:]
                        break
                except:
                    pass
            # 将文件指针移动到开头
            f.seek(0)
            f.write(result)
            f.close()


def get_video_title(folder_path):
    path = os.path.join(folder_path, ".videoInfo")
    # print(path)
    with open(path, "r", encoding="UTF-8") as f:
        data = f.read()
        data = json.loads(data)
        title = data["title"]
        title = replace_title(title)
        f.close()
    print(title)
    return title


def replace_title(title):
    replace_dict = {
        " ": "",  # 空格替换为空白字符
        "\\": "/",  # 反斜杠替换为正斜杠
        ":": "_",  # 冒号替换为下划线
        "\"": "",  # 引号删除
        "<": "",  # 尖括号删除
        ">": "",  # 尖括号删除
        "=": "-",  # 等号替换为短横线
        "|": "-",  # 竖线替换为短横线
    }
    for i in replace_dict.keys():
        title = title.replace(i, replace_dict[i])
    return title


def merge(file_path, tilte, new_folder_path, output_path):
    output_video_path = os.path.join(output_path, f"{tilte}.mp4")
    # print(output_video_path)
    try:
        # 强制覆盖
        command = f"ffmpeg -y -i {file_path[0]} -i {file_path[1]} -codec copy {output_video_path} "

        # subprocess.call(command, shell=True)
        subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        message = f"{tilte}.mp4 转化成功"
    except subprocess.CalledProcessError as e:
        print("命令行执行错误:", e)
        message = f"{tilte}.mp4 转化失败"
    finally:
        # 删除临时文件夹
        shutil.rmtree(new_folder_path)
        print(message)
    return message


def run(folder_path):
    temp_path = os.path.join(BASE_DIR, "temp")
    output_path = os.path.join(BASE_DIR, "output")
    os.makedirs(output_path, exist_ok=True)
    # 创建目标文件夹
    os.makedirs(temp_path, exist_ok=True)

    file_path = open_file(folder_path, temp_path)
    delete(file_path)
    print(file_path)
    title = get_video_title(folder_path)
    message = merge(file_path, title, temp_path, output_path)
    return message


# def batch_convert(path):
#     with open(path, "r", encoding="UTF-8") as f:
#         data = f.readlines()
#         path_list = [i.strip("\n") for i in data]
#         f.close()
#     message_list = list()
#     for i in range(len(path_list)):
#         folder_path = path_list[i]
#         message = run(folder_path)
#         message_list.append(message)
#     print(message_list[0])
#     return message_list


if __name__ == '__main__':
    folder_path = r"F:\bilibili\1186953752"
    # path = os.path.join(BASE_DIR, "videolist.txt")

    run(folder_path)
    # batch_convert()
