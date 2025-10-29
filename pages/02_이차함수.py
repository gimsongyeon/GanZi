import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 앱 제목
st.title("이차함수 그래프 분석")
st.write("""
이 앱은 이차함수 `y = ax^2`의 그래프를 학습하는 도구입니다.
슬라이더를 이용해 `a` 값을 변화시키며 그래프의 변화를 실시간으로 확인할 수 있습니다.
""")

# `a` 값을 입력받는 슬라이더 (값 범위: -10 to 10)
a = st.slider("a 값 선택", -10.0, 10.0, 1.0)

# x 값 범위 설정
x = np.linspace(-10, 10, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label=f"y = {a}x^2", color='blue')
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)
ax.grid(True)

# 타이틀과 레이블
ax.set_title(f"y = {a}x^2 의 그래프")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

# 그래프 출력
st.pyplot(fig)

# `a` 값에 따른 그래프 분석
if a > 0:
    st.write(f"a 값이 {a}일 때, 그래프는 아래로 볼록합니다.")
else:
    st.write(f"a 값이 {a}일 때, 그래프는 위로 볼록합니다.")

# `a` 값 절댓값에 따른 폭 변화 설명
if abs(a) > 1:
    st.write("a의 절댓값이 1보다 크면, 그래프가 더 좁아집니다.")
elif abs(a) < 1:
    st.write("a의 절댓값이 1보다 작으면, 그래프가 더 넓어집니다.")
else:
    st.write("a의 절댓값이 1일 때, 그래프는 보통의 폭을 가집니다.")
