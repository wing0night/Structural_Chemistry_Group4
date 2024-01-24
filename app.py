import streamlit as st

from Introduction import page as Introduction
from part1 import page as part1
from part2 import page as part2
from part3 import page as part3
from part4 import page as part4
from part5 import page as part5

st.sidebar.title("Nevigation")
page = st.sidebar.radio("Go to", ["Introduction", "Part1 对称元素与对称操作", "Part2 群的基本概念&对称操作的乘积", "Part3 几种常见的点群整理", "Part4 例题分析", "Part5 点群应用"])

if page == "Introduction":
    Introduction()
if page == "Part1 对称元素与对称操作":
    part1()
if page == "Part2 群的基本概念&对称操作的乘积":
    part2()
if page == "Part3 几种常见的点群整理":
    part3()
if page == "Part4 例题分析":
    part4()
if page == "Part5 点群应用":
    part5()

