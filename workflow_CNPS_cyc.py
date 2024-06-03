# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:21:56 2024

@author: sunhongtao
"""

########################################################################
#  wf_CNPS_cyc  : 地球化学循环(碳循环(甲烷M), 氮循环(N), 磷循环(P), 硫循环(S))
#  author : 孙洪涛
#  date   : 2024-03-26
########################################################################

"""
########################################################################

1. 根据输入文件，组合成新的smk工程文件，放在工作目录下
2. 打印work.sh，启动分析
3. 打印抓结果、check脚本，生成data_release脚本，上传脚本

########################################################################
"""

import os
import argparse
import sys
import textwrap
#os.chdir("E:\\personal_demand\\workflow_CNPS_cyc\\bin")

sys.path.append("/TJPROJ5/META_ASS/meta/sunhongtao/script/workflow_CNPS_cyc/lib")
import load_config



#读取project.yaml文件，根据文件中的选项，组合成新的smk文件
def get_smk()





def get_option():
    parse = argparse.ArgumentParser(description='This script is used to wf_CNPS_cyc')
    parse.add_argument("--project", type=str,required=True, help="project.yaml")
    parse.add_argument("--workdir", type=str,required=True, help="./")
    parse.add_argument("--config",  required=False, 
                       default="/TJPROJ5/META_ASS/meta/sunhongtao/script/workflow_CNPS_cyc/lib/config.yaml",
                       help="lib目录和环境配置文件(yaml)")
    #parse.add_argument("--step",    type=str,required=True, help="1234")
    args = parse.parse_args()
    
    project = os.path.abspath(args.project)
    workdir = os.path.abspath(args.workdir)
    config  = os.path.abspath(args.config)

    return project,workdir,config




def get_config(config_file):
    #============读取配置文件，生成字典=========
    config=load_config.load_yaml_file(config_file)
    return config



def write_execute_shell(cmd,script_name):
     with open(script_name,"w") as script_file:
        script_file.writelines(textwrap.dedent(cmd.lstrip('\n')))
        os.chmod(script_name, 0o755)
     return None


def main():
    """
    主函数
    """
    #外部传参
    project,workdir,config=get_option()
    #读取配置文件,config为字典格式的全局变量
    config=get_config(config_file)
    #删除并新建工作目录
    if os.path.exists(output):
        os.system(f"rm -r {output}")
    os.makedirs(output)
    #更改工作目录到输出目录
    os.chdir(output)
    

    return None


if __name__=="__main__":
    main()
















