# description yet to be framed

def bin_search_tree(original_list,query_number,error=0):
    leng=len(original_list)
    mid_len=leng//2
    mid_len_out=leng//2 + error
    #mid_len1=len(listt)
    mid_num=original_list[mid_len]
    if query_number==mid_num:
        # return mid_len+error
        print(mid_len_out)
    elif query_number<mid_num:
        new_lis=original_list[:mid_len]
        bin_search_tree(new_lis,query_number,error)
    elif query_number>mid_num:
        new_lis = original_list[mid_len+1:]
        error=error+mid_len+1
        bin_search_tree(new_lis,query_number,error)
x=[2,3,5,6,8,10,11,13,16,22,33,56,100]
y=100
bin_search_tree(x,y)


