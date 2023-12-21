class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for index in range((len(row)+1)//2):
                row[index],row[~index]=1-row[~index],1-row[index]
        return image 