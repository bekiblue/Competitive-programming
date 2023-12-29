class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat=[]
        for row in range(m):
            mat.append([])
            for col in range(n):
                mat[row].append("")
        for guard in guards:
            mat[guard[0]][guard[1]]="G"
        for wall in walls:
            mat[wall[0]][wall[1]]="W"
        count=0
        for guard in guards:
                row=guard[0]
                col=guard[1]
                if mat[row][col]!="G":
                    continue   
                # Marking to the left
                for c in range(col-1,-1,-1):
                    if mat[row][c]=="":
                        mat[row][c]="M"
                        count+=1 
                    elif mat[row][c]=="W" or  mat[row][c]=="G":
                        break
                #Marking to the right
                for c in range(col+1,n):
                    if mat[row][c]=="":
                        mat[row][c]="M"
                        count+=1 
                    elif mat[row][c]=="W" or  mat[row][c]=="G":
                        break
                #Marking to the top
                for r in range(row-1,-1,-1):
                    if mat[r][col]=="":
                        mat[r][col]="M"
                        count+=1
                    elif mat[r][col]=="W" or mat[r][col]=="G" :
                        break
                #Marking to the bottom
                for r in range(row+1,m):
                    if mat[r][col]=="":
                        mat[r][col]="M"
                        count+=1
                    elif mat[r][col]=="W" or mat[r][col]=="G" :
                        break
        
        return m*n-len(guards)-len(walls)-count
                
                
                
