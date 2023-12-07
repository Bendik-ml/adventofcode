from day1 import collect_digits, combine_digits, find_and_replace_number_words

s = "5pfzht "
replaced_s = find_and_replace_number_words(s)
collected_s = collect_digits(replaced_s)
combined_s = combine_digits(replaced_s)

print(replaced_s)
print(collected_s)
print(combined_s)
