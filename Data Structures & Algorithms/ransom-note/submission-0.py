class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
 
        ransom_dict = defaultdict(int)
        mag_dict = defaultdict(int)

        for l in ransomNote:
            ransom_dict[l] += 1
        
        for l in magazine:
            mag_dict[l] += 1
        print(mag_dict)

        for k,v in ransom_dict.items():
            if k not in mag_dict:
                return False
            elif v > mag_dict[k]:
                return False
        
        return True
