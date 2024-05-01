import os
from typing import List,Union,Tuple

def list_files_with_suffix(directory:str, suffix:Tuple) -> Union[List[str],str]:
    try:
        # 列出指定目录中的所有文件和子目录
        files = os.listdir(directory)

        # 筛选出指定后缀的文件
        filtered_files = [file for file in files if file.endswith(suffix)]
        print(f"获取{suffix}文件","\n"*2,"*"*20,"\n"*2,f"开始进行操作(文件名称是)：{filtered_files}")
        return filtered_files
    except FileNotFoundError:
        raise FileNotFoundError("目录不存在")

    except Exception as e:
        raise f"发生错误: {e}"


# directory = "."  # 替换成你要列出文件的目录路径
# suffix = ".txt"  # 替换成你想要筛选的文件后缀
# files_list = list_files_with_suffix(directory, suffix)
# print(f"目录中的以 {suffix} 后缀结尾的文件:")
# print(files_list)
