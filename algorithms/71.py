# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
import re
class Solution:
    paten = re.compile('/|(?<=/)\.{1,2}[\w\.]{0,}|\w+')
    def simplifyPath(self, path: str) -> str:
        strs = self.paten.findall(path)
        aList = []
        for tmp in strs:
            # . 当前本身抵消 ..上一级 /根目录
            if tmp == ".":
                if len(aList)==1:
                    continue
                aList.pop()
                continue
            if tmp =="..":
                if len(aList)==1:
                    continue
                aList.pop()
                aList.pop()
                continue
            if  len(aList)!=0 and  tmp == "/":
                if aList[len(aList)-1]=="/":
                    continue
            aList.append(tmp)
        if(len(aList)!=1 and  aList[len(aList)-1]=="/"):
            aList.pop()
        return "".join(aList)
    def s2(self, path: str) ->str:
        r = []
        for s in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)
solution = Solution()
solution.simplifyPath("/a/b/../c/./..hidden..aa..aa..vv..")
print(solution.s2("/a/b/../c/./..hidden..aa..aa..vv.."))