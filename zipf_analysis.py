import sys

def load_word_counts(filename):
    """
    Load a list of (word, count, percentage) tuples from a file where each
    line is of the form "word count percentage". Lines starting with # are
    ignored.
    """
    counts = []
    with open(filename, "r") as input_fd:
        for line in input_fd:
            if not line.startswith("#"):
                fields = line.split()
                counts.append((fields[0], int(fields[1]), float(fields[2])))
    return counts

def top_two_word(counts):
    """
    Given a list of (word, count, percentage) tuples,
    return the top two word counts.
    """
    limited_counts = counts[0:2]
    count_data = [count for (_, count, _) in limited_counts]
    return count_data

def top_ten_word(counts):
    """
    Given a list of (word, count, percentage) tuples,
    return the top ten word counts.
    """
    limited_counts = counts[0:10]
    count_data = [count for (_, count, _) in limited_counts]
    return count_data

def zipf_analysis(input_file):
    counts = load_word_counts(input_file)
    top_ten = top_ten_word(counts)
    return top_ten
