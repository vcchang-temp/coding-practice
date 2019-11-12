# Flood Fill

# Time: O(n) -> DFS visits every node in 2D array with n cells in worst case
# Space: O(max(len(row), len(col))) -> space taken up by call stack depends on 
#                                      depth of recursion

from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int):
    if image[sr][sc] == newColor:
        return image
        
    fill(image, sr, sc, image[sr][sc], newColor)
    return image
    
def fill(image: List[List[int]], r: int, c: int, originalColor: int, newColor: int):
    if r < 0 or r >= len(image) or c < 0 or c >= len(image[r]) or image[r][c] != originalColor:
        return
        
    image[r][c] = newColor
    fill(image, r-1, c, originalColor, newColor)
    fill(image, r+1, c, originalColor, newColor)
    fill(image, r, c-1, originalColor, newColor)
    fill(image, r, c+1, originalColor, newColor)

if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr, sc, newColor = 1, 1, 2
    expected = [[2,2,2],[2,2,0],[2,0,1]]
    actual = floodFill(image, sr, sc, newColor)
    print(f"Flood-filled image {image} with {newColor}: {actual}")