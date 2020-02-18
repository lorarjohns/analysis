def generate_cases(size):
    if size > 1:
        for var in generate_cases(size-1):
            yield var + [True]
            yield var + [False]

    else:
        yield [True]
        yield [False]

def truth_table(vars, funcs):
    output = ""

    len_vars = str(len(vars))
    len_funcs = str(len(funcs))
    output += r"\begin{center}\begin{tabular}{*{" + len_vars + r"}{c}|*{" + len_funcs + r"}{c}}"

    labels = vars + [func[0] for func in funcs]
    output += "&".join(["$"+label+"$" for label in labels]) + r"\\"
    output += "\n\\hline\n"

    tftext = {True: 'T', False: 'F'}

    for tf in generate_cases(len(vars)):
        values = [tftext[val] for val in tf]
        values += ([tftext[func[1](*tf)] for func in funcs])
        output += "&".join(values) + "\\\\\n"

    output += r"\end{tabular}\end{center}"

    return output

if __name__ == "__main__":

    # print(truth_table(['p', 'q'], [(r'p \implies q', lambda p, q: (p and q) or (not p))]))
    # print(truth_table(['p','q'], [(r'\neg(p \land q)', lambda p, q: not(p and q)),
    #                               (r'\iff', lambda p,q: (not(p and q) and ((not p) or (not q))) 
    #                               or (not(not(p and q)) and not((not p) or (not q)))),
    #                               (r"[(\neg p) \lor (\neg q)]", lambda p, q: not p or not q ) ]))
    # print(truth_table(['p', 'q'], [(r'\neg(p \implies q)', lambda p, q: not((p and q) or (not p))),
    #                                (r'\(\cancel{\iff}\)', lambda p, q: (not((p and q) or (not p))) and ((q and p) or (not q))),
    #                                (r'q \implies p', lambda p, q: (q and p) or (not q))
    # ]
    # ))
    # print(truth_table(['p', 'q'], [(r'p \implies \neg q', lambda p, q: (p and not q) or (not p))]))