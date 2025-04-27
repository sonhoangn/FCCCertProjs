def arithmetic_arranger(problems, show_answers=False):
    arrange_problems=[]
    if len(problems) < 6:
        for x in problems:
            first_operand=x.split()[0]
            operator=x.split()[1]
            second_operand=x.split()[2]
            if (operator == "+") or (operator == "-"):
                if (len(first_operand)>4) or (len(second_operand)>4):
                    return f'Error: Numbers cannot be more than four digits.'
                else:
                    if first_operand.isnumeric() and second_operand.isnumeric():
                        longest_operand_length=max(len(first_operand),len(second_operand))
                        top_line=first_operand.rjust(longest_operand_length+2)
                        bottom_line=operator+" "+second_operand.rjust(longest_operand_length)
                        separator="-"*(longest_operand_length+2)

                        result=""
                        if show_answers:
                            if operator == "+":
                                result=str(int(first_operand)+int(second_operand)).rjust(longest_operand_length+2)
                            elif operator == "-":
                                result=str(int(first_operand)-int(second_operand)).rjust(longest_operand_length+2)

                        arrange_problems.append((top_line,bottom_line,separator,result))
                    else:
                       return f'Error: Numbers must only contain digits.'
            else:
                return "Error: Operator must be '+' or '-'."

        upper_row=(" "*4).join([item[0] for item in arrange_problems])
        lower_row=(" "*4).join([item[1] for item in arrange_problems])
        separator_row=(" "*4).join([item[2] for item in arrange_problems])

        if show_answers:
            result_row=(" "*4).join([item[3] for item in arrange_problems])
            return f"{upper_row}\n{lower_row}\n{separator_row}\n{result_row}"
        else:
            return f"{upper_row}\n{lower_row}\n{separator_row}"
    else:
        return "Error: Too many problems."

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))