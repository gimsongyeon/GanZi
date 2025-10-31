import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# --- 페이지 설정 ---
st.set_page_config(layout="centered", page_title="유리함수 일반형↔표준형 변환 학습")

st.title("🔄 유리함수 일반형 → 표준형 변환 학습기")

# ⭐️⭐️⭐️ 오류 수정 1: LaTeX 제목 수식 표기 오류 수정 ⭐️⭐️⭐️
st.latex(r"y = \frac{ax+b}{cx+d} \quad \longrightarrow \quad y = \frac{k}{x-p} + q")
# 이전 오류: \frac 대신 \rac 등의 오타, 불필요한 [] 기호 등

st.markdown("---")

## 1. 유리함수 계수 입력 (일반형)
st.header("1. 유리함수 계수 입력 (일반형)")
st.write("변환하고 싶은 유리함수의 계수 $a, b, c, d$를 입력해 주세요.")

# 계수 입력 위젯
col1, col2, col3, col4 = st.columns(4)
with col1:
    a = st.number_input('계수 $a$', value=2, step=1)
with col2:
    b = st.number_input('계수 $b$', value=-3, step=1)
with col3:
    c = st.number_input('계수 $c$ (단, $c \\ne 0$)', value=1, step=1)
with col4:
    d = st.number_input('계수 $d$', value=-1, step=1)

# 오류 처리 및 필수 변수 계산
if c == 0:
    st.error("⚠️ $c$는 0이 될 수 없습니다. $c=0$이면 유리함수가 아닌 직선입니다.")
    st.stop()

# --- 표준형 (p, q, k) 계산 ---
q = a / c
numerator_k_prime = b - a * d / c
k = numerator_k_prime / c
p = -d / c

if abs(a * d - b * c) < 1e-6:
    st.warning(f"⚠️ $ad - bc \\approx 0$ 이므로 이 함수는 상수 함수 $y = {q:.2f}$ 에 가깝습니다. 계수를 변경해 주세요.")

# LaTeX 출력에 사용할 포맷팅된 변수 정의
q_fmt = f"{q:.2f}"
num_k_prime_fmt = f"{numerator_k_prime:.2f}"
p_fmt = f"{p:.2f}"
k_fmt = f"{k:.2f}"
d_div_c = d / c

# ⭐️⭐️⭐️ 오류 수정 2: 입력된 일반형 표기 (format_term 함수 로직 개선) ⭐️⭐️⭐️
def format_term_improved(coeff, variable='x', is_numerator_first=False, is_denominator_first=False):
    if coeff == 0:
        return "" # 계수가 0이면 해당 항은 표시하지 않음

    abs_coeff = abs(coeff)
    
    # 첫 항의 부호 처리: 양수일 때 '+'를 붙이지 않음
    if is_numerator_first or is_denominator_first:
        sign = "" if coeff > 0 else "-"
    else: # 두 번째 항부터는 부호를 명확히 표시
        sign = "+" if coeff > 0 else "-"

    if abs_coeff == 1 and variable == 'x': # 1x는 x로 표시
        return f"{sign}{variable}"
    elif variable == 'x': # x항
        return f"{sign}{abs_coeff}{variable}"
    else: # 상수항
        return f"{sign}{abs_coeff}"

# 입력된 일반형 분자와 분모를 정확하게 표기
num_term_ax = format_term_improved(a, 'x', is_numerator_first=True)
num_term_b = format_term_improved(b, '', is_numerator_first=False) # 분자 상수항
formatted_numerator = f"{num_term_ax}{num_term_b}"
if not formatted_numerator: formatted_numerator = "0" # 분자가 0인 경우 대비 (e.g. y = 0/(cx+d))

den_term_cx = format_term_improved(c, 'x', is_denominator_first=True)
den_term_d = format_term_improved(d, '', is_denominator_first=False) # 분모 상수항
formatted_denominator = f"{den_term_cx}{den_term_d}"
if not formatted_denominator: formatted_denominator = "0" # 분모가 0인 경우 대비 (stop() 처리되어 있지만 안전하게)

st.subheader(f"입력된 일반형: $\\mathbf{{y = \\frac{{{formatted_numerator}}}{{{formatted_denominator}}}}}$")
st.markdown("---")

## 2. 일반형 → 표준형 변환 과정
st.header("2. 일반형 → 표준형 변환 과정")

st.write("1. **다항식의 나눗셈**을 이용하여 분자를 분모 $({c}x + {d})$에 대한 식으로 나타냅니다.")
st.latex(f"y = \\frac{{{a}x + {b}}}{{{c}x + {d}}} = \\frac{{ {q_fmt} ({c}x + {d}) + ({num_k_prime_fmt}) }}{{{c}x + {d}}}")

st.write("2. 분리하여 **$q$ 값(수평 점근선)**을 찾습니다.")
st.latex(f"y = \\frac{{{q_fmt} ({c}x + {d})}}{{{c}x + {d}}} + \\frac{{{num_k_prime_fmt}}}{{{c}x + {d}}} = {q_fmt} + \\frac{{{num_k_prime_fmt}}}{{{c}x + {d}}}")

st.write("3. 분모를 $c$로 묶어 **$k$와 $p$ 값**을 찾습니다.")
st.latex(f"y = {q_fmt} + \\frac{{\\frac{{{num_k_prime_fmt}}}{{{c}}}}}{(x - ({p_fmt}))}")

st.success(f"**변환된 표준형:** $\\mathbf{{y = \\frac{{{k_fmt}}}{{x - ({p_fmt})}} + {q_fmt}}}$")

# 점근선 및 대칭 중심
st.subheader("표준형으로부터 알 수 있는 정보:")
st.markdown(f"- **점근선의 교점 (대칭의 중심):** $({p_fmt}, {q_fmt})$")
st.markdown(f"- **수직 점근선:** $x = {p_fmt}$")
st.markdown(f"- **수평 점근선:** $y = {q_fmt}$")
st.markdown("---")

## 3. 그래프 시각화
st.header("3. 그래프 시각화")

# --- 그래프 생성 및 표시 ---
fig, ax = plt.subplots(figsize=(10, 6))

x_p = p # 수직 점근선 x = p
x_q = q # 수평 점근선 y = q

# 그래프를 그릴 x 값: 점근선 근처를 제외
x1 = np.linspace(x_p - 5, x_p - 0.05, 100)
x2 = np.linspace(x_p + 0.05, x_p + 5, 100)
x_vals = np.concatenate((x1, x2))

# y 값 계산
y_vals = k / (x_vals - x_p) + x_q

# 그래프 그리기
ax.plot(x_vals, y_vals, label='유리함수 그래프', color='blue')

# 점근선 표시
ax.axvline(x_p, color='red', linestyle='--', label=f'수직 점근선 $x={x_p:.2f}$')
ax.axhline(x_q, color='green', linestyle='--', label=f'수평 점근선 $y={x_q:.2f}$')

# 점근선의 교점 표시
ax.plot(x_p, x_q, 'o', color='purple', markersize=6, label=f'중심 $({x_p:.2f}, {x_q:.2f})$')

# 축 설정 및 보조선
ax.set_title(f'유리함수 그래프 (점근선 $x={x_p:.2f}$, $y={x_q:.2f}$)')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend()
ax.set_xlim(x_p - 5, x_p + 5)
ax.set_ylim(x_q - 5, x_q + 5)

# 그래프를 Streamlit에 표시
st.pyplot(fig)


st.markdown("---")
st.info("**팁:** $a, b, c, d$ 값을 변경해 보면서 변환 과정과 점근선의 변화를 관찰해 보세요!")
