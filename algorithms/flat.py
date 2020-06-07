# 给你们个题玩玩：
# 写一个flat函数，拍平一个数组，数组内可能有多重嵌套，例如这种：
# [1,"2",[3,"4",[5,undefined,[null,[1,[2,3,[{}]]]]],null]]

# 拍平后返回

# [1, "2", 3, "4", 5, undefined, null, 1, 2, 3, {}, null]

# 要求不能使用语言提供的原生flat方法，不能使用第三方库，不能使用递归
# [1,2,[3,[4]],5]
def flat(datas):
    if(not datas):
        return datas
    res,stack = [],[]
    tmp,tmp_index = datas,0
    tmp_len = len(tmp)
    while(tmp_index<tmp_len):
        if(type(tmp[tmp_index])==list):
            if(tmp_index!=tmp_len-1):
                stack.append(tmp)
                stack.append(tmp_index)
            tmp,tmp_index = tmp[tmp_index],0
            tmp_len = len(tmp)
            continue
        res.append(tmp[tmp_index])
        if(tmp_index == tmp_len-1 and len(stack) ):
            tmp_index,tmp = stack.pop(),stack.pop()
            tmp_len = len(tmp)
        tmp_index += 1
    return res

print(flat([1,[[2],[3],[1,[2,[3]]]]]))

        
        

