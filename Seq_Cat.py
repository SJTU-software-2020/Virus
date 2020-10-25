#病毒数据库处理
import re


def Get_File(filename):
    f = open(filename, 'r')
    a = []
    line = f.readline()
    line = line.replace('\n', '')

    while line:
        a.append(line.split('\t'))
        line = f.readline()
        line = line.replace('\n', '')

    f.close()
    return a

def Seq_Cat(DR_Method, VirusName):
    #读取文件
    DR = Get_File('Protein_DR.txt')
    Spacer = Get_File('Virus_Spacer.txt')
    #Spacer = Get_File('Virus_Spacer_CN.txt')   #中文版
    
    #变量定义
    method = ''     #3' or 5'
    outSeq = ''     #合成后的序列
    Length = 0      #Spacer长度
    DR_Seq = ''
    Spacer_Seq = ''
    Cas13_name = ''
    virus_name = ''

    #匹配字符串
    for m in DR:
        #print(m)
        pattern = re.compile(DR_Method)
        result = re.search(pattern, m[0])
        if result:
            Length = int(m[2])
            method = m[3]    #3'或5'
            DR_Seq = m[1]
            Cas13_name = m[0]
            break
    for s in Spacer:
        pattern = re.compile(VirusName)
        result = re.search(pattern, s[0])
        if result:
            Spacer_Seq = s[1][:Length - 1]
            virus_name = s[0]
            break

    #拼接基因序列
    if method == "3\'":
        outSeq = Spacer_Seq + DR_Seq
        print('SS:' + Spacer_Seq)
        print(virus_name + ' + ' + Cas13_name + ' = ' + outSeq)
    elif method == "5\'":
        outSeq = DR_Seq + Spacer_Seq
        print('SS:' + Spacer_Seq)
        print(Cas13_name+' \+ '+virus_name+' = '+outSeq)


Seq_Cat('Lwa','MERS-CoV')


