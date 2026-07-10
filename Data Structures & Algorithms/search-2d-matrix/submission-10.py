class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low=0
        high= n*m-1
        mid=-1
        while(low<=high):
            mid=(high+low)//2
            r, c= divmod(mid,n)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                low=mid+1
            else:
                high=mid-1

        return False
            





        