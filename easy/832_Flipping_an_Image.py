class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # reverses row, and num^1 to toggle
        # O(N) (where N is every element) time, O(1) space
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image)):
                image[i][j] ^= 1
        
        return image
        

