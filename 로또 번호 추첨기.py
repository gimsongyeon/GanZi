# lotto_app.py

import streamlit as st
import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

def compare_numbers(generated, winning):
    # generated는 리스트, winning는 리스트
    matched = set(generated) & set(winning)
    return len(matched), sorted(matched)

def main():
    st.title("로또 번호 추천기 & 당첨번호 비교")
    st.write("1 ~ 45 중에서 6개의 숫자를 추천합니다.")
    
    # 최근 당첨 번호 입력
    st.sidebar.header("최근 당첨 번호 입력")
    winning_input = st.sidebar.text_input("당첨 번호를 쉼표(,)로 구분해서 입력하세요 (예: 3,15,27,33,34,36)", "3,15,27,33,34,36")
    try:
        winning_numbers = sorted([int(x.strip()) for x in winning_input.split(",") if x.strip()])
        if len(winning_numbers) != 6 or any(n<1 or n>45 for n in winning_numbers):
            st.sidebar.error("당첨 번호는 정확히 6개, 1~45 범위여야 합니다.")
            winning_numbers = None
    except:
        st.sidebar.error("입력 형식이 잘못되었습니다.")
        winning_numbers = None
    
    # 생성할 세트 수 선택
    num_sets = st.number_input("생성할 세트 수", min_value=1, max_value=100, value=1, step=1)
    
    if st.button("추천 번호 생성"):
        sets = []
        for i in range(num_sets):
            nums = generate_lotto_numbers()
            sets.append(nums)
        st.write(f"🎉 생성된 {num_sets}세트 번호:")
        for idx, s in enumerate(sets, start=1):
            st.write(f"세트 {idx}: {s}")
        
        if winning_numbers:
            st.write("---")
            st.write(f"최근 당첨 번호: {winning_numbers}")
            st.write("✅ 맞춘 개수 및 번호:")
            for idx, s in enumerate(sets, start=1):
                count, matched = compare_numbers(s, winning_numbers)
                st.write(f"세트 {idx}: 맞춘 개수 = {count}, 맞춘 번호 = {matched}")
        else:
            st.write("※ 유효한 당첨 번호가 입력되지 않아 비교하지 않습니다.")
    
    st.write("---")
    st.write("※ 참고: 이 앱은 재미용입니다. 실제 로또 구매 및 당첨을 보장하지 않습니다.")

if __name__ == "__main__":
    main()
