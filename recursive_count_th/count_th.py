'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    count = {"counter":0}
    wast = {'wast':0}
    completed = {'compl':0}
    def innercount(word):
        newword = list(word)
        index1 = 1
        index2 = 2
        #print(newword)
        #if newword[0] is not None and newword[1] is not None:
        if index1 < len(word) and index2 < len(word):

            if newword[0] == 't' and newword[1] == 'h':
                count['counter'] += 1
                wast['wast'] = 0
            
            if newword[0] == 'h' and wast['wast'] == 1:
                count['counter'] += 1
            
            if newword[1] == 't':
                wast['wast'] = 1
            #passedword = newword[1]:
            innercount(newword[1:])

        else:
            #print (count.get('counter'))
            completed['compl'] = 1
            #return count.get('counter')
    
    innercount(word)

    if completed['compl'] == 1:
        #print (count.get('counter'))
        return count.get('counter')
    
    
    #return word.count('th')
    
print(count_th('abcthxyz'))    
    
    
