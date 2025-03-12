import streamlit as st

st.title("주식정보조회")

## Sidebar Header
st.sidebar.header("User Input")

## Sidebar User Input

# ticker_type: 라디오 버튼
st.sidebar.radio("Ticker Type Selector",("stock_ticker","stock_code")) #stock_ticker, stock_code

# TODO: st.sidebar.radio 도 변수에 저장하기
#   st.sidebar.radio에서 선택된 게 그대로 저장됨
#   예) stock_tcker 를 선택하면(페이지에서) 변수에 "stock_ticker"가 저장됨


# TODO: 저장된 ticker_type에 따라서 다른 text_ipnut 보여주기
##
# if ticker_type=="stock_ticker":
#   ticker = st.sidebar.text_input("Ticker", "AAPL")
# else ...
##

stock_ticker = st.sidebar.text_input("Ticker","AAPL") # 주식 코드 또는 ticker(이름)을 입력할 곳
stock_start_date = st.sidebar.date_input("Start Date") # 조회 시작 날짜 입력기
stock_end_date = st.sidebar.date_input("End Date") # 조회 끝 날짜 입력기

## 본 페이지 내용

# TODO: 저장된 ticker type에 따라서 "Ticker"를 보여줄지, "Code"를 보여줄지 결정해서 st.write
st.write(f"Stock ticker: {stock_ticker}")
st.write(f"stock start date: {stock_start_date}")
st.write(f"stock end date: {stock_end_date}")


## General Assignments
# Commit and Push this to Git remote repository