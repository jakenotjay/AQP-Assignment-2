def E(L, m_l):
    return L**2+L-(3 * m_l)

L = range(0, 10, 1)

for i in range(len(L)):
    m_l = range(-L[i], L[i]+1, 1)

    print("For L=", L[i])

    for j in range(len(m_l)):
        print("For Ml=", m_l[j], "E is equal to ", E(L[i], m_l[j]))

