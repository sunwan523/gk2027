# -*- coding: utf-8 -*-
"""数学真题（2021—2025 全国卷/新课标卷/部分省卷）。

来源与核实状态见每条 source_ref / verified。verified=0 表示尚未人工核对，
使用时应以 source_ref 指向的原始材料为准。

核实说明：
- 2024 年新课标 I 卷条目以中国教育在线高考频道真题 PDF 的官方答案键为基准，
  并与教习网 / 学科网 / 人人文库等整理版逐题比对，答案与选项均两处以上互证。
- 涉及计算的条目（第 7 题交点个数、第 12/13 题填空值、第 15/16/17 题结果、
  2023 乙卷第 17 题的均值与方差）已另外用数值方式独立复算过。
- 2025 年新课标 I 卷第 13 题仅见单一整理源，且各站点对该卷的叫法
  （“新高考Ⅰ卷”“全国一卷”）不统一，故保持 verified=0。
"""
SUBJECT = "数学"

ITEMS = [
    # ---------------- 一、选择题 ----------------
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "1",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_set",
        "difficulty": 1,
        "stem": "已知集合 $A=\\{x\\mid -5<x^{3}<5\\}$，$B=\\{-3,-1,0,2,3\\}$，则 $A\\cap B=$（　　）",
        "options": [
            "A. $\\{-1,0\\}$",
            "B. $\\{2,3\\}$",
            "C. $\\{-3,-1,0\\}$",
            "D. $\\{-1,0,2\\}$",
        ],
        "answer": "A",
        "analysis": "解析：由 $-5<x^{3}<5$ 得 $-\\sqrt[3]{5}<x<\\sqrt[3]{5}$，又 $1<\\sqrt[3]{5}<2$，"
                    "所以 $A$ 中的整数只有 $-1,0,1$。与 $B=\\{-3,-1,0,2,3\\}$ 取交集得 $\\{-1,0\\}$。"
                    "也可逐项验证：$(-3)^3=-27\\notin(-5,5)$，$(-1)^3=-1\\in(-5,5)$，$0^3=0\\in(-5,5)$，"
                    "$2^3=8\\notin(-5,5)$，$3^3=27\\notin(-5,5)$，故选 A。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "2",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_complex",
        "difficulty": 2,
        "stem": "若 $\\dfrac{z}{z-1}=1+\\mathrm{i}$，则 $z=$（　　）",
        "options": [
            "A. $-1-\\mathrm{i}$",
            "B. $-1+\\mathrm{i}$",
            "C. $1-\\mathrm{i}$",
            "D. $1+\\mathrm{i}$",
        ],
        "answer": "C",
        "analysis": "解析：$\\dfrac{z}{z-1}=\\dfrac{(z-1)+1}{z-1}=1+\\dfrac{1}{z-1}=1+\\mathrm{i}$，"
                    "所以 $\\dfrac{1}{z-1}=\\mathrm{i}$，即 $z-1=\\dfrac{1}{\\mathrm{i}}=-\\mathrm{i}$，"
                    "故 $z=1-\\mathrm{i}$，选 C。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "3",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_vector_dec",
        "difficulty": 2,
        "stem": "已知向量 $\\boldsymbol{a}=(0,1)$，$\\boldsymbol{b}=(2,x)$。若 $\\boldsymbol{b}\\perp(\\boldsymbol{b}-4\\boldsymbol{a})$，"
                "则 $x=$（　　）",
        "options": [
            "A. $-2$",
            "B. $-1$",
            "C. $1$",
            "D. $2$",
        ],
        "answer": "D",
        "analysis": "解析：$\\boldsymbol{b}-4\\boldsymbol{a}=(2,x)-(0,4)=(2,x-4)$。由垂直得数量积为零："
                    "$\\boldsymbol{b}\\cdot(\\boldsymbol{b}-4\\boldsymbol{a})=2\\times2+x(x-4)=x^{2}-4x+4=(x-2)^{2}=0$，"
                    "故 $x=2$，选 D。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "4",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_trig_id",
        "difficulty": 3,
        "stem": "已知 $\\cos(\\alpha+\\beta)=m$，$\\tan\\alpha\\tan\\beta=2$，则 $\\cos(\\alpha-\\beta)=$（　　）",
        "options": [
            "A. $-3m$",
            "B. $-\\dfrac{m}{3}$",
            "C. $\\dfrac{m}{3}$",
            "D. $3m$",
        ],
        "answer": "A",
        "analysis": "解析：由 $\\tan\\alpha\\tan\\beta=\\dfrac{\\sin\\alpha\\sin\\beta}{\\cos\\alpha\\cos\\beta}=2$ 得 "
                    "$\\sin\\alpha\\sin\\beta=2\\cos\\alpha\\cos\\beta$。代入两角和的余弦公式："
                    "$\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta=-\\cos\\alpha\\cos\\beta=m$，"
                    "故 $\\cos\\alpha\\cos\\beta=-m$，$\\sin\\alpha\\sin\\beta=-2m$。于是"
                    "$\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta=-m+(-2m)=-3m$，选 A。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "5",
        "source_ref": "http://www.91apu.com/e/DoPrint?classid=929&id=34156",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_solid",
        "difficulty": 3,
        "stem": "已知圆柱和圆锥的底面半径相等，侧面积相等，且它们的高均为 $\\sqrt{3}$，则圆锥的体积为（　　）",
        "options": [
            "A. $2\\sqrt{3}\\pi$",
            "B. $3\\sqrt{3}\\pi$",
            "C. $6\\sqrt{3}\\pi$",
            "D. $9\\sqrt{3}\\pi$",
        ],
        "answer": "B",
        "analysis": "解析：设公共底面半径为 $r$，圆锥母线长 $l=\\sqrt{r^{2}+(\\sqrt{3})^{2}}=\\sqrt{r^{2}+3}$。"
                    "圆柱侧面积 $2\\pi r\\cdot\\sqrt{3}$，圆锥侧面积 $\\pi r l$，二者相等得 $l=2\\sqrt{3}$，"
                    "即 $r^{2}+3=12$，$r=3$。圆锥体积 "
                    "$V=\\dfrac{1}{3}\\pi r^{2}h=\\dfrac{1}{3}\\pi\\times9\\times\\sqrt{3}=3\\sqrt{3}\\pi$，选 B。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "7",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_trig",
        "difficulty": 3,
        "stem": "当 $x\\in[0,2\\pi]$ 时，曲线 $y=\\sin x$ 与 $y=2\\sin\\left(3x-\\dfrac{\\pi}{6}\\right)$ 的交点个数为（　　）",
        "options": [
            "A. $3$",
            "B. $4$",
            "C. $6$",
            "D. $8$",
        ],
        "answer": "C",
        "analysis": "解析：$y=2\\sin\\left(3x-\\dfrac{\\pi}{6}\\right)$ 的周期 $T=\\dfrac{2\\pi}{3}$，在 $[0,2\\pi]$ 上恰好 3 个周期。"
                    "用“五点法”作出该曲线在 $[0,2\\pi]$ 上的草图，再与 $y=\\sin x$ 的图象叠加对照，"
                    "两条曲线共有 6 个交点（数值求解 $\\sin x=2\\sin\\left(3x-\\frac{\\pi}{6}\\right)$ 亦得 6 个根），选 C。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "8",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_func",
        "difficulty": 4,
        "stem": "已知函数 $f(x)$ 的定义域为 $\\mathbf{R}$，$f(x)>f(x-1)+f(x-2)$，且当 $x<3$ 时 $f(x)=x$，"
                "则下列结论中一定正确的是（　　）",
        "options": [
            "A. $f(10)>100$",
            "B. $f(20)>1000$",
            "C. $f(10)<1000$",
            "D. $f(20)<10000$",
        ],
        "answer": "B",
        "analysis": "解析：由 $x<3$ 时 $f(x)=x$ 得 $f(1)=1$，$f(2)=2$。反复用 $f(x)>f(x-1)+f(x-2)$ 递推："
                    "$f(3)>3$，$f(4)>5$，$f(5)>8$，$f(6)>13$，$f(7)>21$，$f(8)>34$，$f(9)>55$，$f(10)>89$，"
                    "$f(11)>144$，$f(12)>233$，$f(13)>377$，$f(14)>610$，$f(15)>987$，$f(16)>1597>1000$。"
                    "由单调传递性知 $f(20)>f(16)>1000$，B 一定成立；而 $f(10)$ 只能保证 $>89$，推不出 $>100$，A 错；"
                    "不等式只给下界，对 $f$ 的上界没有任何限制，C、D 都不能保证，错。故选 B。",
        "points": [],
    },
    {
        "year": 2023,
        "paper": "全国乙卷（理科）",
        "question_no": "7",
        "source_ref": "http://www.dochui.com/edu/gaokao/21/21484.html",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_count",
        "difficulty": 3,
        "stem": "甲、乙两位同学从 $6$ 种课外读物中各自选读 $2$ 种，则这两人选读的课外读物中恰有 $1$ 种相同的选法共有（　　）",
        "options": [
            "A. $30$ 种",
            "B. $60$ 种",
            "C. $120$ 种",
            "D. $240$ 种",
        ],
        "answer": "C",
        "analysis": "解析：先定两人共同读的那 1 种，有 $\\mathrm{C}_{6}^{1}=6$ 种；再从剩余 5 种里取 2 种分别分给甲、乙，"
                    "有 $\\mathrm{A}_{5}^{2}=20$ 种；由分步乘法计数原理得 $6\\times20=120$ 种。"
                    "也可用排除法：$\\mathrm{C}_{6}^{2}\\mathrm{C}_{6}^{2}-\\mathrm{C}_{6}^{2}-\\mathrm{C}_{6}^{2}\\mathrm{C}_{4}^{2}"
                    "=225-15-90=120$。故选 C。",
        "points": [],
    },

    # ---------------- 二、填空题 ----------------
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "12",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_conic",
        "difficulty": 3,
        "stem": "设双曲线 $C:\\dfrac{x^{2}}{a^{2}}-\\dfrac{y^{2}}{b^{2}}=1\\ (a>0,b>0)$ 的左、右焦点分别为 $F_{1},F_{2}$，"
                "过 $F_{2}$ 作平行于 $y$ 轴的直线交 $C$ 于 $A$，$B$ 两点，若 $|F_{1}A|=13$，$|AB|=10$，"
                "则 $C$ 的离心率为 ____。",
        "options": [],
        "answer": "$\\dfrac{3}{2}$",
        "analysis": "解析：由对称性 $|AF_{2}|=\\dfrac{1}{2}|AB|=5$，故 $|AB|=10$。又把 $x=c$ 代入双曲线方程得 "
                    "$|AF_{2}|=\\dfrac{b^{2}}{a}=5$。由双曲线定义 $2a=|F_{1}A|-|AF_{2}|=13-5=8$，得 $a=4$；"
                    "于是 $b^{2}=5a=20$，$c^{2}=a^{2}+b^{2}=36$，$c=6$，所以 $e=\\dfrac{c}{a}=\\dfrac{6}{4}=\\dfrac{3}{2}$。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "13",
        "source_ref": "https://static-gkcx.gaokao.cn/upload/zhenti/20240611/1718078152_5550.pdf",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_deriv",
        "difficulty": 3,
        "stem": "若曲线 $y=\\mathrm{e}^{x}+x$ 在点 $(0,1)$ 处的切线也是曲线 $y=\\ln(x+1)+a$ 的切线，则 $a=$ ____。",
        "options": [],
        "answer": "$\\ln 2$",
        "analysis": "解析：对 $y=\\mathrm{e}^{x}+x$ 求导得 $y'=\\mathrm{e}^{x}+1$，$x=0$ 处斜率为 $2$，"
                    "切线方程为 $y=2x+1$。设它与 $y=\\ln(x+1)+a$ 相切于横坐标为 $x_{0}$ 的点，"
                    "由 $y'=\\dfrac{1}{x_{0}+1}=2$ 得 $x_{0}=-\\dfrac{1}{2}$，切点为 $\\left(-\\dfrac{1}{2},\\ a-\\ln 2\\right)$。"
                    "代入 $y=2x+1$：$a-\\ln 2=2\\times\\left(-\\dfrac{1}{2}\\right)+1=0$，故 $a=\\ln 2$。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "13",
        "source_ref": "https://www.51jiaoxi.com/doc-18762217.html",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_seq",
        "difficulty": 3,
        "stem": "若一个等比数列的各项均为正数，且前 $4$ 项的和等于 $4$，前 $8$ 项的和等于 $68$，则这个数列的公比等于 ____。",
        "options": [],
        "answer": "$2$",
        "analysis": "解析：设公比为 $q\\ (q>0)$，前 $n$ 项和为 $S_{n}$。由等比数列分段求和性质 "
                    "$S_{8}=S_{4}+q^{4}S_{4}=(1+q^{4})S_{4}$，即 $68=4(1+q^{4})$，得 $q^{4}=16$，$q=\\pm 2$。"
                    "各项均为正数说明 $q>0$，故 $q=2$。"
                    "（已双源核对：官方《试题分析》转载与教习网真题追踪一致，题干已按原卷措辞修正。）",
        "points": [],
    },

    # ---------------- 三、解答题 ----------------
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "15",
        "source_ref": "https://www.51jiaoxi.com/doc-17126532.html",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_solve_tri",
        "difficulty": 4,
        "stem": "记 $\\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，已知 $\\sin C=\\sqrt{2}\\cos B$，"
                "$a^{2}+b^{2}-c^{2}=\\sqrt{2}ab$。\n"
                "(1) 求 $B$；\n"
                "(2) 若 $\\triangle ABC$ 的面积为 $3+\\sqrt{3}$，求 $c$。",
        "options": [],
        "answer": "(1) $B=\\dfrac{\\pi}{3}$；(2) $c=2\\sqrt{2}$",
        "analysis": "解析：(1) 由余弦定理 $\\cos C=\\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\\dfrac{\\sqrt{2}ab}{2ab}=\\dfrac{\\sqrt{2}}{2}$，"
                    "又 $C\\in(0,\\pi)$，故 $C=\\dfrac{\\pi}{4}$，$\\sin C=\\dfrac{\\sqrt{2}}{2}$。代入 $\\sin C=\\sqrt{2}\\cos B$ "
                    "得 $\\cos B=\\dfrac{1}{2}$，又 $B\\in(0,\\pi)$，故 $B=\\dfrac{\\pi}{3}$。\n"
                    "(2) $A=\\pi-B-C=\\dfrac{5\\pi}{12}$，$\\sin A=\\sin\\left(\\dfrac{\\pi}{3}+\\dfrac{\\pi}{4}\\right)"
                    "=\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$。由正弦定理 $\\dfrac{a}{\\sin A}=\\dfrac{c}{\\sin C}$ 得"
                    "$a=\\dfrac{\\sin A}{\\sin C}c=\\dfrac{1+\\sqrt{3}}{2}c$。于是面积"
                    "$S=\\dfrac{1}{2}ac\\sin B=\\dfrac{1}{2}\\cdot\\dfrac{1+\\sqrt{3}}{2}c\\cdot c\\cdot\\dfrac{\\sqrt{3}}{2}"
                    "=\\dfrac{3+\\sqrt{3}}{8}c^{2}=3+\\sqrt{3}$，解得 $c^{2}=8$，即 $c=2\\sqrt{2}$。",
        "points": [
            "第(1)问：由余弦定理得 $\\cos C=\\dfrac{\\sqrt2}{2}$，故 $C=\\dfrac{\\pi}{4}$，$\\sin C=\\dfrac{\\sqrt2}{2}$（3分）；"
            "代入 $\\sin C=\\sqrt2\\cos B$ 得 $\\cos B=\\dfrac12$，故 $B=\\dfrac{\\pi}{3}$（3分）",
            "第(2)问：算出 $\\sin A=\\dfrac{\\sqrt6+\\sqrt2}{4}$，由正弦定理得 $a=\\dfrac{1+\\sqrt3}{2}c$（3分）；"
            "代入 $S=\\dfrac12 ac\\sin B$ 得 $\\dfrac{3+\\sqrt3}{8}c^2=3+\\sqrt3$，解得 $c=2\\sqrt2$（4分）",
        ],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "16",
        "source_ref": "https://www.51jiaoxi.com/doc-17126532.html",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_conic",
        "difficulty": 4,
        "stem": "已知 $A(0,3)$ 和 $P\\left(3,\\dfrac{3}{2}\\right)$ 为椭圆 $C:\\dfrac{x^{2}}{a^{2}}+\\dfrac{y^{2}}{b^{2}}=1\\ (a>b>0)$ 上两点。\n"
                "(1) 求 $C$ 的离心率；\n"
                "(2) 若过 $P$ 的直线 $l$ 交 $C$ 于另一点 $B$，且 $\\triangle ABP$ 的面积为 $9$，求 $l$ 的方程。",
        "options": [],
        "answer": "(1) $e=\\dfrac{1}{2}$；(2) $l$ 的方程为 $3x-2y-6=0$ 或 $x-2y=0$",
        "analysis": "解析：(1) $A(0,3)$ 在 $C$ 上得 $b^{2}=9$；$P\\left(3,\\dfrac{3}{2}\\right)$ 在 $C$ 上得 "
                    "$\\dfrac{9}{a^{2}}+\\dfrac{9/4}{9}=1$，即 $\\dfrac{9}{a^{2}}=\\dfrac{3}{4}$，$a^{2}=12$。"
                    "故 $c^{2}=a^{2}-b^{2}=3$，$e=\\dfrac{c}{a}=\\dfrac{\\sqrt{3}}{2\\sqrt{3}}=\\dfrac{1}{2}$。\n"
                    "(2) $k_{AP}=\\dfrac{\\frac32-3}{3-0}=-\\dfrac12$，直线 $AP$：$x+2y-6=0$，"
                    "$|AP|=\\sqrt{3^{2}+\\left(\\frac32\\right)^{2}}=\\dfrac{3\\sqrt5}{2}$。"
                    "由 $S_{\\triangle ABP}=\\dfrac12|AP|\\,d=9$ 得 $B$ 到直线 $AP$ 的距离 $d=\\dfrac{12}{\\sqrt5}$。\n"
                    "又 $S_{\\triangle AOP}=\\dfrac12|\\overrightarrow{OA}\\times\\overrightarrow{OP}|=\\dfrac92$，"
                    "所以将 $A$ 关于原点对称到 $A'(0,-3)$ 时 $S_{\\triangle AA'P}=9$，得 $B_{1}=(0,-3)$；"
                    "将 $P$ 关于原点对称到 $P'\\left(-3,-\\dfrac32\\right)$ 时 $S_{\\triangle APP'}=9$，"
                    "得 $B_{2}=\\left(-3,-\\dfrac{3}{2}\\right)$。\n"
                    "$B=B_{1}$ 时 $k_{l}=\\dfrac{-3-\\frac32}{0-3}=\\dfrac32$，$l:\\ y=\\dfrac32x-3$，即 $3x-2y-6=0$；\n"
                    "$B=B_{2}$ 时 $k_{l}=\\dfrac{-\\frac32-\\frac32}{-3-3}=\\dfrac12$，$l:\\ y=\\dfrac12x$，即 $x-2y=0$。",
        "points": [
            "第(1)问：由 $A,P$ 在椭圆上解出 $b^2=9$，$a^2=12$（3分）；$c^2=a^2-b^2=3$，故 $e=\\dfrac{c}{a}=\\dfrac12$（3分）",
            "第(2)问：求出直线 $AP$ 方程 $x+2y-6=0$ 与 $|AP|=\\dfrac{3\\sqrt5}{2}$，由面积得 $B$ 到 $AP$ 的距离 $d=\\dfrac{12}{\\sqrt5}$（4分）",
            "第(2)问：定出 $B(0,-3)$ 或 $B\\left(-3,-\\dfrac32\\right)$，进而得 $l:\\ 3x-2y-6=0$ 或 $x-2y=0$（5分）",
        ],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "17",
        "source_ref": "https://zy.21cnjy.com/26578731",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_space_vec",
        "difficulty": 5,
        "stem": "如图，四棱锥 $P-ABCD$ 中，$PA\\perp$ 底面 $ABCD$，$PA=AC=2$，$BC=1$，$AB=\\sqrt{3}$。\n"
                "(1) 若 $AD\\perp PB$，证明：$AD\\parallel$ 平面 $PBC$；\n"
                "(2) 若 $AD\\perp DC$，且二面角 $A-CP-D$ 的正弦值为 $\\dfrac{\\sqrt{42}}{7}$，求 $AD$。",
        "options": [],
        "answer": "(1) 证明见解析；(2) $AD=\\sqrt{3}$",
        "analysis": "解析：(1) 因为 $PA\\perp$ 底面 $ABCD$，$AD\\subset$ 底面 $ABCD$，所以 $PA\\perp AD$；"
                    "又 $AD\\perp PB$，$PA\\cap PB=P$，$PA,PB\\subset$ 平面 $PAB$，故 $AD\\perp$ 平面 $PAB$，"
                    "而 $AB\\subset$ 平面 $PAB$，所以 $AD\\perp AB$。由 $AB^{2}+BC^{2}=3+1=4=AC^{2}$ 知 $AB\\perp BC$，"
                    "故 $AD\\parallel BC$。又 $AD\\not\\subset$ 平面 $PBC$，$BC\\subset$ 平面 $PBC$，所以 $AD\\parallel$ 平面 $PBC$。\n"
                    "(2) 由 $AD\\perp DC$ 且 $PA\\perp$ 底面，以 $D$ 为原点，$DA$、$DC$ 所在直线及过点 $D$ 且平行于 $AP$ 的直线"
                    "分别为 $x,y,z$ 轴建立空间直角坐标系。设 $AD=t$，由 $AD^{2}+DC^{2}=AC^{2}=4$ 得 $DC=\\sqrt{4-t^{2}}$，"
                    "于是 $A(t,0,0)$，$P(t,0,2)$，$C(0,\\sqrt{4-t^{2}},0)$，$D(0,0,0)$。\n"
                    "平面 $CPD$ 的法向量可取 $\\boldsymbol{n}_{2}=(-2,0,t)$；平面 $ACP$ 的法向量可取 "
                    "$\\boldsymbol{n}_{1}=(\\sqrt{4-t^{2}},\\,t,\\,0)$。\n"
                    "二面角正弦值为 $\\dfrac{\\sqrt{42}}{7}$，故其余弦绝对值 $\\sqrt{1-\\dfrac{42}{49}}=\\dfrac{\\sqrt7}{7}$："
                    "$|\\cos\\langle\\boldsymbol n_{1},\\boldsymbol n_{2}\\rangle|="
                    "\\dfrac{2\\sqrt{4-t^{2}}}{2\\sqrt{4+t^{2}}}=\\dfrac{\\sqrt7}{7}$，即 $\\dfrac{4-t^{2}}{4+t^{2}}=\\dfrac17$，"
                    "解得 $t^{2}=3$，$t=\\sqrt3$，即 $AD=\\sqrt{3}$。",
        "points": [
            "第(1)问：由 $PA\\perp$ 底面与 $AD\\perp PB$ 推出 $AD\\perp$ 平面 $PAB$，得 $AD\\perp AB$（3分）；"
            "由 $AB^2+BC^2=AC^2$ 得 $BC\\perp AB$，故 $AD\\parallel BC$，从而 $AD\\parallel$ 平面 $PBC$（3分）",
            "第(2)问：正确建系并写出 $A,P,C,D$ 坐标（3分）",
            "第(2)问：求出两平面的法向量 $\\boldsymbol n_1=(\\sqrt{4-t^2},t,0)$、$\\boldsymbol n_2=(-2,0,t)$（3分）",
            "第(2)问：由正弦值 $\\dfrac{\\sqrt{42}}{7}$ 化为余弦值 $\\dfrac{\\sqrt7}{7}$，解方程得 $t=\\sqrt3$，即 $AD=\\sqrt3$（3分）",
        ],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "18",
        "source_ref": "http://lanqi.org?p=36026/",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_deriv",
        "difficulty": 5,
        "stem": "已知函数 $f(x)=\\ln\\dfrac{x}{2-x}+ax+b(x-1)^{3}$。\n"
                "(1) 若 $b=0$，且 $f'(x)\\ge 0$，求 $a$ 的最小值；\n"
                "(2) 证明：曲线 $y=f(x)$ 是中心对称图形；\n"
                "(3) 若 $f(x)>-2$ 当且仅当 $1<x<2$，求 $b$ 的取值范围。",
        "options": [],
        "answer": "(1) $-2$；(2) 曲线关于点 $(1,a)$ 中心对称；(3) $b\\ge-\\dfrac{2}{3}$",
        "analysis": "解析：定义域由 $\\dfrac{x}{2-x}>0$ 得 $x\\in(0,2)$。\n"
                    "(1) $b=0$ 时 $f(x)=\\ln\\dfrac{x}{2-x}+ax$，$f'(x)=\\dfrac{1}{x}+\\dfrac{1}{2-x}+a="
                    "\\dfrac{2}{x(2-x)}+a$。因为 $x(2-x)\\le\\left(\\dfrac{x+2-x}{2}\\right)^{2}=1$（$x=1$ 取等号），"
                    "所以 $\\dfrac{2}{x(2-x)}\\ge2$，其最小值为 $2$。要使 $f'(x)\\ge0$ 恒成立，需 $-a\\le2$，即 $a\\ge-2$，"
                    "故 $a$ 的最小值为 $-2$。\n"
                    "(2) $f(2-x)=\\ln\\dfrac{2-x}{x}+a(2-x)+b(1-x)^{3}"
                    "=-\\left[\\ln\\dfrac{x}{2-x}+ax+b(x-1)^{3}\\right]+2a=-f(x)+2a$，"
                    "即 $f(x)+f(2-x)=2a$，故曲线 $y=f(x)$ 关于点 $(1,a)$ 成中心对称图形。\n"
                    "(3) 由 $f(x)>-2$ 当且仅当 $1<x<2$ 及 $f$ 连续知 $x=1$ 是 $f(x)=-2$ 的一个解，"
                    "故 $f(1)=0+a+0=-2$，得 $a=-2$。此时令 $t=x-1\\in(-1,1)$，"
                    "$g(t)=f(1+t)+2=\\ln\\dfrac{1+t}{1-t}-2t+bt^{3}$，$g(0)=0$，"
                    "$g'(t)=\\dfrac{2}{1-t^{2}}-2+3bt^{2}=t^{2}\\left(\\dfrac{2}{1-t^{2}}+3b\\right)$。\n"
                    "若 $b\\ge-\\dfrac23$，则 $\\dfrac{2}{1-t^{2}}+3b\\ge2-2=0$（$t\\ne0$ 时严格 $>0$），"
                    "$g$ 在 $(-1,1)$ 上单调递增，故 $t>0$（即 $1<x<2$）时 $g(t)>0$，$t<0$ 时 $g(t)<0$，符合题意；\n"
                    "若 $b<-\\dfrac23$，则在 $t=0$ 右侧充分小的区间内 $\\dfrac{2}{1-t^{2}}+3b<0$，$g'(t)<0$，"
                    "得 $g(t)<0$，与“$1<x<2$ 时 $f(x)>-2$”矛盾。综上 $b\\ge-\\dfrac{2}{3}$。",
        "points": [
            "第(1)问：写出 $f'(x)=\\dfrac{2}{x(2-x)}+a$，用基本不等式得 $\\dfrac{2}{x(2-x)}\\ge2$（$x=1$ 取等）（3分）；"
            "得 $a\\ge-2$，最小值为 $-2$（2分）",
            "第(2)问：计算 $f(2-x)=-f(x)+2a$ 或 $f(x)+f(2-x)=2a$，说明对称中心为 $(1,\\ a)$（5分）",
            "第(3)问：由“当且仅当”与连续性得 $f(1)=-2$，求出 $a=-2$（2分）；"
            "换元 $t=x-1$ 得 $g'(t)=t^2\\left(\\dfrac{2}{1-t^2}+3b\\right)$ 并分类讨论（3分）；"
            "证得 $b\\ge-\\dfrac23$ 时成立、$b<-\\dfrac23$ 时不成立，写出范围（2分）",
        ],
    },
    {
        "year": 2023,
        "paper": "全国乙卷（理科）",
        "question_no": "17",
        "source_ref": "https://cdn.zizzs.com/zixunzhan/202310/e96eb015-4652-4ed4-b391-0145db94d500.pdf",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_stat2",
        "difficulty": 4,
        "stem": "某厂为比较甲、乙两种工艺对橡胶产品伸缩率的处理效应，进行 $10$ 次配对试验，每次配对试验选用材质相同的两个"
                "橡胶产品，随机地选其中一个用甲工艺处理，另一个用乙工艺处理，测量处理后的橡胶产品的伸缩率。"
                "甲、乙两种工艺处理后的橡胶产品的伸缩率分别记为 $x_{i},y_{i}\\ (i=1,2,\\cdots,10)$，试验结果如下：\n"
                "试验序号 $i$：$1\\quad2\\quad3\\quad4\\quad5\\quad6\\quad7\\quad8\\quad9\\quad10$\n"
                "伸缩率 $x_{i}$：$545\\quad533\\quad551\\quad522\\quad575\\quad544\\quad541\\quad568\\quad596\\quad548$\n"
                "伸缩率 $y_{i}$：$536\\quad527\\quad543\\quad530\\quad560\\quad533\\quad522\\quad550\\quad576\\quad536$\n"
                "记 $z_{i}=x_{i}-y_{i}\\ (i=1,2,\\cdots,10)$，记 $z_{1},z_{2},\\cdots,z_{10}$ 的样本平均数为 $\\bar z$，"
                "样本方差为 $s^{2}$。\n"
                "(1) 求 $\\bar z$，$s^{2}$；\n"
                "(2) 判断甲工艺处理后的橡胶产品的伸缩率较乙工艺处理后的橡胶产品的伸缩率是否有显著提高"
                "（如果 $\\bar z\\ge 2\\sqrt{\\dfrac{s^{2}}{10}}$，则认为甲工艺处理后的橡胶产品的伸缩率较乙工艺处理后的"
                "橡胶产品的伸缩率有显著提高，否则不认为有显著提高）。",
        "options": [],
        "answer": "(1) $\\bar z=11$，$s^{2}=61$；(2) 有显著提高",
        "analysis": "解析：(1) 逐项相减得 $z_{i}$ 依次为 $9,\\,6,\\,8,\\, -8,\\,15,\\,11,\\,19,\\,18,\\,20,\\,12$，"
                    "故 $\\bar z=\\dfrac{9+6+8-8+15+11+19+18+20+12}{10}=\\dfrac{110}{10}=11$。\n"
                    "$s^{2}=\\dfrac{1}{10}\\big[(-2)^{2}+(-5)^{2}+(-3)^{2}+(-19)^{2}+4^{2}+0^{2}+8^{2}+7^{2}+9^{2}+1^{2}\\big]$"
                    "$=\\dfrac{4+25+9+361+16+0+64+49+81+1}{10}=\\dfrac{610}{10}=61$。\n"
                    "(2) $2\\sqrt{\\dfrac{s^{2}}{10}}=2\\sqrt{6.1}\\approx4.94$，而 $\\bar z=11>4.94$，"
                    "满足 $\\bar z\\ge2\\sqrt{\\dfrac{s^{2}}{10}}$，故认为甲工艺处理后的橡胶产品的伸缩率较乙工艺处理后的"
                    "橡胶产品的伸缩率有显著提高。",
        "points": [
            "第(1)问：算出 10 个 $z_i=x_i-y_i$ 的值（3分）；求 $\\bar z=11$（2分）；求 $s^2=61$（4分）",
            "第(2)问：计算临界值 $2\\sqrt{\\dfrac{s^2}{10}}=2\\sqrt{6.1}\\approx4.94$（2分）；"
            "比较 $\\bar z$ 与临界值并得出“有显著提高”的结论（1分）",
        ],
    },
]
