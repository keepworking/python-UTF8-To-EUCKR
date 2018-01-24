def convFileEnc(file1,file2):
    f = open(file1,'r');
    f2 = open(file2,'wb');

    lines = f.readlines()
    lines2 = []
    for line in lines:
        lines2.append(line.decode('utf-8').encode('euc-kr','ignore'))
    f2.writelines(lines2)
    f2.close()
    f.close()


if __name__ == '__main__':
    convFileEnc("content/utf8.csv","content/euckr.csv")
