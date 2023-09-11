def resolve(clause1, clause2):
    return [literal for literal in clause1 if -literal not in clause2] + [literal for literal in clause2 if -literal not in clause1]

def can_resolve(clause1, clause2):
    return any(-literal in clause2 for literal in clause1) or any(-literal in clause1 for literal in clause2)

def resolution(clauses):
    new_clauses = clauses.copy()
    while True:
        n = len(new_clauses)
        for i in range(n):
            for j in range(i + 1, n):
                if can_resolve(new_clauses[i], new_clauses[j]):
                    resolvent = resolve(new_clauses[i], new_clauses[j])
                    if not resolvent:
                        return True  # Contradiction found
                    if resolvent not in new_clauses:
                        new_clauses.append(resolvent)
        if len(new_clauses) == n:
            return False  # No new clauses can be generated

# Example usage
clauses = [[-1, 2], [-1, 2], [-1, 2],[-1, 2]]
result = resolution(clauses)
print("The clauses are unsatisfiable (contradictory)." if result else "The clauses are satisfiable.")

# def negate_literal(literal):
#     if literal.startswith("~"):
#         return literal[1:]
#     else:
#         return "~" + literal
    
# def resolve(clause1, clause2):
#     new_clause = []
#     for literal1 in clause1:
#         for literal2 in clause2:
#             if literal1 == negate_literal(literal2):
#                 new_clause = [lit for lit in (clause1 + clause2) if lit != literal1 and lit != literal2]
#                 return new_clause

# def resolution(premises, conclusion):
#     premises.append(negate_literal(conclusion))
#     clauses = [prem.split(" v ") for prem in premises]
#     while True:
#         new_clauses = []
#         for i in range(len(clauses)):
#             for j in range(i + 1, len(clauses)):
#                 resolvent = resolve(clauses[i], clauses[j])
#                 if not resolvent:
#                     return True # Empty clause, contradiction found
#                 new_clauses.append(resolvent)
#         if any(new_clause == clause for new_clause in new_clauses for clause in clauses):
#             return False # No more new clauses can be generated
#         clauses += new_clauses


# # Example premises and conclusion in CNF
# premises = ["P v Q", "~P v R", "~Q v R"]
# conclusion = "R"
# result = resolution(premises, conclusion)
# if result:
#     print("Conclusion follows from the premises.")
# else:
#     print("Conclusion does not follow from the premises.")