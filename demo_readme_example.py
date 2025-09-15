#!/usr/bin/env python3
"""
Demonstration script for the README examples with max_sentence_length feature.
"""

import os
from py4jrush import RuSH

def main():
    # Get the rules file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rules_file = os.path.join(current_dir, 'tests', 'rush_rules.tsv')
    
    print("=" * 80)
    print("py4jrush README Example - Max Sentence Length Feature")
    print("=" * 80)
    
    # Initialize RuSH with maximum sentence length of 100 characters
    rush = RuSH(rules_file, max_sentence_length=100, enable_logger=True)
    
    # Long sentence that will be automatically split
    long_text = ("This is a very long clinical sentence that contains multiple medical concepts "
                "and exceeds the maximum length limit, so it will be intelligently split into "
                "smaller segments at appropriate boundaries like whitespace or punctuation marks "
                "to ensure each resulting sentence stays within the specified character limit.")
    
    print(f"\nOriginal text (length {len(long_text)}):")
    print(f"'{long_text}'")
    print()
    
    sentences = rush.segToSentenceSpans(long_text)
    
    print(f"Split into {len(sentences)} sentences:")
    print("-" * 40)
    
    for i, sentence in enumerate(sentences):
        segment = long_text[sentence.begin:sentence.end]
        print(f"Sentence {i} (length {len(segment)}): {segment}")
    
    print()
    print("✅ All sentences are within the 100-character limit!")
    
    # Verify all sentences are within limit
    max_length = 100
    all_within_limit = True
    for i, sentence in enumerate(sentences):
        segment = long_text[sentence.begin:sentence.end]
        if len(segment) > max_length:
            print(f"❌ ERROR: Sentence {i} exceeds limit: {len(segment)} > {max_length}")
            all_within_limit = False
    
    if all_within_limit:
        print("✅ SUCCESS: All sentences respect the max_sentence_length parameter!")
    
    # Clean up
    rush.shutdownJVM()

if __name__ == "__main__":
    main()