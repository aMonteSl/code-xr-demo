import re
from collections import defaultdict, deque

# Low CCN (Cyclomatic Complexity Number) function:
def add_numbers(a, b):
    """
    Return the sum of two numbers.
    """
    return a + b


# Low CCN function:
def is_even(number):
    """
    Check if a number is even.
    """
    return number % 2 == 0


# Low CCN function:
def greet_user(name):
    """
    Return a greeting message for the given user name.
    """
    return f"Hello, {name}!"


# Low CCN function:
def factorial(n):
    """
    Compute the factorial of n recursively.
    """
    if n < 2:
        return 1
    return n * factorial(n - 1)


# Medium CCN function:
def fibonacci_sequence(n):
    """
    Generate a list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


# High CCN function:
def complex_password_validator(password):
    """
    Validate a password string against multiple rules:
      - Minimum length 8
      - At least one uppercase letter
      - At least one lowercase letter
      - At least one digit
      - At least one special character (!@#$%^&*()-_+=)
      - No sequences of three or more repeating characters
      - No common dictionary words (simple example)
      - No whitespace
    Returns True if all rules are satisfied, False otherwise.
    """
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()-_+=")
    dictionary_words = {"password", "admin", "welcome", "letmein", "qwerty"}
    prev_char = ''
    repeat_count = 1

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
        elif char.isspace():
            return False  # immediate fail on whitespace

        if char == prev_char:
            repeat_count += 1
            if repeat_count >= 3:
                return False
        else:
            prev_char = char
            repeat_count = 1

    if not (has_upper and has_lower and has_digit and has_special):
        return False

    pwd_lower = password.lower()
    for word in dictionary_words:
        if word in pwd_lower:
            return False

    return True


# High CCN function:
def analyze_text(text):
    """
    Perform a rudimentary text analysis:
      - Normalize whitespace and lowercase
      - Remove punctuation
      - Tokenize into words
      - Count word frequencies
      - Identify top-N frequent words
      - Classify overall sentiment based on simple keywords
    Returns a dict with 'word_counts' and 'sentiment'.
    """
    # Normalize and remove punctuation
    normalized = text.strip().lower()
    normalized = re.sub(r"[^\w\s]", " ", normalized)  # replace punctuation with spaces
    tokens = normalized.split()

    # Count frequencies
    freq = defaultdict(int)
    for token in tokens:
        freq[token] += 1

    # Identify top 5 frequent words
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top_five = sorted_items[:5]

    # Simple sentiment classification
    positive_words = {"good", "happy", "joy", "excellent", "fortunate", "correct", "superior"}
    negative_words = {"bad", "sad", "pain", "terrible", "unfortunate", "wrong", "inferior"}
    pos_count = 0
    neg_count = 0

    for word, count in freq.items():
        if word in positive_words:
            pos_count += count
        elif word in negative_words:
            neg_count += count

    if pos_count > neg_count:
        sentiment = "Positive"
    elif neg_count > pos_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "word_counts": freq,
        "top_five": top_five,
        "sentiment": sentiment
    }


# High CCN function:
def find_all_paths(graph, start, end):
    """
    Find all possible paths in a directed acyclic graph from start node to end node.
    graph: dict where keys are node IDs and values are lists of neighbor node IDs.
    Returns a list of paths, where each path is a list of node IDs.
    """
    all_paths = []

    def dfs(current, path, visited):
        # visited set prevents revisiting nodes in the current path (avoid cycles)
        if current == end:
            all_paths.append(path.copy())
            return

        if current not in graph:
            return

        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            path.append(neighbor)
            dfs(neighbor, path, visited)
            path.pop()
            visited.remove(neighbor)

    dfs(start, [start], {start})
    return all_paths


# High CCN function:
def knapsack_bruteforce(values, weights, capacity):
    """
    Solve the 0/1 knapsack problem with brute force.
    values: list of item values
    weights: list of item weights (same length as values)
    capacity: maximum weight capacity
    Returns the maximum achievable value without exceeding capacity.
    """
    n = len(values)
    max_value = 0

    # Iterate over all possible subsets (2^n combinations)
    for subset_mask in range(1 << n):
        total_weight = 0
        total_value = 0

        for i in range(n):
            # Check if the i-th item is included in the subset
            if subset_mask & (1 << i):
                total_weight += weights[i]
                total_value += values[i]
                if total_weight > capacity:
                    # Early break for overweight subset
                    break
        else:
            # Only check value if weight is within capacity
            if total_value > max_value:
                max_value = total_value

    return max_value


if __name__ == "__main__":
    # Demonstration of low CCN functions
    print(greet_user("Alice"))                 # "Hello, Alice!"
    print("2 + 3 =", add_numbers(2, 3))         # 5
    print("Is 10 even?", is_even(10))           # True
    print("5! =", factorial(5))                 # 120
    print("First 7 Fibonacci numbers:", fibonacci_sequence(7))

    # Demonstration of password validator (high CCN)
    sample_passwords = [
        "P@ssw0rd", "Secure#123", "aaaaBBB1!", "Admin123!", "Complex-XY9"
    ]
    for pwd in sample_passwords:
        result = complex_password_validator(pwd)
        print(f"Password '{pwd}' valid?", result)

    # Demonstration of text analysis (high CCN)
    sample_text = (
        "This is a good day. I feel happy and joyful! "
        "However, there is also some bad news."
    )
    analysis_result = analyze_text(sample_text)
    print("Top five words:", analysis_result["top_five"])
    print("Sentiment:", analysis_result["sentiment"])

    # Demonstration of graph path finding (high CCN)
    sample_graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["G"],
        "E": ["G", "H"],
        "F": ["H"],
        "G": [],
        "H": []
    }
    paths = find_all_paths(sample_graph, "A", "G")
    print("All paths from A to G:", paths)

    # Demonstration of knapsack (high CCN)
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_val = knapsack_bruteforce(values, weights, capacity)
    print("Max knapsack value:", max_val)
