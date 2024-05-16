from flask import Flask, Blueprint, render_template
import pandas as pd
import requests
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc("font", family="Malgun Gothic")

bp = Blueprint("graph", __name__, url_prefix="/graph")
df = pd.read_csv("pybo\static\others\서울시 코로나19 확진자전수감시 발생동향.csv", encoding="cp949")
df1 = df.copy()

df1["서울시 기준일"]= df1["서울시 기준일"].str.replace(".", "-")
df1["서울시 기준일"] = df1["서울시 기준일"].str.split("-").str[:3].str.join("-")

df1["전국 기준일"]= df1["전국 기준일"].str.replace(".", "-")
df1["전국 기준일"] = df1["전국 기준일"].str.split("-").str[:3].str.join("-")

# 앞 연도 수가 2자리인 경우에만 20을 추가하겠다는 정규 표현식 패턴을 추가함.
df1["전국 기준일"]= df1["전국 기준일"].str.replace(r"(?<!\d)20-", "2020-", regex=True)

df1["서울기준일_dt"] = pd.to_datetime(df1["서울시 기준일"])
df1["전국기준일_dt"] = pd.to_datetime(df1["전국 기준일"])

df1["서울시기준연도"]= df1["서울기준일_dt"].dt.year
df1["서울시기준월"]= df1["서울기준일_dt"].dt.month
df1["전국기준연도"]= df1["전국기준일_dt"].dt.year
df1["전국기준월"]= df1["전국기준일_dt"].dt.month

df1 = df1.fillna(0)

df_2023 = df1.loc[df1["서울시기준연도"]== 2023, :]
df_2022 = df1.loc[df1["서울시기준연도"]== 2022, :]
df_2021 = df1.loc[df1["서울시기준연도"]== 2021, :]
df_2020 = df1.loc[df1["서울시기준연도"]== 2020, :]


@bp.route("/worldmap")
def worldmap():
    return render_template("covid19/covid19_map.html")


@bp.route("/covid19analysis")
def covid19_analysis():
    global df1, df_2020, df_2021, df_2022, df_2023

    바뀌= pd.pivot_table(data=바뀌, index=["서울시기준바뀌"], values=["서울시 확진자","서울시 퇴원", "서울시 사망"])

    바뀌.plot(kind="line",y=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("서울시 2023년 확진, 퇴원, 사망 현황")
    photo1 = "pybo/static/upload/line_plot.png"
    plt.savefig(photo1)
    line = photo1[11:]

    plt.subplot(1, 1, 1)
    df_year.plot(kind="bar", y=["서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("완치자와 사망자 비교표")
    photo2 = "pybo/static/upload/bar_plot.png"
    plt.savefig(photo2)
    bar = photo2[11:]

    ############################ 2020년
    
    df2020= pd.pivot_table(data=df_2020, index=["서울시기준월"], values=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    df2020.plot(kind="line",y=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("서울시 월 단위 확진, 퇴원, 사망 현황 [2020년]")
    photo20 = "pybo/static/upload/line_plot20.png"
    plt.savefig(photo20)
    line20 = photo20[11:]

    plt.subplot(1, 1, 1)
    df2020.plot(kind="bar", y=["서울시 사망"])
    plt.ylabel("Count")
    plt.title("사망자 집계 비교표")
    photo20m = "pybo/static/upload/bar_plot20.png"
    plt.savefig(photo20m)
    bar20 = photo20m[11:]

    ############################ 2021년

    df2021= pd.pivot_table(data=df_2021, index=["서울시기준월"], values=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    df2021.plot(kind="line",y=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("서울시 월 단위 확진, 퇴원, 사망 현황 [2021년]")
    photo21 = "pybo/static/upload/line_plot21.png"
    plt.savefig(photo21)
    line21 = photo21[11:]

    plt.subplot(1, 1, 1)
    df2021.plot(kind="bar", y=["서울시 사망"])
    plt.ylabel("Count")
    plt.title("사망자 집계 비교표")
    photo21m = "pybo/static/upload/bar_plot21.png"
    plt.savefig(photo21m)
    bar21 = photo21m[11:]

        ############################ 2022년
    
    df2022= pd.pivot_table(data=df_2022, index=["서울시기준월"], values=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    df2022.plot(kind="line",y=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("서울시 월 단위 확진, 퇴원, 사망 현황 [2022년]")
    photo22 = "pybo/static/upload/line_plot22.png"
    plt.savefig(photo22)
    line22 = photo22[11:]

    plt.subplot(1, 1, 1)
    df2022.plot(kind="bar", y=["서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("완치자와 사망 비교표")
    photo22m = "pybo/static/upload/bar_plot22.png"
    plt.savefig(photo22m)
    bar22 = photo22m[11:]

    plt.subplot(1, 1, 1)
    df2022.plot(kind="bar", y=["서울시 사망"])
    plt.ylabel("Count")
    plt.title("사망자 집계표")
    photo222m = "pybo/static/upload/bar_plot222.png"
    plt.savefig(photo222m)
    bar222 = photo222m[11:]

        ############################ 2023년
    
    df2023= pd.pivot_table(data=df_2023, index=["서울시기준월"], values=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    df2023.plot(kind="line",y=["서울시 확진자","서울시 퇴원", "서울시 사망"])
    plt.ylabel("Count")
    plt.title("서울시 월 단위 확진, 퇴원, 사망 현황 [2023년]")
    photo23 = "pybo/static/upload/line_plot23.png"
    plt.savefig(photo23)
    line23 = photo23[11:]

    plt.subplot(1,1,1)
    df2023.plot(kind="bar", y=["서울시 퇴원","서울시 사망"])
    plt.ylabel("Count")
    plt.title("완치자와 사망자 비교표")
    photo23m = "pybo/static/upload/bar_plot23.png"
    plt.savefig(photo23m)
    bar23 = photo23m[11:]

    plt.subplot(1, 1, 1)
    df2023.plot(kind="bar", y=["서울시 퇴원"])
    plt.ylabel("Count")
    plt.title("완치자 집계표")
    photo233m = "pybo/static/upload/bar_plot233.png"
    plt.savefig(photo233m)
    bar233 = photo233m[11:]


    return render_template("/test/analysis_covid19.html", line_plot=line, bar_plot=bar,
                           line_plot20=line20, bar_plot20=bar20, line_plot21=line21, bar_plot21=bar21,
                           line_plot22=line22, bar_plot22=bar22, bar_plot222=bar222,
                           line_plot23=line23, bar_plot23=bar23, bar_plot233=bar233)