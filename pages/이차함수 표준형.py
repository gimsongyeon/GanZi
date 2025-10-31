import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 페이지 설정 ---
st.set_page_config(layout="centered", page_title="이차함수 일반형↔표준형 변환 학습")

st.title("🔄 이차함수 일반형 → 표준형 변환 학습기")
st.markdown("""
이 앱은 이차함수의 **일반형** $y = ax^2 + bx + c$를 **표준형** $y = a(x-p)^2 + q$로 변환하는 과정을 보여주고,
변환된 그래프를 시각적으로 확인할 수 있도록 돕습니다.
""")
st.markdown("---")

st.header("1. 이차함수 계수 입력 (일반형)")
st.write("변환하고 싶은 이차함수의 계수 $a, b, c$를 입력해 주세요.")

# 계수 입력 위젯
# a는 0이 아니어야 하므로 min_value를 조정하고 초기값을 설정
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input('계수 $a$ (단, $a \\ne 0$)', min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
with col2:
    b = st.number_input('계수 $b$', value=2.0, step=0.1)
with col3:
    c = st.number_input('계수 $c$', value=3.0, step=0.1)

# a가 0인 경우 경고
if a == 0:
    st.error("⚠️ $a$는 0이 될 수 없습니다. $a=0$이면 이차함수가 아닙니다.")
    st.stop() # a가 0이면 더 이상 진행하지 않음

st.subheader(f"입력된 일반형: $y = {a}x^2 + {b}x + {c}$")
st.markdown("---")

st.header("2. 일반형 → 표준형 변환 과정")

st.markdown(f"주어진 이차함수: $\\mathbf{{y = {a}x^2 + {b}x + {c}}}$")

st.write("1. $x^2$의 계수 $a$로 묶습니다.")
st.markdown(f"$\\quad y = {a}(x^2 + \\frac{{{b}}}{{{a}}}x) + {c}$")

# 완전제곱식 만들기 위한 항 계산
half_b_over_a = (b / a) / 2
square_half_b_over_a = half_b_over_a**2

st.write("2. 괄호 안을 완전제곱식으로 만들기 위해 $(\\frac{{b}}{{2a}})^2$를 더하고 뺍니다.")
st.markdown(f"$\\quad y = {a}(x^2 + \\frac{{{b}}}{{{a}}}x + (\\frac{{{b}}}{{2{a}}})^2 - (\\frac{{{b}}}{{2{a}}})^2) + {c}$")
st.markdown(f"$\\quad y = {a}(x^2 + {b/a:.2f}x + {square_half_b_over_a:.2f} - {square_half_b_over_a:.2f}) + {c}$")


st.write("3. 완전제곱식 부분을 묶고, 나머지 항을 괄호 밖으로 꺼냅니다.")
st.markdown(f"$\\quad y = {a}((x + \\frac{{{b}}}{{2{a}}})^2 - (\\frac{{{b}}}{{2{a}}})^2) + {c}$")
st.markdown(f"$\\quad y = {a}(x + {half_b_over_a:.2f})^2 - {a} \\times {square_half_b_over_a:.2f} + {c}$")

# p, q 값 계산
p = -half_b_over_a
q = a * (-square_half_b_over_a) + c
q_simplified = (4*a*c - b**2) / (4*a) # 판별식과 유사한 형태 (꼭짓점의 y좌표)

st.write("4. 계산하여 최종 표준형을 얻습니다.")
st.markdown(f"$\\quad y = {a}(x - ({p:.2f}))^2 + ({q_simplified:.2f})$")
st.success(f"**변환된 표준형:** $\\mathbf{{y = {a}(x - {p:.2f})^2 + {q_simplified:.2f}}}$")

# 꼭짓점과 축의 방정식
st.subheader("표준형으로부터 알 수 있는 정보:")
st.markdown(f"- **꼭짓점 (p, q):** $({p:.2f}, {q_simplified:.2f})$")
st.markdown(f"- **축의 방정식:** $x = {p:.2f}$")
st.markdown("---")


st.header("3. 그래프 시각화")
st.write("일반형과 표준형은 같은 그래프를 나타냅니다. 직접 확인해 보세요.")

# x 범위 설정
x_vals = np.linspace(p - 5, p + 5, 400) # 꼭짓점을 중심으로 x 범위 설정
if a == 0: # a가 0인 경우 대비 (위에서 막았지만 혹시 모를 상황)
    y_general = np.zeros_like(x_vals) + c
    y_standard = np.zeros_like(x_vals) + c
else:
    # 일반형 계산
    y_general = a * x_vals**2 + b * x_vals + c
    # 표준형 계산
    y_standard = a * (x_vals - p)**2 + q_simplified

# Matplotlib을 사용하여 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x_vals, y_general, label=f'일반형 $y={a}x^2+{b}x+{c}$', color='blue', linestyle='-')
ax.plot(x_vals, y_standard, label=f'표준형 $y={a}(x-{p:.2f})^2+{q_simplified:.2f}$', color='red', linestyle='--', alpha=0.7)

# 꼭짓점 표시
ax.plot(p, q_simplified, 'o', color='green', markersize=8, label=f'꼭짓점 $({p:.2f}, {q_simplified:.2f})$')
ax.text(p, q_simplified, f'  ({p:.2f}, {q_simplified:.2f})', verticalalignment='bottom', horizontalalignment='left', color='green')


ax.axhline(0, color='gray', linewidth=0.7, linestyle='--') # x축
ax.axvline(0, color='gray', linewidth=0.7, linestyle='--') # y축
ax.axvline(p, color='purple', linewidth=0.7, linestyle=':', label=f'축 $x={p:.2f}$') # 축의 방정식

ax.set_title('일반형과 표준형 그래프 비교')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend()
ax.set_ylim(min(y_general.min(), y_standard.min()) - 2, max(y_general.max(), y_standard.max()) + 2) # y축 범위 동적 조절
ax.set_aspect('equal', adjustable='box') # x, y 축 스케일 동일하게

# 그래프를 Streamlit에 표시
st.pyplot(fig)

st.markdown("---")
st.info("**팁:** $a, b, c$ 값을 변경해 보면서 변환 과정과 그래프의 변화를 관찰해 보세요!")
