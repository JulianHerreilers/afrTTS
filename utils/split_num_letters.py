def split_nums_letters(seq):
    import re

    def convert_num_word(num):
        nums = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','30','40','50','60','70','80','90','100', '1000']
        num_words = ['nul', 'een','twee', 'drie','vier','vyf', 'ses','sewe', 'agt', 'nege','tien','elf','twaalf','dertien','veertien','vyftien','sestien','sewentien', 'agtien', 'negentien', 
            'twintig','dertig', 'veertig', 'vyftig', 'sestig', 'sewentig', 'tagtig', 'negentig', 'honderd', 'duisend']
        num_tens = ['10','11','12','13','14','15','16','17','18','19','20','30','40','50','60','70','80','90']
        num_words_tens = ['tien','elf','twaalf','dertien','veertien','vyftien','sestien','sewentien', 'agtien', 'negentien', 
            'twintig','dertig', 'veertig', 'vyftig', 'sestig', 'sewentig', 'tagtig', 'negentig']
        a = int(num)
        ans = []
        i=0
        #print(a)
        num_word_equiv = ""
        tu_both = 0
        t_added = 0
        h_added = 0
        tt_th_both = 0
        tt_added = 0
        
        u =  str(int(a%10))
        t =  str(int((a%100)/10))
        h =  str(int((a%1000)/100))
        tu = str(a%100)
        th = str(int(a/1000)-int(a/10000)*10)
        tt = str(int(a/10000))
        tt_th = str(int(a/1000))

        if tt_th:
            for k in num_tens:
                if tt_th == k and k!="0":
                    index = num_tens.index(k)
                    num_word_equiv = num_word_equiv + num_words_tens[index]
                    t_added = 1
                    tt_th_both = 1
                    break
        if tt:
            for k in nums:
                if tt == k and k!="0" and tt_th_both == 0:
                    index = nums.index(k)
                    num_word_equiv = num_word_equiv + num_words[index]
                    tt_added = 1
                    break
        if th:
            for k in nums:
                if th == k and k!="0" and tt_th_both == 0:
                    index = nums.index(k)
                    if tt_added: num_word_equiv = num_word_equiv +" en "+  num_words[index]
                    else: num_word_equiv = num_word_equiv +  num_words[index]
                    t_added =1
                    break
        
        if t_added: num_word_equiv += " duisend"

        if h:
            for k in nums:
                if h == k and k!="0":
                    index = nums.index(k)
                    if t_added: num_word_equiv = num_word_equiv + " en "+ num_words[index] + ' honderd'
                    else: num_word_equiv = num_word_equiv + num_words[index] + ' honderd'
                    
                    h_added = 1
                    break
        if tu:
            for k in nums:
                if tu == k and k!="0":
                    index = nums.index(k)
                    if h_added: num_word_equiv = num_word_equiv +" en "+ num_words[index]
                    else: num_word_equiv = num_word_equiv + num_words[index]
                    tu_both = 1
                    break
        if t:
            for k in nums:
                if t == k and tu_both==0 and k!="0":
                    index = nums.index(k)
                    if h_added: num_word_equiv = num_word_equiv +" en "+ num_words[index]
                    else: num_word_equiv = num_word_equiv + num_words[index]
                    break
        if u:
            for k in nums:
                if u == k and tu_both==0 and k!="0":
                    index = nums.index(k)
                    if h_added: num_word_equiv = num_word_equiv +" en "+ num_words[index]
                    else: num_word_equiv = num_word_equiv + num_words[index]
                    break
            
        return num_word_equiv

    c = re.findall(r'[A-Za-z\']+|\d+', seq) #Source: https://stackoverflow.com/questions/28290492/python-splitting-numbers-and-letters-into-sub-strings-with-regular-expression
    ans = []
    for j,i in enumerate(c):
        if i.isdigit():
            ans.append(convert_num_word(i))
        else: ans.append(i)

    return ans