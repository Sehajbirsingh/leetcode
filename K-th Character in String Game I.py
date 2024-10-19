#K-th Character in String Game I
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        
        # Keep performing operations until word length is >= k
        while len(word) < k:
            # Generate next string by transforming each character
            next_string = ""
            for char in word:
                # If char is 'z', wrap around to 'a', else move to next char
                if char == 'z':
                    next_string += 'a'
                else:
                    next_string += chr(ord(char) + 1)
            
            # Append generated string to original word
            word += next_string
        
        # Return the k-th character (k-1 since indexing starts at 0)
        return word[k-1]