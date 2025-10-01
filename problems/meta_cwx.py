# Your previous Plain Text content is preserved below:

# Input: "abbba"
# Output: "" ("abbba" => "aa" => "")

# Input: "ab"
# Output: "ab"

# Input: "abbaa"
# Output (alternative 1): ""  ("abbaa" => "aaa" => "")
# Output (alternative 2): "a"  ("abbaa" => "abb" => "a")


def remove_adjacent_duplicates(s):
    st = []
    prev = ""

    for c in s:
        if not st or c != st[-1]:
            if c != prev:
                st.append(c)
        else:
            prev = st.pop()
    
    res = "".join(st)
    return(res)

print(remove_adjacent_duplicates("abbba"))
print(remove_adjacent_duplicates("ab"))
print(remove_adjacent_duplicates("abbaa"))
print(remove_adjacent_duplicates("abbbb"))
print(remove_adjacent_duplicates("abbbc"))

