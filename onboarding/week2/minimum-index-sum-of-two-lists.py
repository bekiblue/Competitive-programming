class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dic={}
        mnm=float("inf")
        answer=[]
        for index,word in enumerate(list1):
            if not list1_dic.get(word,None):
                list1_dic[word]=index
        for index,word in enumerate(list2):
            if word in list1_dic:
                if list1_dic[word]+index < mnm:
                    answer=[word]
                    mnm=list1_dic[word]+index
                elif list1_dic[word]+index == mnm:
                    answer.append(word)
                else:
                    continue
        return answer