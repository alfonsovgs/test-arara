def is_token_valid(token):
    return token in ['(', ')', '[', ']']


def is_bracket_open(token):
    return token in ['(', '[']


def is_bracket_close(token):
    return token in [')', ']']


def tokens_match(previous_token, current_token):
    if previous_token == '[' and current_token == ']':
        return True
    elif previous_token == '(' and current_token == ')':
        return True

    return False


def multiple_brackets(strParam):
    # Get only valid tokens
    tokens = [token for token in strParam if is_token_valid(token)]
    tokens_proc = []
    brackets_counter = 0

    # tokens should be [()] or (()]

    if tokens:
        for token in tokens:
            if is_bracket_open(token):
                tokens_proc.append(token)
            elif is_bracket_close(token):
                if tokens_proc:
                    previous_token = tokens_proc[-1]

                    # if previus token match with current close token is a correct match
                    if tokens_match(previous_token, token):
                        tokens_proc.pop()
                        brackets_counter += 1
                    else:
                        # token doesn't match correctly
                        return 0
                else:
                    return 0  # token doesn't match correctly
    else:
        # Without tokens
        return 1

    return f'1 {brackets_counter}'


if __name__ == "__main__":
    # keep this function call here
    print(multiple_brackets(input()))
