import sympy

x, y, z = sympy.symbols('x y z')


def s_poly(poly_first, poly_second):
    lt_f = sympy.LT(poly_first)
    lt_s = sympy.LT(poly_second)
    #print(sympy.lcm(lt_f, lt_s))
    return sympy.Poly(sympy.lcm(lt_f, lt_s) * ((poly_first/lt_f)-(poly_second/lt_s)))


# def largest_term(f):
#     poly = f.as_poly(x, y, z)
#     monomials = poly.monoms()
#     highest_degree_monomial = max(monomials, key=lambda monomial: sum(monomial))
#     coeff_of_highest_term = poly.coeff_monomial(highest_degree_monomial)
#     return coeff_of_highest_term*x**highest_degree_monomial[0]*y**highest_degree_monomial[1]*z**highest_degree_monomial[2]

def largest_term(f):
    poly = f.as_poly(x, y, z)
    monomials = poly.monoms()
    highest_degree_monomial = max(monomials, key=lambda monomial: sum(monomial))
    coeff_of_highest_term = poly.coeff_monomial(highest_degree_monomial)
    return coeff_of_highest_term * x ** highest_degree_monomial[0] * y ** highest_degree_monomial[1] * z ** \
        highest_degree_monomial[2]


# def largest_term(f, s):
#     poly = f.as_poly(s)
#     monomials = poly.monoms()
#     for i in range(len(monomials)):
#         highest_degree_monomial = 1
#     coeff_of_highest_term = poly.coeff_monomial(highest_degree_monomial)
#     return coeff_of_highest_term*x**highest_degree_monomial[0]*y**highest_degree_monomial[1]*z**highest_degree_monomial[2]

# def general_divide2(f, gs):
#     h = f
#     qs = [0] * len(gs)
#     for i in range(len(gs)):
#         while h != 0:
#             # lt_gi = largest_term(gs[i], [x, y, z])
#             # lt_h = largest_term(h, [x, y, z])
#
#             lt_gi = largest_term(gs[i])
#             lt_h = largest_term(h)
#
#             # print(largest_term(h))
#             # print('----')
#             # print(h)
#             # print(gs[i])
#             # print(lt_h)
#             # print(lt_gi)
#             # print(lt_gi.free_symbols)
#             # print(lt_h.free_symbols)
#             if set(lt_gi.free_symbols).issubset(set(lt_h.free_symbols)):
#                 q, r = sympy.div(lt_h, lt_gi)
#                 if r == 0:
#                     h = sympy.expand(h - (gs[i] * q))
#                     qs[i] = qs[i] + q
#                 else:
#                     break
#             else:
#                 break
#     return h, qs


def general_divide2(f, gs):
    h = sympy.Poly(f, [x, y, z])
    qs = [0] * len(gs)
    for i in range(len(gs)):
        gs[i] = sympy.Poly(gs[i], [x, y, z])
        while h != 0:
            lt_gi = largest_term(gs[i])
            lt_h = largest_term(h)

            if set(lt_gi.free_symbols).issubset(set(lt_h.free_symbols)):
                q, r = sympy.div(lt_h, lt_gi)
                if r == 0:
                    h = h - (gs[i] * q)
                    qs[i] = qs[i] + q
                else:
                    break
            else:
                break
    return h, qs


def general_divide(f, gs):
    h = f
    r = 0
    qs = [0] * len(gs)
    while h != 0:
        # div_occurred = False
        for i in range(len(gs)):
            div_occurred = False
            while not div_occurred:
                lt_gi = sympy.LT(gs[i])
                lt_h = sympy.LT(h)
                # print('----')
                # print(h)
                # print(gs[i])
                # print(lt_h)
                # print(lt_gi)
                # print(sympy.rem(lt_h, lt_gi))
                # print(sympy.quo(lt_h, lt_gi))
                # print('####')
                if sympy.rem(lt_h, lt_gi) == 0:
                    div = sympy.quo(lt_h, lt_gi)
                    qs[i] = qs[i] + div
                    h = sympy.simplify(h - div * gs[i])
                    div_occurred = True
                if not div_occurred:
                    r = r + lt_h
                    h = sympy.simplify(h - lt_h)

    return r, qs

