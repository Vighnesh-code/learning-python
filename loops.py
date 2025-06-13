student_scores = [100, 124, 165, 173, 189, 169, 146]
# total_scores  = sum(student_scores, 0)
# print(total_scores)

# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

print(f"Sum of all student scores: {sum(student_scores)}")

# print(max(student_scores))

max = student_scores[0]

for score in student_scores:
    if score >= max:
        max = score

print(f"Max Number is: {max}")

