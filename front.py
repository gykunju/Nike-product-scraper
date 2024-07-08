import streamlit as st
import mongodb

st.title("Session Counter")

def set_data():
    pass

side1, side2 = st.columns((2,1))
with side1:
    st.subheader("Products")

with side2:
    st.selectbox("Filter", ['Men', 'Women', 'kids'], on_change='', args=())

left, right = st.columns(2)
count = 0
for key in mongodb.get_accessories():
    if count % 2:
        with left:
            with st.container():
                st.write("---")
                left_col_count = 0
                left_col1, left_col2 = st.columns(2)
                for k, val in key.items():
                    if k != "_id" and k != "link":
                        if left_col_count % 2 == 0:
                            with left_col1:
                                st.write(f" {val}")
                                left_col_count +=1
                        else:
                            with left_col2:
                                if k == 'category':
                                    st.write(' {val}')
                                    left_col_count += 1
                                    continue
                                st.write(f" {val}")
                                left_col_count +=1
                    if k == 'link':
                        link = val
                        st.button("Go to site", key=f"button_{count}")
    else:
        with right:
            with st.container():
                st.write("---")
                col1, col2 = st.columns(2)
                col_count = 0
                for k, val in key.items():
                    if k != "_id" and k != "link":
                        if col_count % 2 == 0:
                            with col1:
                                st.write(f" {val}")
                                col_count +=1
                        else:
                            with col2:
                                st.write(f" {val}")
                                col_count +=1
                    if k == 'link':
                        link = val
                        st.button("Go to site", key=f"button_{count}")
    st.write("---")
    count += 1