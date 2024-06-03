def linear_search(haystack:list, needle) -> int:
    """
    Find and return the index of a specific element
	If the element is not in the list, return -1
	>>> linear_search([5,8,12],8)
	1
	
	>>> linear_search([5,8,12],9)
	-1
    """
    for i in range(len(haystack)):
        print(print(haystack[i]))
        if haystack[i] == needle:
            return i
    return -1

def main():
	i = linear_search([10,9,8,7,4,1],1)
	print(i)

if __name__ == "__main__":
	main()
