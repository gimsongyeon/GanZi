import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 페이지 설정 ---
st.set_page_config(layout="centered")
st.title("📊 이차함수 $y=ax^2$ 그래프 탐구")
st.markdown("---")

st.header("1. $a$ 값 조절하기")

# --- a 값 슬라이더 설정 ---
# -5부터 5까지, 0을 제외하고 조절 가능하도록 합니다.
# 0 근처의 작은 값도 확인할 수 있도록 step을 작게 설정할 수 있습니다.
a = st.slider(
    '**계수 $a$ 값 선택:** ($a \ne 0$)',
    min_value=-5.0,
    max_value=5.0,
    value=1.0,  # 초기값 설정
    step=0.1,
    key='a_slider'
)

# a가 0인 경우를 막기 위한 처리
if a == 0:
    st.error("⚠️ $a$는 0이 될 수 없습니다. 슬라이더를 움직여 다른 값을 선택해 주세요.")
    a = 1.0 # 임시로 1로 설정하여 그래프 오류를 방지

st.subheader(f"현재 함수: $y = {a}x^2$")
st.markdown("---")


# --- 그래프 생성 및 표시 ---
st.header("2. 그래프 시각화")

# x 범위 설정
x = np.linspace(-5, 5, 400)
# y 값 계산
y = a * x**2

# Matplotlib을 사용하여 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f'$y={a}x^2$', color='blue')
ax.axhline(0, color='gray', linewidth=0.5) # x축
ax.axvline(0, color='gray', linewidth=0.5) # y축
ax.set_title(f'이차함수 $y = {a}x^2$ 그래프')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(-10, 10) # y축 범위 고정 (a 값이 너무 커져도 안정적으로 보이도록)

# 그래프를 Streamlit에 표시
st.pyplot(fig)



# --- 분석 결과 정리 ---
st.header("3. 그래프 성질 분석 (귀납적 추론)")

st.write(f"선택된 $a$ 값: **${a}$**")

### 1. 볼록 방향 ($a$의 부호에 따른 분석)
st.subheader("🔸 볼록 방향 ( $a$의 부호 )")

if a > 0:
    st.success(f"**$a > 0$** 일 때, 그래프는 **아래로 볼록**합니다.")
else: # a < 0
    st.error(f"**$a < 0$** 일 때, 그래프는 **위로 볼록**합니다.")

### 2. 그래프의 폭 ($|a|$의 절댓값에 따른 분석)
st.subheader("🔹 그래프의 폭 ( $|a|$의 절댓값 )")
abs_a = abs(a)

st.info(f"$|a| = **{abs_a:.1f}**$ 입니다.")
if abs_a > 1:
    st.markdown("**$|a|$의 절댓값**이 클수록 그래프의 폭은 $y=x^2$보다 **좁아집니다**.")
elif 0 < abs_a < 1:
    st.markdown("**$|a|$의 절댓값**이 작을수록 그래프의 폭은 $y=x^2$보다 **넓어집니다**.")
else: # abs_a == 1
    st.markdown("기준 그래프 $y=x^2$와 폭이 **같습니다**.")

st.markdown("""
* **귀납적 추론:** 여러 $a$ 값에 대한 그래프를 그려보고,
    $|a|$이 커질수록 그래프가 $y$축에 **가까워져 폭이 좁아지는** 경향을 스스로 확인해 보세요.
""")
