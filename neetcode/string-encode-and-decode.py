# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

import json

class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.dumps(strs)

    def decode(self, s: str) -> List[str]:
        return json.loads(s)
