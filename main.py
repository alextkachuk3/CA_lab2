import sympy

x, y, z = sympy.symbols('x y z')

symbols = [z, y, x]


def general_division_remainder(G, s):
    k = 0
    result = s
    for f in G:
        for symbol in symbols:
            quo = sympy.quo(sympy.LT(result, symbol), sympy.LT(f, symbol))
            while quo != 0:
                result = result - quo * f
                quo = sympy.quo(sympy.LT(result, symbol), sympy.LT(f, symbol))
    return result


def s_poly(poly_first, poly_second):
    lt_f = sympy.LT(poly_first)
    lt_s = sympy.LT(poly_second)
    return sympy.Poly(sympy.lcm(lt_f, lt_s) * ((poly_first / lt_f) - (poly_second / lt_s)), [z, y, x])


def groebner_basis(G):
    step = 0
    U = []

    for i in range(0, len(G)):
        for j in range(0, len(G)):
            if i != j:
                U.append((G[i], G[j]))

    for pair in U:
        print('Step {}'.format(str(step)))
        print('Pair {}, {}'.format(str(pair[0].args), str(pair[1].args)))
        cur_s_poly = s_poly(pair[0], pair[1])
        print('S-poly {}'.format(str(cur_s_poly.args[0])))
        remainder = general_division_remainder(G, cur_s_poly)
        if remainder != 0:
            if remainder in G or -remainder in G:
                break
            else:
                G.append(remainder)
                for f in G:
                    U.append((f, remainder))

        step += 1
    return G


poly1 = sympy.Poly(y * z + x ** 2 + z, [z, y, x])
poly2 = sympy.Poly(x * y * z + x * z - y ** 3, [z, y, x])
poly3 = sympy.Poly(x * z + y ** 2, [z, y, x])

basis = groebner_basis([poly1, poly2, poly3])

print('--------------------------------------------------')
print('Result')
for p in basis:
    print(p.args[0])
