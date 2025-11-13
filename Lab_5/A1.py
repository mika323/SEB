def short_text(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему недождь) () (())'
print(short_text(text))

