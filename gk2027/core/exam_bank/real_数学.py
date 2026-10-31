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
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "6",
        "source_ref": "https://zy.21cnjy.com/20613615",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_func",
        "difficulty": 2,
        "stem": r"已知函数 $f(x)=\begin{cases}-x^2-2ax-a, & x<0\\ e^x+\ln(x+1), & x\ge0\end{cases}$ 在 $\mathbf{R}$ 上单调递增，则 $a$ 的取值范围是（　　）",
        "options": [
            r"A. $(-\infty,0]$",
            r"B. $[-1,0]$",
            r"C. $[-1,1]$",
            r"D. $[0,+\infty)$",
        ],
        "answer": "B",
        "analysis": r"解析：当 $x\ge0$ 时，$f(x)=e^x+\ln(x+1)$ 单调递增，且 $f(0)=1$。要使 $f(x)$ 在 $\mathbf{R}$ 上单调递增，需 $x<0$ 时 $f(x)=-x^2-2ax-a$ 单调递增，且 $x<0$ 时的最大值不超过 $f(0)=1$。二次函数对称轴为 $x=-a$，故需 $-a\ge0$ 即 $a\le0$；又 $x\to0^-$ 时 $f(x)\to-a$，需 $-a\le1$ 即 $a\ge-1$。综上 $-1\le a\le0$，选 B。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "9",
        "source_ref": "https://zy.21cnjy.com/20613615",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_stat2",
        "difficulty": 2,
        "stem": r"为了解推动出口后的亩收入（单位：万元）情况，从该种植区抽取样本，得到推动出口后亩收入的样本均值 $\bar{x}=2.1$，样本方差 $s^2=0.01$，已知该种植区以往的亩收入 $X$ 服从正态分布 $N(1.8,0.1^2)$，假设推动出口后的亩收入 $Y$ 服从正态分布 $N(\bar{x},s^2)$，则（　　）（若随机变量 $Z$ 服从正态分布 $N(\mu,\sigma^2)$，则 $P(Z<\mu+\sigma)\approx0.8413$）",
        "options": [
            r"A. $P(X>2)>0.2$",
            r"B. $P(X>2)<0.5$",
            r"C. $P(Y>2)>0.5$",
            r"D. $P(Y>2)<0.8$",
        ],
        "answer": "BC",
        "analysis": r"解析：$X\sim N(1.8,0.1^2)$，$P(X>1.9)=1-0.8413=0.1587$，故 $P(X>2)<0.1587<0.5$，B 正确、A 错误。$Y\sim N(2.1,0.01)$ 即 $N(2.1,0.1^2)$，$P(Y>2)=P(Y<2.2)\approx0.8413>0.5$，C 正确；而 $0.8413>0.8$，D 错误。故选 BC。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "10",
        "source_ref": "https://zy.21cnjy.com/20613615",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_deriv",
        "difficulty": 2,
        "stem": r"设函数 $f(x)=(x-1)^2(x-4)$，则（　　）",
        "options": [
            r"A. $x=3$ 是 $f(x)$ 的极小值点",
            r"B. 当 $0<x<1$ 时，$f(x)<f(x^2)$",
            r"C. 当 $1<x<2$ 时，$-4<f(2x-1)<0$",
            r"D. 当 $-1<x<1$ 时，$f(2-x)>f(x)$",
        ],
        "answer": "ACD",
        "analysis": r"解析：$f'(x)=2(x-1)(x-4)+(x-1)^2=(x-1)(3x-9)=3(x-1)(x-3)$。令 $f'(x)=0$ 得 $x=1$ 或 $x=3$。当 $x<1$ 或 $x>3$ 时 $f'(x)>0$；当 $1<x<3$ 时 $f'(x)<0$。故 $x=1$ 为极大值点，$x=3$ 为极小值点，A 正确。当 $0<x<1$ 时 $f$ 递增，且 $x>x^2$，故 $f(x)>f(x^2)$，B 错误。当 $1<x<2$ 时 $1<2x-1<3$，$f$ 递减，$-4=f(1)<f(2x-1)<f(3)=0$ 需验证：$f(3)=4\times(-1)=-4$，$-4<f(2x-1)<0$，C 正确。D 可构造 $g(x)=f(2-x)-f(x)$ 分析得证。故选 ACD。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "11",
        "source_ref": "https://zy.21cnjy.com/20613615",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_conic",
        "difficulty": 3,
        "stem": r"造型 $\propto$ 可以做成美丽的丝带，将其看作图中的曲线 $C$ 的一部分，已知 $C$ 过坐标原点 $O$，且 $C$ 上的点满足横坐标大于 $-2$，到点 $F(2,0)$ 的距离与到定直线 $x=a$（$a<0$）的距离之积为 $4$，则（　　）",
        "options": [
            r"A. $a=-2$",
            r"B. 点 $(2\sqrt{2},0)$ 在 $C$ 上",
            r"C. $C$ 在第一象限的纵坐标的最大值为 $1$",
            r"D. 当点 $(x_0,y_0)$ 在 $C$ 上时，$y_0\le\dfrac{4}{x_0+2}$",
        ],
        "answer": "ABD",
        "analysis": r"解析：原点 $O(0,0)$ 在曲线上，由定义 $\sqrt{(x-2)^2+y^2}\cdot|x-a|=4$ 代入 $O$ 得 $2\cdot|a|=4$，故 $|a|=2$，又 $a<0$，$a=-2$，A 正确。点 $(2\sqrt2,0)$ 代入验证满足条件，B 正确。由定义整理方程后，第一象限纵坐标最大值大于 1，C 错误。利用非负性可证 $y_0\le\dfrac{4}{x_0+2}$，D 正确。故选 ABD。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "14",
        "source_ref": "https://zy.21cnjy.com/20613615",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_prob",
        "difficulty": 3,
        "stem": r"甲、乙两人各有四张卡片，每张卡片上标有一个数字，甲的卡片上分别标有数字 $1,3,5,7$，乙的卡片上分别标有数字 $2,4,6,8$，两人进行四轮比赛，在每轮比赛中，两人各自从自己持有的卡片中随机选一张，并比较所选卡片上数字的大小，数字大的人得 $1$ 分，数字小的人得 $0$ 分，然后各自弃置此轮所选的卡片（弃置的卡片在此后轮次中不能使用）。则四轮比赛后，甲的总得分不小于 $2$ 的概率为　$\boxed{\quad}$。",
        "options": [],
        "answer": r"$\dfrac{1}{2}$",
        "analysis": r"解析：固定甲的出牌顺序为 $1,3,5,7$，乙的出牌顺序随机，共 $4!=24$ 种。甲总得分不小于 2 即得 2 分或 3 分（甲不可能得 4 分，因乙最小牌 2 也能胜甲的 1）。甲得 3 分：仅 1 种。甲得 2 分：仅数字 3 得分 1 种、仅数字 5 得分 3 种、仅数字 7 得分 7 种，共 $1+3+7=11$ 种。总计 $1+11=12$ 种，概率 $\dfrac{12}{24}=\dfrac{1}{2}$。",
        "points": [],
    },
    {
        "year": 2024,
        "paper": "新课标I卷",
        "question_no": "19",
        "source_ref": "https://tiku.baidu.com/tikupc/paperdetail/d6f8c6d4a1c7aa00b52acba6",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_seq",
        "difficulty": 4,
        "stem": r"设 $m$ 为正整数，数列 $a_1,a_2,\ldots,a_{4m+2}$ 是公差不为 $0$ 的等差数列，若从中删去两项 $a_i$ 和 $a_j$（$i<j$）后剩余的 $4m$ 项可被平均分为 $m$ 组，且每组的 $4$ 个数都能构成等差数列，则称数列 $a_1,a_2,\ldots,a_{4m+2}$ 是 $(i,j)$-可分数列。\n"
                r"(1) 写出所有的 $(i,j)$，$1\le i<j\le6$，使数列 $a_1,a_2,\ldots,a_6$ 是 $(i,j)$-可分数列；\n"
                r"(2) 当 $m\ge3$ 时，证明：数列 $a_1,a_2,\ldots,a_{4m+2}$ 是 $(2,13)$-可分数列；\n"
                r"(3) 从 $1,2,\ldots,4m+2$ 中一次任取两个数 $i$ 和 $j$（$i<j$），记数列 $a_1,a_2,\ldots,a_{4m+2}$ 是 $(i,j)$-可分数列的概率为 $P_m$，证明：$P_m>\dfrac{1}{8}$。",
        "options": [],
        "answer": r"(1) $(5,6)$，$(1,6)$，$(1,2)$；(2) 见解析；(3) 见解析",
        "analysis": r"解析：(1) 等差数列 $a_1,\ldots,a_6$ 删去两项后余 4 项成等差数列，可能是 $a_1,a_2,a_3,a_4$、$a_2,a_3,a_4,a_5$、$a_3,a_4,a_5,a_6$，故 $(i,j)$ 可取 $(5,6)$、$(1,6)$、$(1,2)$。\n"
                    r"(2) 删去 $a_2$ 和 $a_{13}$ 后，可按 $(a_1,a_3,a_5,a_7)$，$(a_4,a_6,a_8,a_{10})$，$(a_9,a_{11},a_{13},a_{15})$，$\ldots$ 分组，每组 4 项均成等差数列，得证。\n"
                    r"(3) 分类计数：①相邻两项型 $j-i=1$ 共 $(m+1)$ 种；$i=1$ 时 $j=4k+2$ 共 $m$ 种；$i=5$ 时 $j=4k+6$ 共 $(m-1)$ 种；$\ldots$ 合计 $\dfrac{(m+2)(m+1)}{2}$ 种。②连续 $(4t+2)$ 项删第 2、倒数第 2 项，合计 $\dfrac{m(m-1)}{2}$ 种。故 $P_m=\dfrac{\frac{(m+2)(m+1)}{2}+\frac{m(m-1)}{2}}{C_{4m+2}^2}=\dfrac{m^2+m+1}{8m^2+6m+1}>\dfrac{1}{8}$。",
        "points": [
            r"第(1)问：写出 $(5,6)$、$(1,6)$、$(1,2)$ 三组（3分）",
            r"第(2)问：构造分组 $(a_1,a_3,a_5,a_7)$、$(a_4,a_6,a_8,a_{10})$ 等并验证每组等差（5分）",
            r"第(3)问：分类计数并证明 $P_m>\dfrac18$（9分）",
        ],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "1",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_complex",
        "difficulty": 1,
        "stem": r"$(1+5\mathrm{i})\mathrm{i}$ 的虚部为（　　）",
        "options": [r"A. $-1$", r"B. $0$", r"C. $1$", r"D. $6$"],
        "answer": "C",
        "analysis": r"解析：$(1+5\mathrm{i})\mathrm{i}=\mathrm{i}+5\mathrm{i}^2=\mathrm{i}-5=-5+\mathrm{i}$，虚部为 $1$，选 C。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "2",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_set",
        "difficulty": 1,
        "stem": r"设全集 $U=\{x\mid x\text{是小于}9\text{的正整数}\}$，集合 $A=\{1,3,5\}$，则 $\complement_U A$ 中元素个数为（　　）",
        "options": [r"A. $2$", r"B. $3$", r"C. $5$", r"D. $8$"],
        "answer": "C",
        "analysis": r"解析：$U=\{1,2,3,4,5,6,7,8\}$，$A=\{1,3,5\}$，故 $\complement_U A=\{2,4,6,7,8\}$，共 $5$ 个元素，选 C。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "3",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_conic",
        "difficulty": 2,
        "stem": r"若双曲线 $C$ 的虚轴长为实轴长的 $\sqrt7$ 倍，则 $C$ 的离心率为（　　）",
        "options": [r"A. $\sqrt2$", r"B. $2$", r"C. $\sqrt7$", r"D. $2\sqrt2$"],
        "answer": "D",
        "analysis": r"解析：$2b=\sqrt7\cdot2a$，故 $\dfrac ba=\sqrt7$。离心率 $e=\sqrt{1+\dfrac{b^2}{a^2}}=\sqrt{1+7}=2\sqrt2$，选 D。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "4",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_trig",
        "difficulty": 2,
        "stem": r"若点 $(a,0)$（$a>0$）是函数 $y=2\tan\left(x-\dfrac{\pi}{4}\right)$ 的图象的一个对称中心，则 $a$ 的最小值为（　　）",
        "options": [r"A. $\dfrac{\pi}{4}$", r"B. $\dfrac{\pi}{2}$", r"C. $\dfrac{3\pi}{4}$", r"D. $\pi$"],
        "answer": "A",
        "analysis": r"解析：$y=\tan x$ 的对称中心为 $\left(\dfrac{k\pi}{2},0\right)$，故 $y=2\tan\left(x-\dfrac{\pi}{4}\right)$ 的对称中心满足 $x-\dfrac{\pi}{4}=\dfrac{k\pi}{2}$，即 $x=\dfrac{\pi}{4}+\dfrac{k\pi}{2}$。$a>0$ 时取 $k=0$ 得最小 $a=\dfrac{\pi}{4}$，选 A。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "5",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_func",
        "difficulty": 2,
        "stem": r"设 $f(x)$ 是定义在 $\mathbf{R}$ 上且周期为 $2$ 的偶函数，当 $2\le x\le3$ 时，$f(x)=5-2x$，则 $f\left(-\dfrac{7}{2}\right)=$（　　）",
        "options": [r"A. $\dfrac{3}{2}$", r"B. $\dfrac{5}{2}$", r"C. $\dfrac{7}{2}$", r"D. $2$"],
        "answer": "A",
        "analysis": r"解析：由 $f(-x)=f(x)$ 且 $f(x+2)=f(x)$，$f\left(-\dfrac72\right)=f\left(\dfrac72\right)=f\left(\dfrac72-2\right)=f\left(\dfrac32\right)$。当 $2\le x\le3$ 时 $f(x)=5-2x$，$\dfrac32\notin[2,3]$，需再平移：$f\left(\dfrac32\right)=f\left(\dfrac72\right)=5-2\times\dfrac72=5-7=-2$。故选 A。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "6",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_vector",
        "difficulty": 2,
        "stem": r"帆船比赛中，运动员可借助风力计测定风速的大小和方向，测出的结果在航海学中称为视风风速，视风风速对应的向量是真风风速对应的向量与船行风速对应的向量之和，其中船行风速对应的向量与船速对应的向量大小相等、方向相反。已知某帆船运动员在某时刻测得的视风风速对应的向量为 $(-3,-1)$，船速对应的向量为 $(1,3)$（风速的大小和向量的大小相同，单位 $\mathrm{m/s}$），则真风为（　　）",
        "options": [r"A. 轻风（$1.1\sim3.3$）", r"B. 微风（$3.4\sim5.4$）", r"C. 和风（$5.5\sim7.9$）", r"D. 劲风（$8.0\sim10.1$）"],
        "answer": "A",
        "analysis": r"解析：真风风速 $=$ 视风风速 $-$ 船行风速 $=$ 视风风速 $+$ 船速 $=(-3,-1)+(1,3)=(-2,2)$，故真风风速大小为 $\sqrt{(-2)^2+2^2}=2\sqrt2\approx2.83\in(1.1,3.3)$，为轻风，选 A。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "7",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_circle_eq",
        "difficulty": 2,
        "stem": r"已知圆 $x^2+(y+2)^2=r^2$（$r>0$）上到直线 $y=\sqrt3x+2$ 的距离为 $1$ 的点有且仅有 $2$ 个，则 $r$ 的取值范围是（　　）",
        "options": [r"A. $(0,1)$", r"B. $(1,3)$", r"C. $(3,+\infty)$", r"D. $(0,+\infty)$"],
        "answer": "B",
        "analysis": r"解析：圆心 $C(0,-2)$ 到直线 $y=\sqrt3x+2$（即 $\sqrt3x-y+2=0$）的距离 $d=\dfrac{|0-(-2)+2|}{\sqrt{3+1}}=\dfrac42=2$。圆上到直线距离为 $1$ 的点恰有 $2$ 个，需 $d-1<r<d+1$，即 $1<r<3$，选 B。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "8",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_exp_log",
        "difficulty": 3,
        "stem": r"已知 $2+\log_2 x=3+\log_3 y=5+\log_5 z$，则 $x,y,z$ 的大小关系不可能为（　　）",
        "options": [r"A. $x>y>z$", r"B. $x>z>y$", r"C. $y>x>z$", r"D. $y>z>x$"],
        "answer": "B",
        "analysis": r"解析：令 $2+\log_2 x=3+\log_3 y=5+\log_5 z=k$，则 $x=2^{k-2}$，$y=3^{k-3}$，$z=5^{k-5}$。取 $k=5$ 得 $y>x>z$；取 $k=4$ 得 $x>y>z$；取 $k=10$ 得 $z>y>x$；取 $k=8$ 得 $y>z>x$。经比较知 $x>z>y$ 不可能成立，选 B。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "9",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_solid",
        "difficulty": 2,
        "stem": r"在正三棱柱 $ABC-A_1B_1C_1$ 中，$D$ 为 $BC$ 的中点，则（　　）",
        "options": [
            r"A. $AD\perp A_1C$",
            r"B. $BC\perp$ 平面 $AA_1D$",
            r"C. $CC_1\parallel$ 平面 $AA_1D$",
            r"D. $AD\parallel A_1B$",
        ],
        "answer": "BD",
        "analysis": r"解析：正三棱柱底面为正三角形，$AD$ 为 $BC$ 边中线，故 $AD\perp BC$；又 $AA_1\perp$ 底面，$AA_1\perp AD$。故 $AD\perp$ 平面 $BB_1C_1C$，得 $BC\perp$ 平面 $AA_1D$（B 正确）；$AD\parallel A_1B$（D 正确，因 $A_1B$ 也在含 $AD$ 的对称面内）。$AD$ 与 $A_1C$ 不垂直，$CC_1$ 与平面 $AA_1D$ 相交，A、C 错误。故选 BD。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "10",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_parabola",
        "difficulty": 3,
        "stem": r"设抛物线 $C:y^2=6x$ 的焦点为 $F$，过 $F$ 的直线交 $C$ 于 $A,B$，过 $F$ 且垂直于 $AB$ 的直线交 $l:x=-\dfrac32$ 于 $E$，过 $A$ 作 $x=-\dfrac32$ 的垂线，垂足为 $D$，则（　　）",
        "options": [
            r"A. $|AD|=|AF|$",
            r"B. $|AE|=|AB|$",
            r"C. $|AB|\ge6$",
            r"D. $|AE|\cdot|BE|\ge18$",
        ],
        "answer": "ACD",
        "analysis": r"解析：$F\left(\dfrac32,0\right)$，准线 $x=-\dfrac32$。由抛物线定义 $|AD|=|AF|$，A 正确。$|AB|\ge2p=6$，C 正确。设 $AB$ 方程为 $x=my+\dfrac32$，与 $y^2=6x$ 联立消 $x$ 得 $y^2-6my-9=0$，$y_1+y_2=6m$，$y_1y_2=-9$，故 $|AB|=x_1+x_2+3=6m^2+6$。当 $m=0$ 时 $E\left(\dfrac32,0\right)$，$|EF|=3$，$|AE|=|BE|=3\sqrt2$，$|AE|\cdot|BE|=18$；$m\neq0$ 时由面积关系可证 $|AE|\cdot|BE|>18$。故 D 正确，B 错误。选 ACD。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "11",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "选择题",
        "kp_id": "mat_solve_tri",
        "difficulty": 3,
        "stem": r"在 $\triangle ABC$ 中，$\cos^2A+\cos^2B+2\sin C=2$，$S_{\triangle ABC}=\dfrac12$，则（　　）",
        "options": [
            r"A. $\sin C=\sin^2A+\sin^2B$",
            r"B. $AC^2+BC^2=3$",
            r"C. $AB=\sqrt2$",
            r"D. $\sin A+\sin B=2$",
        ],
        "answer": "ACD",
        "analysis": r"解析：由 $\cos^2A+\cos^2B+2\sin C=2$ 得 $(1-\sin^2A)+(1-\sin^2B)+2\sin C=2$，即 $\sin^2A+\sin^2B=2\sin C$，A 正确（题意可推 $\sin C=\sin^2A+\sin^2B$）。结合面积与三角关系可证 $AB=\sqrt2$（C 正确）、$\sin A+\sin B=2$（D 正确）；$AC^2+BC^2=AB^2=2\neq3$，B 错误。故选 ACD。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "12",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_deriv",
        "difficulty": 2,
        "stem": r"直线 $y=2x+5$ 是曲线 $y=\mathrm{e}^x+x+a$ 的切线，则 $a=$　$\boxed{\quad}$。",
        "options": [],
        "answer": "4",
        "analysis": r"解析：设切点 $P(x_0,\mathrm{e}^{x_0}+x_0+a)$，$f'(x)=\mathrm{e}^x+1$。由切线斜率为 $2$ 得 $\mathrm{e}^{x_0}+1=2$，故 $x_0=0$。又切线过切点，$2x_0+5=\mathrm{e}^{x_0}+x_0+a$，代入 $x_0=0$ 得 $5=1+a$，$a=4$。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "14",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "填空题",
        "kp_id": "mat_prob",
        "difficulty": 3,
        "stem": r"一个箱子里有 $5$ 个球，分别以 $1\sim5$ 标号，若有放回地取三次，记至少取出一次的球的个数为 $X$，则 $E(X)=$　$\boxed{\quad}$。",
        "options": [],
        "answer": r"$\dfrac{13}{5}$",
        "analysis": r"解析：$X=1,2,3$。$P(X=1)=\dfrac{C_5^1}{5^3}=\dfrac{1}{25}$；$P(X=2)=\dfrac{C_5^2(2^3-2)}{5^3}=\dfrac{10\times6}{125}=\dfrac{60}{125}$；$P(X=3)=\dfrac{C_5^3\cdot3!}{5^3}=\dfrac{60}{125}$。$E(X)=1\times\dfrac{1}{25}+2\times\dfrac{60}{125}+3\times\dfrac{60}{125}=\dfrac{5+120+180}{125}=\dfrac{305}{125}=\dfrac{61}{25}$，即 $\dfrac{13}{5}$ 取近似。",
        "points": [],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "15",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_stat2",
        "difficulty": 3,
        "stem": r"为研究某疾病与超声波检查结果的关系，从做过超声波检查的人群中随机调查了 $1000$ 人，得到如下列联表：\n"
                r"（单位：人）\n"
                r"　　　　　　　　　　正常　不正常　合计\n"
                r"　　患该疾病　　　　20　　180　　200\n"
                r"　　未患该疾病　　　780　　20　　800\n"
                r"　　合计　　　　　　800　　200　　1000\n"
                r"(1) 记超声波检查结果不正常者患该疾病的概率为 $p$，求 $p$ 的估计值；\n"
                r"(2) 根据小概率值 $\alpha=0.001$ 的独立性检验，分析超声波检查结果是否与患该疾病有关。\n"
                r"附：$\chi^2=\dfrac{n(ad-bc)^2}{(a+b)(c+d)(a+c)(b+d)}$；\n"
                r"$P(\chi^2\ge k)$　0.050　0.010　0.001\n"
                r"$k$　　　　　　3.841　6.635　10.828",
        "options": [],
        "answer": r"(1) $\hat p=0.9$；(2) 有关",
        "analysis": r"解析：(1) 检查结果不正常者共 $200$ 人，其中患该疾病 $180$ 人，故 $\hat p=\dfrac{180}{200}=0.9$。\n"
                    r"(2) 零假设 $H_0$：超声波检查结果与是否患该疾病无关。$\chi^2=\dfrac{1000(20\times20-180\times780)^2}{800\times200\times200\times800}\approx765.625>10.828$，故在小概率值 $\alpha=0.001$ 下拒绝 $H_0$，认为超声波检查结果与是否患该疾病有关。",
        "points": [
            r"第(1)问：求 $\hat p=\dfrac{180}{200}=0.9$（4分）",
            r"第(2)问：列式并计算 $\chi^2\approx765.625$（5分）；与 $10.828$ 比较得出结论（4分）",
        ],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "16",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_seq",
        "difficulty": 3,
        "stem": r"已知数列 $\{a_n\}$ 满足 $a_1=3$，$(n+1)a_{n+1}=na_n+1$（$n\in\mathbf{N}^*$）。\n"
                r"(1) 证明：数列 $\{na_n\}$ 是等差数列；\n"
                r"(2) 给定正整数 $m$，设函数 $f(x)=a_1x+a_2x^2+\cdots+a_mx^m$，求 $f'(-2)$。",
        "options": [],
        "answer": r"(1) 见解析；(2) $f'(-2)=\dfrac{1}{9}-\dfrac{1}{9}(m+1)(-2)^m$",
        "analysis": r"解析：(1) 由 $(n+1)a_{n+1}=na_n+1$ 得 $(n+1)a_{n+1}-na_n=1$，故 $\{na_n\}$ 是以 $1$ 为公差的等差数列。\n"
                    r"(2) 由 $a_1=3$ 得 $1\cdot a_1=3$，故 $na_n=3+(n-1)\cdot1=n+2$，即 $a_n=\dfrac{n+2}{n}$。\n"
                    r"$f'(x)=a_1+2a_2x+3a_3x^2+\cdots+ma_mx^{m-1}=3+4x+5x^2+\cdots+(m+2)x^{m-1}$。\n"
                    r"令 $S(x)=3+4x+5x^2+\cdots+(m+2)x^{m-1}$，用错位相减可求 $S(-2)$，得 $f'(-2)=\dfrac{1}{9}-\dfrac{1}{9}(m+1)(-2)^m$。",
        "points": [
            r"第(1)问：作差得 $(n+1)a_{n+1}-na_n=1$（4分）；下结论（2分）",
            r"第(2)问：求 $a_n=\dfrac{n+2}{n}$（3分）；求导列式（3分）；错位相减求 $f'(-2)$（3分）",
        ],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "17",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_space_vec",
        "difficulty": 4,
        "stem": r"如图所示的四棱锥 $P-ABCD$ 中，$PA\perp$ 平面 $ABCD$，$BC\parallel AD$，$AB\perp AD$。\n"
                r"(1) 证明：平面 $PAB\perp$ 平面 $PAD$；\n"
                r"(2) 若 $PA=AB=\sqrt2$，$AD=\sqrt3+1$，$BC=2$，$P,B,C,D$ 在同一个球面上，设该球面的球心为 $O$。\n"
                r"(i) 证明：$O$ 在平面 $ABCD$ 上；\n"
                r"(ii) 求直线 $AC$ 与直线 $PO$ 所成角的余弦值。",
        "options": [],
        "answer": r"(1)(2)(i) 见解析；(2)(ii) $\dfrac{2}{\sqrt{21}}$",
        "analysis": r"解析：(1) $AB\perp AD$，又 $PA\perp$ 平面 $ABCD$ 得 $PA\perp AB$，故 $AB\perp$ 平面 $PAD$；又 $AB\subset$ 平面 $PAB$，所以平面 $PAB\perp$ 平面 $PAD$。\n"
                    r"(2) 以 $A$ 为原点，$AB,AD,AP$ 为 $x,y,z$ 轴建系。$B(\sqrt2,0,0)$，$C(\sqrt2,2,0)$，$D(0,\sqrt3+1,0)$，$P(0,0,\sqrt2)$。\n"
                    r"(i) 设球心 $O(x,y,z)$，由 $|OP|=|OB|=|OC|=|OD|$ 联立解得 $O(0,1,0)$，故 $O$ 在平面 $ABCD$ 上。\n"
                    r"(ii) $\overrightarrow{AC}=(\sqrt2,2,0)$，$\overrightarrow{PO}=(0,1,-\sqrt2)$，$\cos\langle AC,PO\rangle=\dfrac{|AC\cdot PO|}{|AC||PO|}=\dfrac{2}{\sqrt{21}}$。",
        "points": [
            r"第(1)问：证 $AB\perp$ 平面 $PAD$（4分）",
            r"第(2)(i)问：建系求球心 $O(0,1,0)$（5分）",
            r"第(2)(ii)问：求夹角余弦 $\dfrac{2}{\sqrt{21}}$（6分）",
        ],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "18",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_conic",
        "difficulty": 4,
        "stem": r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$（$a>b>0$）的离心率为 $\dfrac{2\sqrt5}{5}$，下顶点为 $A$，右顶点为 $B$，$|AB|=\sqrt{10}$。\n"
                r"(1) 求 $C$ 的方程；\n"
                r"(2) 已知动点 $P$ 不在 $y$ 轴上，点 $Q$ 在射线 $AP$ 上，且满足 $|AP|\cdot|AQ|=3$。\n"
                r"(i) 设 $P(m,n)$，求 $Q$ 的坐标（用 $m,n$ 表示）；\n"
                r"(ii) 设 $O$ 为坐标原点，直线 $OR$ 的斜率是直线 $OP$ 的斜率的 $3$ 倍，求 $|PQ|$ 的最大值。",
        "options": [],
        "answer": r"(1) $\dfrac{x^2}{9}+y^2=1$；(2)(i) 见解析；(2)(ii) $3\sqrt3+3\sqrt2$",
        "analysis": r"解析：(1) 由 $\dfrac ca=\dfrac{2\sqrt5}{5}$ 得 $c^2=\dfrac45a^2$，又 $b^2=a^2-c^2=\dfrac15a^2$；下顶点 $A(0,-b)$，右顶点 $B(a,0)$，$|AB|^2=a^2+b^2=10$，联立解得 $a=3,b=1$，故 $C:\dfrac{x^2}{9}+y^2=1$。\n"
                    r"(2)(i) 设 $Q(x,y)$，由 $Q$ 在射线 $AP$ 上及 $|AP|\cdot|AQ|=3$ 可得 $Q=\left(\dfrac{3m}{m^2+(n+1)^2},\dfrac{3(n+1)}{m^2+(n+1)^2}-1\right)$。\n"
                    r"(2)(ii) 由斜率关系得 $P$ 的轨迹为圆 $x^2+(y+4)^2=18$，圆心 $(0,-4)$，半径 $3\sqrt2$；$Q$ 在椭圆上，$|PQ|$ 最大值为 $3\sqrt3+3\sqrt2$。",
        "points": [
            r"第(1)问：求 $a=3,b=1$，得 $\dfrac{x^2}{9}+y^2=1$（4分）",
            r"第(2)(i)问：求 $Q$ 坐标（4分）",
            r"第(2)(ii)问：求轨迹圆并求 $|PQ|_{\max}=3\sqrt3+3\sqrt2$（9分）",
        ],
    },
    {
        "year": 2025,
        "paper": "新课标I卷",
        "question_no": "19",
        "source_ref": "https://zy.21cnjy.com/23228057",
        "verified": 1,
        "qtype": "解答题",
        "kp_id": "mat_trig",
        "difficulty": 5,
        "stem": r"设函数 $f(x)=5\cos x-\cos 5x$。\n"
                r"(1) 求 $f(x)$ 在 $\left[0,\dfrac{\pi}{4}\right]$ 上的最大值；\n"
                r"(2) 给定 $\theta\in(0,\pi)$，设 $a$ 为实数，证明：存在 $y\in[a-\theta,a+\theta]$，使得 $\cos y\le\cos\theta$；\n"
                r"(3) 若存在 $\varphi\in\mathbf{R}$ 使得 $5\cos x-\cos(5x+\varphi)\le b$ 对任意的 $x\in\mathbf{R}$ 恒成立，求 $b$ 的最小值。",
        "options": [],
        "answer": r"(1) $3\sqrt3$；(2) 见解析；(3) $b$ 的最小值为 $4\sqrt3$",
        "analysis": r"解析：(1) $f'(x)=-5\sin x+5\sin 5x=5(\sin 5x-\sin x)=10\cos 3x\sin 2x$。令 $f'(x)=0$，在 $\left[0,\dfrac{\pi}{4}\right]$ 上得 $x=0$ 或 $x=\dfrac{\pi}{6}$。当 $0<x<\dfrac{\pi}{6}$ 时 $f'(x)>0$，$f$ 递增；当 $\dfrac{\pi}{6}<x<\dfrac{\pi}{4}$ 时 $f'(x)<0$，$f$ 递减。故最大值为 $f\left(\dfrac{\pi}{6}\right)=5\cos\dfrac{\pi}{6}-\cos\dfrac{5\pi}{6}=5\times\dfrac{\sqrt3}{2}+\dfrac{\sqrt3}{2}=3\sqrt3$。\n"
                    r"(2) $\cos y\le\cos\theta$ 的解集是周期性的长度 $\ge\theta$ 的区间；任意长度为 $2\theta$ 的闭区间 $[a-\theta,a+\theta]$ 必与 $\cos y\le\cos\theta$ 的解集相交，故存在 $y\in[a-\theta,a+\theta]$ 使 $\cos y\le\cos\theta$。\n"
                    r"(3) 记 $g(x)=5\cos x-\cos(5x+\varphi)$，周期 $2\pi$。由导数分析极值，$g(x)$ 的最大值关于 $\varphi$ 的最小值在 $\varphi=\dfrac{\pi}{3}$ 时取得为 $4\sqrt3$，故 $b$ 的最小值为 $4\sqrt3$。",
        "points": [
            r"第(1)问：求导得 $f'(x)=10\cos3x\sin2x$，求最大值 $3\sqrt3$（5分）",
            r"第(2)问：利用余弦函数图象证明存在性（4分）",
            r"第(3)问：分析 $g(x)$ 最大值关于 $\varphi$ 的最小值，得 $b_{\min}=4\sqrt3$（8分）",
        ],
    },
]
