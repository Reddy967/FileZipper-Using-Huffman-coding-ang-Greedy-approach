import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Overloading comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Count frequency of each character
    frequency = Counter(text)
    
    # Create a priority queue
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return

    # If it's a leaf node, store the code
    if root.char is not None:
        codes[root.char] = current_code
        return

    # Traverse left and right subtrees
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_encoding(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    
    # Encode the text
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes, root

def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        
        if current_node.char is not None:  # Leaf node
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# Test the Huffman coding
if __name__ == "__main__":
    input_text = "this is an example of huffman encoding"
    print("Original text:", input_text)

    encoded_text, codes, root = huffman_encoding(input_text)
    print("\nEncoded text:", encoded_text)
    print("\nHuffman Codes:", codes)

    decoded_text = huffman_decoding(encoded_text, root)
    print("\nDecoded text:", decoded_text)
    
    assert input_text == decoded_text, "The decoded text does not match the original!"
