# -*- coding: utf-8 -*-

BANK = {}

# -*- coding: utf-8 -*-
BANK.update({
"mat_set": [
{"qtype":"选择题","difficulty":1,"stem":"已知集合 A={1,2,3}，B={2,3,4}，则 A∩B=（ ）","options":["A. {1}","B. {2,3}","C. {1,2,3,4}","D. {4}"],"answer":"B","analysis":"交集取两集合公共元素，公共元素为 2、3，故选 B。"},
{"qtype":"选择题","difficulty":1,"stem":"全集 U={1,2,3,4,5}，集合 A={1,3,5}，则 ∁UA=（ ）","options":["A. {2,4}","B. {1,3,5}","C. {1,2,3,4,5}","D. ∅"],"answer":"A","analysis":"补集为全集中不属于 A 的元素，即 {2,4}。注意区分∈与⊆。"},
{"qtype":"选择题","difficulty":2,"stem":"集合 A={x|-1<x<3}，B={x|x≥1}，则 A∩B=（ ）","options":["A. {x|1≤x<3}","B. {x|-1<x≤1}","C. {x|x>-1}","D. {x|x<3}"],"answer":"A","analysis":"取两段区间公共部分：x≥1 且 -1<x<3，得 1≤x<3。端点 1 属于 B 应取等号。"},
{"qtype":"选择题","difficulty":2,"stem":"「x>2」是「x^2>4」的（ ）","options":["A. 充分不必要条件","B. 必要不充分条件","C. 充要条件","D. 既不充分也不必要条件"],"answer":"A","analysis":"x>2 可推出 x^2>4；但 x=-3 时 x^2>4 却不满足 x>2，故充分不必要。"},
{"qtype":"选择题","difficulty":2,"stem":"命题「∀x∈R，x^2≥0」的否定是（ ）","options":["A. ∃x∈R，x^2<0","B. ∀x∈R，x^2≤0","C. ∃x∈R，x^2≥0","D. ∀x∈R，x^2<0"],"answer":"A","analysis":"全称命题的否定为特称命题，先改量词再否定结论，≥0 的否定是 <0。"},
{"qtype":"选择题","difficulty":1,"stem":"集合 A={x|x^2-1=0}，下列关系正确的是（ ）","options":["A. 1⊆A","B. 1∈A","C. ∅∈A","D. {1}∈A"],"answer":"B","analysis":"A={-1,1}，1 是 A 的元素应记 1∈A；⊆用于集合间，{1}⊆A 才对。"},
{"qtype":"选择题","difficulty":2,"stem":"M={x|x=2k，k∈Z}，N={x|x=2k+1，k∈Z}，则 M∪N=（ ）","options":["A. Z","B. M","C. N","D. ∅"],"answer":"A","analysis":"M 为偶数集，N 为奇数集，其并集为全体整数集 Z。"},
{"qtype":"选择题","difficulty":3,"stem":"A={x|x<a}，B={x|x<2}，若 A⊆B，则实数 a 的取值范围是（ ）","options":["A. a≤2","B. a<2","C. a≥2","D. a>2"],"answer":"A","analysis":"A⊆B 表示所有小于 a 的数都小于 2，需 a≤2；a=2 时 A=B 仍成立。"},
{"qtype":"填空题","difficulty":1,"stem":"集合 A={x|x^2-3x+2=0}，用列举法表示 A=________。","answer":"{1,2}","analysis":"解方程 x^2-3x+2=(x-1)(x-2)=0，得根 1、2。"},
{"qtype":"填空题","difficulty":2,"stem":"A={1,2}，B={2,3,4}，则 A∪B 的子集个数为________。","answer":"16","analysis":"A∪B={1,2,3,4} 共 4 个元素，子集个数为 2^4=16，注意空集与自身都算子集。"},
{"qtype":"填空题","difficulty":2,"stem":"「x=1」是「x^2-1=0」的________条件（从充分不必要、必要不充分、充要、既不充分也不必要中选填）。","answer":"充分不必要","analysis":"x=1 可推出 x^2-1=0，但 x=-1 也满足后者，故充分不必要。"},
{"qtype":"填空题","difficulty":1,"stem":"命题「∃x∈R，x+1=0」是________命题（填真或假）。","answer":"真","analysis":"取 x=-1 时等式成立，存在性命题为真。"},
{"qtype":"填空题","difficulty":3,"stem":"已知集合 A={x|mx^2-2x+1=0} 恰有两个元素，则实数 m 的取值范围是________。","answer":"m<1 且 m≠0","analysis":"二次方程有两个不等实根需 m≠0 且 Δ=4-4m>0，即 m<1 且 m≠0；m=0 时退化为一次方程只有一个根。"},
{"qtype":"解答题","difficulty":3,"stem":"全集 U=R，A={x|x^2-3x-4≤0}，B={x|2<x≤5}，求 A∩B、A∪B 及 ∁U(A∩B)。","answer":"解：由 x^2-3x-4=(x-4)(x+1)≤0 得 A={x|-1≤x≤4}。A∩B={x|2<x≤4}；A∪B={x|-1≤x≤5}；∁U(A∩B)={x|x≤2 或 x>4}。","analysis":"先解一元二次不等式写出区间，再按交并补定义运算；补集端点不取，注意与 A∩B 端点相反。"},
{"qtype":"解答题","difficulty":4,"stem":"A={x|x^2-ax+a^2-19=0}，B={x|x^2-5x+6=0}，C={x|x^2+2x-8=0}，且 A∩B≠∅，A∩C=∅，求实数 a 的值。","answer":"解：B={2,3}，C={2,-4}。因 A∩C=∅ 且 A∩B≠∅，故 3∈A 而 2∉A。把 x=3 代入得 9-3a+a^2-19=0，即 a^2-3a-10=0，解得 a=5 或 a=-2。检验：a=5 时 A={2,3}，含 2 不合题意；a=-2 时 A={3,-5}，满足 A∩B={3}≠∅ 且 A∩C=∅。故 a=-2。","analysis":"关键是利用 A∩C=∅ 排除元素 2 与 -4，再由 A∩B≠∅ 锁定 3∈A；求出 a 后必须回代检验，避免增根。"}
],
"mat_complex": [
{"qtype":"选择题","difficulty":2,"stem":"复数 z=(1+i)/(1-i)=（ ）","options":["A. 1","B. -1","C. i","D. -i"],"answer":"C","analysis":"分子分母同乘 1+i，(1+i)^2/2=2i/2=i。"},
{"qtype":"选择题","difficulty":1,"stem":"复数 z=3-4i 的共轭复数是（ ）","options":["A. 3+4i","B. -3-4i","C. 4-3i","D. -3+4i"],"answer":"A","analysis":"共轭复数实部不变、虚部取反，即 3+4i。"},
{"qtype":"选择题","difficulty":1,"stem":"复数 z=1+i 的模 |z|=（ ）","options":["A. 1","B. √2","C. 2","D. 4"],"answer":"B","analysis":"|z|=√(1^2+1^2)=√2。"},
{"qtype":"选择题","difficulty":2,"stem":"复数 z=(2+i)i 的虚部为（ ）","options":["A. -1","B. 1","C. 2","D. 2i"],"answer":"C","analysis":"(2+i)i=2i+i^2=-1+2i，虚部是实数 2 而非 2i。"},
{"qtype":"选择题","difficulty":2,"stem":"i^2026=（ ）","options":["A. 1","B. -1","C. i","D. -i"],"answer":"B","analysis":"i 的幂以 4 为周期，2026=4×506+2，故 i^2026=i^2=-1。"},
{"qtype":"选择题","difficulty":3,"stem":"复数 z=(a^2-1)+(a-1)i 为纯虚数，则实数 a=（ ）","options":["A. 1","B. -1","C. ±1","D. 0"],"answer":"B","analysis":"纯虚数要求实部为 0 且虚部不为 0：a^2-1=0 得 a=±1，又 a-1≠0 得 a≠1，故 a=-1。"},
{"qtype":"选择题","difficulty":2,"stem":"复数 z=2/(1-i) 在复平面内对应的点位于（ ）","options":["A. 第一象限","B. 第二象限","C. 第三象限","D. 第四象限"],"answer":"A","analysis":"z=2(1+i)/2=1+i，对应点 (1,1) 在第一象限。"},
{"qtype":"选择题","difficulty":2,"stem":"z1=1+i，z2=2-i，则 z1·z2=（ ）","options":["A. 3+i","B. 3-i","C. 1+i","D. 1+3i"],"answer":"A","analysis":"(1+i)(2-i)=2-i+2i-i^2=3+i。"},
{"qtype":"填空题","difficulty":1,"stem":"复数 (1+i)^2=________。","answer":"2i","analysis":"展开得 1+2i+i^2=2i。"},
{"qtype":"填空题","difficulty":2,"stem":"已知 z=3+4i，则 z·\u0304z=________。","answer":"25","analysis":"z 乘共轭复数等于 |z|^2=3^2+4^2=25。"},
{"qtype":"填空题","difficulty":2,"stem":"复数 (1-i)/(1+i)=________。","answer":"-i","analysis":"分子分母同乘 1-i，(1-i)^2/2=-2i/2=-i。"},
{"qtype":"填空题","difficulty":2,"stem":"复数 z 满足 z·(1+i)=2i，则 z=________。","answer":"1+i","analysis":"z=2i/(1+i)=2i(1-i)/2=i(1-i)=1+i。"},
{"qtype":"填空题","difficulty":3,"stem":"复数 z=2i/(1-i) 的模为________。","answer":"√2","analysis":"|2i/(1-i)|=|2i|/|1-i|=2/√2=√2。"},
{"qtype":"解答题","difficulty":3,"stem":"复数 z=(m^2-m-2)+(m^2-3m+2)i（m∈R）。当 m 为何值时：(1)z 为实数；(2)z 为纯虚数；(3)z 对应点在复平面实轴上。","answer":"解：(1)z 为实数需虚部为 0：m^2-3m+2=(m-1)(m-2)=0，得 m=1 或 m=2。(2)z 为纯虚数需实部为 0 且虚部不为 0：m^2-m-2=(m-2)(m+1)=0 得 m=2 或 m=-1，又 m≠1 且 m≠2，故 m=-1。(3)点在实轴上即虚部为 0，同(1)，m=1 或 m=2。","analysis":"实数看虚部为 0；纯虚数须实部 0 且虚部非 0，两者缺一不可；实轴上的点就是实数点。"},
{"qtype":"解答题","difficulty":3,"stem":"已知复数 z1=1+2i，z2=a-i（a∈R）。(1)若 z1+z2 为纯虚数，求 a；(2)在(1)的条件下求 |z1·z2|。","answer":"解：(1)z1+z2=(1+a)+i，为纯虚数需实部 0，即 1+a=0，得 a=-1。(2)此时 z2=-1-i，z1·z2=(1+2i)(-1-i)=-1-i-2i-2i^2=1-3i，故 |z1·z2|=√(1^2+(-3)^2)=√10。","analysis":"纯虚数要求实部为 0、虚部非 0；乘法按多项式展开并注意 i^2=-1；模用 √(实部^2+虚部^2)。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_eq_sys": [
{"qtype":"选择题","difficulty":1,"stem":"方程组 x+y=5，x-y=1 的解是（ ）","options":["A. x=3，y=2","B. x=2，y=3","C. x=4，y=1","D. x=1，y=4"],"answer":"A","analysis":"两式相加得 2x=6，x=3，代入得 y=2。"},
{"qtype":"选择题","difficulty":1,"stem":"用代入消元法解 y=2x，x+y=9，则 x=（ ）","options":["A. 2","B. 3","C. 4","D. 5"],"answer":"B","analysis":"把 y=2x 代入 x+y=9 得 3x=9，x=3。"},
{"qtype":"选择题","difficulty":2,"stem":"方程组 2x+y=7，x+2y=8 的解满足 x-y=（ ）","options":["A. 1","B. 2","C. 3","D. -1"],"answer":"D","analysis":"两式相减得 (2x+y)-(x+2y)=7-8，即 x-y=-1。"},
{"qtype":"选择题","difficulty":2,"stem":"若 x=2，y=1 是方程 ax-y=3 的解，则 a=（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"代入得 2a-1=3，a=2。"},
{"qtype":"选择题","difficulty":3,"stem":"方程组 x+y=3，y+z=5，x+z=4 的解 x+y+z=（ ）","options":["A. 5","B. 6","C. 7","D. 8"],"answer":"B","analysis":"三式相加得 2(x+y+z)=12，故 x+y+z=6。"},
{"qtype":"选择题","difficulty":2,"stem":"鸡兔同笼，共 35 头、94 脚，设鸡 x 只兔 y 只，方程组正确的是（ ）","options":["A. x+y=35，2x+4y=94","B. x+y=35，4x+2y=94","C. x+y=94，2x+4y=35","D. x+y=35，x+4y=94"],"answer":"A","analysis":"头数 x+y=35，脚数鸡 2 兔 4，即 2x+4y=94。"},
{"qtype":"选择题","difficulty":3,"stem":"关于 x、y 的方程组 2x+3y=k，3x+2y=k+2 的解满足 x+y=4，则 k=（ ）","options":["A. 9","B. 10","C. 11","D. 12"],"answer":"A","analysis":"两式相加得 5(x+y)=2k+2，代入 x+y=4 得 20=2k+2，k=9。"},
{"qtype":"选择题","difficulty":2,"stem":"二元一次方程组 x+y=1，x+y=2 的解的情况是（ ）","options":["A. 唯一解","B. 无数解","C. 无解","D. 无法确定"],"answer":"C","analysis":"两方程左边相同右边不同，矛盾，故无解。"},
{"qtype":"填空题","difficulty":1,"stem":"方程组 3x+2y=12，y=x 的解为 x=________。","answer":"12/5","analysis":"代入得 5x=12，x=12/5。"},
{"qtype":"填空题","difficulty":2,"stem":"若 2x+3y=12 且 x=3y，则 y=________。","answer":"4/3","analysis":"代入得 6y+3y=12，y=4/3。"},
{"qtype":"填空题","difficulty":2,"stem":"方程组 (x/2)+(y/3)=2，x+y=5 的解为 x=________。","answer":"2","analysis":"第一式乘 6 得 3x+2y=12，与 x+y=5 联立，解得 x=2，y=3。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 |x+y-5|+(x-y-1)^2=0，则 x=________。","answer":"3","analysis":"绝对值与平方均非负，同时为 0：x+y=5，x-y=1，解得 x=3。"},
{"qtype":"填空题","difficulty":3,"stem":"若方程组 2x-y=3，4x+ky=6 有无数组解，则 k=________。","answer":"-2","analysis":"两方程成比例时无数解：4/2=6/3=2，故 k/(-1)=2，k=-2。"},
{"qtype":"解答题","difficulty":2,"stem":"用适当方法解方程组：3x+4y=16，5x-6y=33。","answer":"解：第一式乘 3 得 9x+12y=48，第二式乘 2 得 10x-12y=66，相加得 19x=114，x=6；代入第一式 18+4y=16，y=-1/2。故 x=6，y=-1/2。","analysis":"用加减消元，把 y 的系数化为互为相反数再相加；求出一代回原方程。"},
{"qtype":"解答题","difficulty":3,"stem":"某班购买甲、乙两种笔记本共 40 本，甲每本 3 元，乙每本 2 元，共花费 100 元，求甲、乙各买多少本。","answer":"解：设甲 x 本、乙 y 本。由题意 x+y=40，3x+2y=100。第一式乘 2 得 2x+2y=80，两式相减得 x=20，则 y=20。答：甲、乙各买 20 本。","analysis":"列二元方程组，关键是把总数与总价两个等量关系写对；结果需检验合理性。"}
],
"mat_func": [
{"qtype":"选择题","difficulty":1,"stem":"函数 f(x)=1/(x-2) 的定义域是（ ）","options":["A. x≠2","B. x>2","C. x<2","D. x≠-2"],"answer":"A","analysis":"分母不为 0，即 x-2≠0，x≠2。"},
{"qtype":"选择题","difficulty":1,"stem":"f(x)=2x+1，则 f(3)=（ ）","options":["A. 5","B. 6","C. 7","D. 8"],"answer":"C","analysis":"f(3)=2×3+1=7。"},
{"qtype":"选择题","difficulty":2,"stem":"函数 f(x)=x^2-2x 的值域是（ ）","options":["A. [-1,+∞)","B. (-1,+∞)","C. [0,+∞)","D. R"],"answer":"A","analysis":"f(x)=(x-1)^2-1≥-1，最小值 -1。"},
{"qtype":"选择题","difficulty":2,"stem":"下列函数为偶函数的是（ ）","options":["A. f(x)=x^3","B. f(x)=x^2+1","C. f(x)=2x","D. f(x)=x+1"],"answer":"B","analysis":"偶函数满足 f(-x)=f(x)，x^2+1 符合；奇次项为奇函数，一次函数过原点为奇函数。"},
{"qtype":"选择题","difficulty":2,"stem":"函数 f(x)=1/x 在下列区间为减函数的是（ ）","options":["A. (-∞,0)∪(0,+∞)","B. (0,+∞)","C. R","D. (-1,1)"],"answer":"B","analysis":"f(x)=1/x 在每个连续的单调区间 (0,+∞)、(-∞,0) 上分别递减，但不能写成并集。"},
{"qtype":"选择题","difficulty":2,"stem":"f(x) 为奇函数且 f(2)=3，则 f(-2)=（ ）","options":["A. 3","B. -3","C. 0","D. 无法确定"],"answer":"B","analysis":"奇函数满足 f(-x)=-f(x)，f(-2)=-f(2)=-3。"},
{"qtype":"选择题","difficulty":3,"stem":"f(x) 是 R 上的偶函数，且在 [0,+∞) 上单调递增，则（ ）","options":["A. f(-3)<f(1)","B. f(-3)>f(1)","C. f(-3)=f(1)","D. 无法比较"],"answer":"B","analysis":"偶函数 f(-3)=f(3)，又 3>1 且递增，故 f(3)>f(1)，即 f(-3)>f(1)。"},
{"qtype":"选择题","difficulty":3,"stem":"f(x)=x^2+2(a-1)x+2 在区间 (-∞,4] 上单调递减，则 a 的取值范围是（ ）","options":["A. a≤-3","B. a≥-3","C. a≤3","D. a≥3"],"answer":"A","analysis":"开口向上，对称轴 x=1-a，递减区间为 (-∞,1-a]，需 1-a≥4，即 a≤-3。"},
{"qtype":"填空题","difficulty":1,"stem":"函数 f(x)=√(x-3) 的定义域是________。","answer":"x≥3","analysis":"被开方数非负，x-3≥0。"},
{"qtype":"填空题","difficulty":2,"stem":"f(x)=x^2，则 f(x+1)=________。","answer":"(x+1)^2","analysis":"把 x 换成 x+1，得 (x+1)^2=x^2+2x+1。"},
{"qtype":"填空题","difficulty":2,"stem":"f(x)=2x-1，若 f(a)=5，则 a=________。","answer":"3","analysis":"2a-1=5，a=3。"},
{"qtype":"填空题","difficulty":3,"stem":"f(x) 为 R 上的奇函数，当 x>0 时 f(x)=x(1+x)，则 x<0 时 f(x)=________。","answer":"x(1-x)","analysis":"x<0 时 -x>0，f(-x)=(-x)(1-x)，奇函数 f(x)=-f(-x)=x(1-x)。"},
{"qtype":"填空题","difficulty":3,"stem":"f(x) 满足 f(x+2)=f(x)，且 f(1)=2，则 f(5)=________。","answer":"2","analysis":"周期为 2，f(5)=f(1+2×2)=f(1)=2。"},
{"qtype":"解答题","difficulty":3,"stem":"判断 f(x)=x/(x^2+1) 的奇偶性，并求 f(2)+f(-2) 的值。","answer":"解：定义域为 R 关于原点对称。f(-x)=(-x)/((-x)^2+1)=-x/(x^2+1)=-f(x)，故为奇函数。f(2)=2/5，f(-2)=-2/5，所以 f(2)+f(-2)=0。","analysis":"先看定义域是否对称，再用定义比较 f(-x) 与 f(x)；奇函数对任意 x 都有 f(x)+f(-x)=0。"},
{"qtype":"解答题","difficulty":4,"stem":"证明 f(x)=x+1/x 在 (1,+∞) 上单调递增，并比较 f(2) 与 f(3) 的大小。","answer":"解：任取 1<x1<x2，f(x1)-f(x2)=(x1-x2)+(1/x1-1/x2)=(x1-x2)+(x2-x1)/(x1x2)=(x1-x2)(1-1/(x1x2))。因 x1<x2，x1-x2<0；又 x1x2>1，故 1-1/(x1x2)>0，于是 f(x1)-f(x2)<0，即 f(x1)<f(x2)，故递增。因 2<3，所以 f(2)<f(3)。","analysis":"用定义作差，关键把差因式分解成若干因子乘积，逐段判号；得到单调性后直接比较自变量大小。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_exp_log": [
{"qtype":"选择题","difficulty":1,"stem":"2^3·2^2=（ ）","options":["A. 2^5","B. 2^6","C. 4^5","D. 2^1"],"answer":"A","analysis":"同底数幂相乘底数不变指数相加，3+2=5。"},
{"qtype":"选择题","difficulty":1,"stem":"log_2 8=（ ）","options":["A. 2","B. 3","C. 4","D. 8"],"answer":"B","analysis":"2^3=8，故 log_2 8=3。"},
{"qtype":"选择题","difficulty":2,"stem":"log_3 9+log_3 (1/3)=（ ）","options":["A. 1","B. 2","C. 3","D. 0"],"answer":"A","analysis":"log_3 9=2，log_3(1/3)=-1，和为 1。"},
{"qtype":"选择题","difficulty":2,"stem":"函数 f(x)=a^x (a>1) 是（ ）","options":["A. 增函数","B. 减函数","C. 奇函数","D. 偶函数"],"answer":"A","analysis":"底数 a>1 的指数函数在 R 上单调递增，且恒过 (0,1)。"},
{"qtype":"选择题","difficulty":2,"stem":"log_2 x 的定义域是（ ）","options":["A. x>0","B. x≥0","C. x∈R","D. x>1"],"answer":"A","analysis":"对数真数必须大于 0。"},
{"qtype":"选择题","difficulty":2,"stem":"下列各式正确的是（ ）","options":["A. 2^0=0","B. (1/2)^(-1)=2","C. lg 10=0","D. log_2(-1)=1"],"answer":"B","analysis":"(1/2)^(-1)=2；2^0=1，lg 10=1，负数无对数。"},
{"qtype":"选择题","difficulty":3,"stem":"设 a=log_2 3，b=log_2 5，c=log_2 0.5，则（ ）","options":["A. b>a>c","B. a>b>c","C. c>a>b","D. a>c>b"],"answer":"A","analysis":"底数 2>1 对数递增，5>3>0.5，故 b>a>c。"},
{"qtype":"选择题","difficulty":3,"stem":"方程 2^x=8 的解是（ ）","options":["A. x=2","B. x=3","C. x=4","D. x=1/3"],"answer":"B","analysis":"8=2^3，故 x=3。"},
{"qtype":"填空题","difficulty":1,"stem":"3^(-2)=________。","answer":"1/9","analysis":"负指数取倒数，3^(-2)=1/9。"},
{"qtype":"填空题","difficulty":2,"stem":"lg 2+lg 5=________。","answer":"1","analysis":"lg 2+lg 5=lg 10=1。"},
{"qtype":"填空题","difficulty":2,"stem":"log_5 5^3=________。","answer":"3","analysis":"log_a a^n=n。"},
{"qtype":"填空题","difficulty":3,"stem":"函数 y=√(log_2 x) 的定义域是________。","answer":"x≥1","analysis":"需 x>0 且 log_2 x≥0，即 x≥1。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 2^x=3，则 4^x=________。","answer":"9","analysis":"4^x=(2^2)^x=(2^x)^2=9。"},
{"qtype":"解答题","difficulty":3,"stem":"计算：(1)log_2 32-log_2 4；(2)(1/4)^(-1/2)+lg 0.01。","answer":"解：(1)原式=log_2(32/4)=log_2 8=3。(2)(1/4)^(-1/2)=4^(1/2)=2，lg 0.01=lg 10^(-2)=-2，故原式=2+(-2)=0。","analysis":"对数运算先用同底对数加减法则合并，再求值；指数式先化底数再乘方，注意负指数与负对数。"},
{"qtype":"解答题","difficulty":4,"stem":"比较 a=0.3^2，b=2^0.3，c=log_2 0.3 的大小。","answer":"解：0<a=0.3^2=0.09<1；b=2^0.3>2^0=1；c=log_2 0.3<log_2 1=0。故 b>a>c。","analysis":"指数函数值与 1 比较，对数函数值与 0 比较，利用中间值 0 和 1 作桥梁。"}
],
"mat_ineq": [
{"qtype":"选择题","difficulty":1,"stem":"不等式 2x-4>0 的解集是（ ）","options":["A. x>2","B. x<2","C. x>-2","D. x<-2"],"answer":"A","analysis":"移项得 2x>4，x>2。"},
{"qtype":"选择题","difficulty":2,"stem":"不等式 x^2-3x+2<0 的解集是（ ）","options":["A. x<1 或 x>2","B. 1<x<2","C. x<1","D. x>2"],"answer":"B","analysis":"(x-1)(x-2)<0，开口向上取两根之间，1<x<2。"},
{"qtype":"选择题","difficulty":2,"stem":"不等式 |x|<3 的解集是（ ）","options":["A. x<3","B. -3<x<3","C. x>3","D. x<-3 或 x>3"],"answer":"B","analysis":"|x|<a 等价于 -a<x<a。"},
{"qtype":"选择题","difficulty":2,"stem":"若 a>b，则下列一定成立的是（ ）","options":["A. ac>bc","B. a^2>b^2","C. a-c>b-c","D. 1/a<1/b"],"answer":"C","analysis":"不等式两边同减同一个数方向不变；乘负数或取倒数需讨论符号。"},
{"qtype":"选择题","difficulty":3,"stem":"x>0，则 x+1/x 的最小值是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"由均值不等式 x+1/x≥2√(x·1/x)=2，当 x=1 取等。"},
{"qtype":"选择题","difficulty":2,"stem":"不等式 (x-1)/(x+2)≥0 的解集是（ ）","options":["A. x≥1","B. x≥1 或 x<-2","C. x>-2","D. -2<x≤1"],"answer":"B","analysis":"分式不等式等价于 (x-1)(x+2)≥0 且 x≠-2，得 x≥1 或 x<-2。"},
{"qtype":"选择题","difficulty":3,"stem":"x>0，y>0，x+y=4，则 xy 的最大值是（ ）","options":["A. 2","B. 4","C. 8","D. 16"],"answer":"B","analysis":"xy≤((x+y)/2)^2=4，当 x=y=2 取等。"},
{"qtype":"选择题","difficulty":3,"stem":"不等式组 x≥0，y≥0，x+y≤2 表示的平面区域面积是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"该区域是直角边为 2 的直角三角形，面积为 2。"},
{"qtype":"填空题","difficulty":1,"stem":"不等式 -3x>6 的解集是________。","answer":"x<-2","analysis":"两边除以负数 -3，不等号方向改变。"},
{"qtype":"填空题","difficulty":2,"stem":"x^2≥4 的解集是________。","answer":"x≤-2 或 x≥2","analysis":"x^2≥a (a>0) 等价于 |x|≥√a。"},
{"qtype":"填空题","difficulty":2,"stem":"不等式 |2x-1|≤3 的解集是________。","answer":"-1≤x≤2","analysis":"-3≤2x-1≤3，解得 -1≤x≤2。"},
{"qtype":"填空题","difficulty":3,"stem":"x>1，则 x+1/(x-1) 的最小值为________。","answer":"3","analysis":"原式=(x-1)+1/(x-1)+1≥2+1=3，当 x=2 取等。"},
{"qtype":"填空题","difficulty":3,"stem":"不等式 x^2+ax+4<0 的解集为空集，则 a 的取值范围是________。","answer":"-4≤a≤4","analysis":"开口向上恒不小于 0 需 Δ≤0，即 a^2-16≤0。"},
{"qtype":"解答题","difficulty":3,"stem":"解不等式：(1)-x^2+2x+3≥0；(2)(x-2)/(x+1)≤1。","answer":"解：(1)化为 x^2-2x-3≤0，即 (x-3)(x+1)≤0，得 -1≤x≤3。(2)移项通分：(x-2)/(x+1)-1≤0，即 (-3)/(x+1)≤0，需 x+1>0，得 x>-1。","analysis":"二次不等式先化二次项系数为正再求根；分式不等式不能直接去分母，必须移项通分后讨论分母符号。"},
{"qtype":"解答题","difficulty":4,"stem":"某工厂生产甲、乙两种产品，每件甲利润 2 百元，每件乙利润 3 百元，生产一件甲需工时 1、原料 3，生产一件乙需工时 2、原料 2。现有工时 8、原料 12，问各生产多少利润最大？","answer":"解：设甲 x 件、乙 y 件，利润 z=2x+3y。约束 x≥0，y≥0，x+2y≤8，3x+2y≤12。两直线 x+2y=8 与 3x+2y=12 交于 (2,3)。顶点有 (0,0)、(4,0)、(0,4)、(2,3)。代入 z：(4,0) 得 8；(0,4) 得 12；(2,3) 得 13。故生产甲 2 件、乙 3 件时利润最大为 13 百元。","analysis":"线性规划先把目标函数与约束写成不等式组，画出可行域，把各顶点代入目标函数比较，最优解必在顶点处取得。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_trig": [
{"qtype":"选择题","difficulty":1,"stem":"sin 30°=（ ）","options":["A. 1/2","B. √2/2","C. √3/2","D. 1"],"answer":"A","analysis":"特殊角值，sin 30°=1/2。"},
{"qtype":"选择题","difficulty":1,"stem":"cos 60°=（ ）","options":["A. 1/2","B. √2/2","C. √3/2","D. √3"],"answer":"A","analysis":"cos 60°=1/2。"},
{"qtype":"选择题","difficulty":2,"stem":"角 α 终边过点 (3,4)，则 sin α=（ ）","options":["A. 3/5","B. 4/5","C. 3/4","D. 4/3"],"answer":"B","analysis":"r=√(9+16)=5，sin α=y/r=4/5。"},
{"qtype":"选择题","difficulty":2,"stem":"sin α<0 且 cos α>0，则 α 在（ ）","options":["A. 第一象限","B. 第二象限","C. 第三象限","D. 第四象限"],"answer":"D","analysis":"sin<0 在三、四象限，cos>0 在一、四象限，公共为第四象限。"},
{"qtype":"选择题","difficulty":2,"stem":"函数 y=sin x 的最小正周期是（ ）","options":["A. π","B. 2π","C. π/2","D. 4π"],"answer":"B","analysis":"正弦函数最小正周期为 2π。"},
{"qtype":"选择题","difficulty":2,"stem":"tan(π-α)=（ ）","options":["A. tan α","B. -tan α","C. cot α","D. -cot α"],"answer":"B","analysis":"π-α 的诱导公式 tan(π-α)=-tan α。"},
{"qtype":"选择题","difficulty":3,"stem":"y=2sin(3x+π/4) 的最小正周期是（ ）","options":["A. π/3","B. 2π/3","C. 2π","D. 3π"],"answer":"B","analysis":"周期 T=2π/ω=2π/3。"},
{"qtype":"选择题","difficulty":3,"stem":"y=sin x 的最大值与最小值之差是（ ）","options":["A. 0","B. 1","C. 2","D. 4"],"answer":"C","analysis":"最大值 1、最小值 -1，差为 2。"},
{"qtype":"填空题","difficulty":1,"stem":"tan 45°=________。","answer":"1","analysis":"特殊角，tan 45°=1。"},
{"qtype":"填空题","difficulty":2,"stem":"cos(π+α)=________。","answer":"-cos α","analysis":"π+α 的余弦，函数名不变符号看象限。"},
{"qtype":"填空题","difficulty":2,"stem":"sin(π/2-α)=________。","answer":"cos α","analysis":"余角诱导公式。"},
{"qtype":"填空题","difficulty":3,"stem":"函数 y=3sin x 的值域是________。","answer":"[-3,3]","analysis":"sin x∈[-1,1]，乘 3 得 [-3,3]。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 sin α=1/3，α 为第二象限角，则 cos α=________。","answer":"-2√2/3","analysis":"cos α=-√(1-sin^2 α)=-√(8/9)=-2√2/3，第二象限余弦为负。"},
{"qtype":"解答题","difficulty":3,"stem":"已知角 α 终边经过点 P(-4,3)，求 sin α、cos α、tan α 的值。","answer":"解：x=-4，y=3，r=√((-4)^2+3^2)=5。sin α=y/r=3/5，cos α=x/r=-4/5，tan α=y/x=-3/4。","analysis":"利用三角函数定义，先求 r=√(x^2+y^2)，再按定义求值；注意符号由所在象限决定。"},
{"qtype":"解答题","difficulty":4,"stem":"求函数 y=2sin(2x+π/6) 的：(1)最小正周期；(2)最大值及取最大值时 x 的集合；(3)单调递增区间。","answer":"解：(1)T=2π/2=π。(2)当 2x+π/6=π/2+2kπ，即 x=π/6+kπ（k∈Z）时，y 取最大值 2。(3)令 -π/2+2kπ≤2x+π/6≤π/2+2kπ，解得 -π/3+kπ≤x≤π/6+kπ（k∈Z），即递增区间为 [-π/3+kπ,π/6+kπ]。","analysis":"把 2x+π/6 整体看作正弦函数的自变量，套用正弦函数的周期、最值与单调性结论，注意解出 x。"}
],
"mat_trig_id": [
{"qtype":"选择题","difficulty":1,"stem":"sin^2 α+cos^2 α=（ ）","options":["A. 0","B. 1","C. 2","D. tan α"],"answer":"B","analysis":"同角三角函数基本关系恒等式。"},
{"qtype":"选择题","difficulty":2,"stem":"sin 2α=（ ）","options":["A. 2sin α","B. 2cos α","C. 2sin α cos α","D. sin^2 α-cos^2 α"],"answer":"C","analysis":"二倍角正弦公式。"},
{"qtype":"选择题","difficulty":2,"stem":"cos 2α=（ ）","options":["A. 2sin^2 α","B. 2cos^2 α-1","C. sin α+cos α","D. 2sin α cos α"],"answer":"B","analysis":"二倍角余弦三种形式之一，另两种为 cos^2 α-sin^2 α 和 1-2sin^2 α。"},
{"qtype":"选择题","difficulty":2,"stem":"sin(α+β)=（ ）","options":["A. sin α cos β+cos α sin β","B. sin α cos β-cos α sin β","C. cos α cos β-sin α sin β","D. sin α sin β+cos α cos β"],"answer":"A","analysis":"两角和正弦公式。"},
{"qtype":"选择题","difficulty":2,"stem":"sin 15° cos 15°=（ ）","options":["A. 1/4","B. 1/2","C. √3/4","D. √3/2"],"answer":"A","analysis":"sin 15°cos 15°=1/2 sin 30°=1/4。"},
{"qtype":"选择题","difficulty":3,"stem":"已知 sin α=3/5，α∈(π/2,π)，则 sin 2α=（ ）","options":["A. 24/25","B. -24/25","C. 12/25","D. -12/25"],"answer":"B","analysis":"cos α=-4/5，sin 2α=2sin α cos α=2·(3/5)·(-4/5)=-24/25。"},
{"qtype":"选择题","difficulty":3,"stem":"tan 20°+tan 40°+√3 tan 20° tan 40°=（ ）","options":["A. √3","B. 1","C. 0","D. -√3"],"answer":"A","analysis":"由 tan 60°=(tan 20°+tan 40°)/(1-tan 20°tan 40°)=√3，展开得原式=√3。"},
{"qtype":"选择题","difficulty":3,"stem":"化简 sin x+√3 cos x 等于（ ）","options":["A. 2sin(x+π/3)","B. 2sin(x+π/6)","C. 2cos(x+π/3)","D. sin(x+π/3)"],"answer":"A","analysis":"辅助角公式：1 与 √3 的平方和开方为 2，=2sin(x+π/3)。"},
{"qtype":"填空题","difficulty":1,"stem":"tan α=sin α/cos α 的前提是 cos α≠________。","answer":"0","analysis":"分母为 0 时 tan α 无意义。"},
{"qtype":"填空题","difficulty":2,"stem":"cos^2 α-sin^2 α=________。","answer":"cos 2α","analysis":"二倍角余弦的一种形式。"},
{"qtype":"填空题","difficulty":2,"stem":"sin(π/6+α)+sin(π/6-α)=________。","answer":"cos α","analysis":"展开相加，交叉项抵消，得 2·(1/2)cos α=cos α。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 tan α=2，则 tan 2α=________。","answer":"-4/3","analysis":"tan 2α=2tan α/(1-tan^2 α)=4/(1-4)=-4/3。"},
{"qtype":"填空题","difficulty":3,"stem":"2sin^2 15°-1=________。","answer":"-√3/2","analysis":"由 cos 2α=1-2sin^2 α，原式=-cos 30°=-√3/2。"},
{"qtype":"解答题","difficulty":3,"stem":"已知 sin α=5/13，α∈(0,π/2)，求 cos 2α 与 sin(α+π/4)。","answer":"解：cos α=√(1-(25/169))=12/13。cos 2α=1-2sin^2 α=1-50/169=119/169。sin(α+π/4)=sin α cos π/4+cos α sin π/4=(√2/2)(5/13+12/13)=17√2/26。","analysis":"先由同角关系求 cos α，再代二倍角公式与两角和公式；注意 α 在第一象限 cos 取正。"},
{"qtype":"解答题","difficulty":4,"stem":"化简：(1)(sin α+cos α)^2；(2)sin 3α cos α-cos 3α sin α，并求 α=π/6 时的值。","answer":"解：(1)原式=sin^2 α+2sin α cos α+cos^2 α=1+sin 2α。(2)由两角差正弦公式，原式=sin(3α-α)=sin 2α。当 α=π/6 时，原式=sin(π/3)=√3/2。","analysis":"第一题展开后用平方关系与二倍角公式；第二题逆用两角差正弦公式，把整体角合并。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_vector": [
{"qtype":"选择题","difficulty":1,"stem":"下列量中是向量的是（ ）","options":["A. 质量","B. 距离","C. 力","D. 身高"],"answer":"C","analysis":"向量既有大小又有方向，力同时具备大小与方向。"},
{"qtype":"选择题","difficulty":2,"stem":"AB 向量+BC 向量=（ ）","options":["A. AC","B. CA","C. AB","D. BC"],"answer":"A","analysis":"向量加法三角形法则，首尾相接由起点指向终点。"},
{"qtype":"选择题","difficulty":2,"stem":"已知 |a|=2，|b|=3，且 a 与 b 同向，则 |a+b|=（ ）","options":["A. 1","B. 5","C. √13","D. 6"],"answer":"B","analysis":"同向向量相加模直接相加。"},
{"qtype":"选择题","difficulty":2,"stem":"a·b=0 是 a⊥b 的（ ）（a,b 为非零向量）","options":["A. 充分不必要","B. 必要不充分","C. 充要","D. 既不充分也不必要"],"answer":"C","analysis":"非零向量垂直等价于数量积为 0。"},
{"qtype":"选择题","difficulty":2,"stem":"已知 |a|=2，|b|=1，a 与 b 夹角为 60°，则 a·b=（ ）","options":["A. 1","B. 2","C. √3","D. 1/2"],"answer":"A","analysis":"a·b=|a||b|cos 60°=2×1×1/2=1。"},
{"qtype":"选择题","difficulty":3,"stem":"|a|=3，|b|=4，a·b=-6，则 a 与 b 的夹角为（ ）","options":["A. 60°","B. 120°","C. 30°","D. 150°"],"answer":"B","analysis":"cos θ=a·b/(|a||b|)=-6/12=-1/2，夹角 120°。"},
{"qtype":"选择题","difficulty":2,"stem":"下列关于零向量的说法正确的是（ ）","options":["A. 零向量没有方向","B. 零向量方向任意","C. 零向量不能与任意向量平行","D. 零向量模为 1"],"answer":"B","analysis":"零向量模为 0，方向任意，规定与任意向量平行。"},
{"qtype":"选择题","difficulty":3,"stem":"在平行四边形 ABCD 中，AB=a，AD=b，则 AC=（ ）","options":["A. a+b","B. a-b","C. b-a","D. a+2b"],"answer":"A","analysis":"平行四边形法则，对角线 AC=AB+AD=a+b。"},
{"qtype":"填空题","difficulty":1,"stem":"AB 向量-BA 向量=________。","answer":"2AB","analysis":"BA=-AB，故 AB-BA=AB+AB=2AB。"},
{"qtype":"填空题","difficulty":2,"stem":"已知 |a|=5，|b|=3，则 |a-b| 的最大值为________。","answer":"8","analysis":"当 a 与 b 反向时 |a-b| 最大，等于 |a|+|b|=8。"},
{"qtype":"填空题","difficulty":2,"stem":"若 a=(1,2)，b=(x,-1)，且 a∥b，则 x=________。","answer":"-1/2","analysis":"平行对应分量成比例：1·(-1)-2·x=0，得 x=-1/2。"},
{"qtype":"填空题","difficulty":3,"stem":"|a|=2，|b|=3，且 a⊥b，则 (a+b)·(a-b)=________。","answer":"-5","analysis":"展开=|a|^2-|b|^2=4-9=-5。"},
{"qtype":"填空题","difficulty":3,"stem":"单位向量 e 的模 |e|=________。","answer":"1","analysis":"单位向量定义为模长等于 1 的向量。"},
{"qtype":"解答题","difficulty":3,"stem":"已知 |a|=4，|b|=3，a 与 b 的夹角为 120°，求：(1)a·b；(2)(2a-b)·(a+3b)。","answer":"解：(1)a·b=|a||b|cos 120°=4×3×(-1/2)=-6。(2)原式=2|a|^2+6a·b-a·b-3|b|^2=2×16+5×(-6)-3×9=32-30-27=-25。","analysis":"数量积按定义代入，展开多项式时把 a·a 写成 |a|^2，注意夹角是 120° 余弦为负。"},
{"qtype":"解答题","difficulty":4,"stem":"已知 a、b 是两个非零向量，且 |a|=|b|=|a-b|，求 a 与 a+b 的夹角。","answer":"解：设 |a|=|b|=|a-b|=m。由 |a-b|^2=|a|^2+|b|^2-2a·b 得 m^2=2m^2-2a·b，故 a·b=m^2/2。又 |a+b|^2=2m^2+2·(m^2/2)=3m^2，|a+b|=√3 m。cos θ=a·(a+b)/(|a||a+b|)=(m^2+m^2/2)/(m·√3 m)=(3/2)/√3=√3/2，故 θ=30°。","analysis":"把模平方转化为数量积，先求 a·b 与 |a+b|，再用夹角公式；注意向量 a+b 的模用和的平方展开。"}
],
"mat_vector_dec": [
{"qtype":"选择题","difficulty":1,"stem":"已知 a=(1,2)，b=(3,-1)，则 a+b=（ ）","options":["A. (4,1)","B. (4,3)","C. (-2,3)","D. (2,1)"],"answer":"A","analysis":"坐标相加，对应分量分别相加。"},
{"qtype":"选择题","difficulty":2,"stem":"A(1,2)，B(4,6)，则 AB 向量=（ ）","options":["A. (3,4)","B. (-3,-4)","C. (5,8)","D. (3,-4)"],"answer":"A","analysis":"AB=B-A=(4-1,6-2)=(3,4)。"},
{"qtype":"选择题","difficulty":2,"stem":"a=(2,-3)，则 2a=（ ）","options":["A. (4,-6)","B. (2,-6)","C. (4,-3)","D. (-4,6)"],"answer":"A","analysis":"数乘向量各分量乘该数。"},
{"qtype":"选择题","difficulty":2,"stem":"a=(3,4)，则 |a|=（ ）","options":["A. 3","B. 4","C. 5","D. 7"],"answer":"C","analysis":"|a|=√(9+16)=5。"},
{"qtype":"选择题","difficulty":2,"stem":"a=(1,2)，b=(x,4)，若 a∥b，则 x=（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"平行条件 1×4-2×x=0，x=2。"},
{"qtype":"选择题","difficulty":3,"stem":"a=(2,3)，b=(-1,2)，则 a·b=（ ）","options":["A. 4","B. 3","C. -2","D. 8"],"answer":"A","analysis":"数量积=2×(-1)+3×2=4。"},
{"qtype":"选择题","difficulty":3,"stem":"a=(1,√3)，b=(√3,1)，则 a 与 b 的夹角为（ ）","options":["A. 30°","B. 45°","C. 60°","D. 90°"],"answer":"A","analysis":"a·b=2√3，|a|=|b|=2，cos θ=2√3/4=√3/2，夹角 30°。"},
{"qtype":"选择题","difficulty":3,"stem":"点 A(2,1)，B(4,3)，则 AB 中点坐标为（ ）","options":["A. (3,2)","B. (2,2)","C. (3,3)","D. (6,4)"],"answer":"A","analysis":"中点坐标为两端点坐标平均。"},
{"qtype":"填空题","difficulty":1,"stem":"a=(-1,3)，则 -a=________。","answer":"(1,-3)","analysis":"向量取反各分量变号。"},
{"qtype":"填空题","difficulty":2,"stem":"已知 A(1,0)，B(3,2)，则 |AB|=________。","answer":"2√2","analysis":"AB=(2,2)，|AB|=√(4+4)=2√2。"},
{"qtype":"填空题","difficulty":2,"stem":"a=(2,1)，b=(x,-2)，若 a⊥b，则 x=________。","answer":"1","analysis":"垂直条件数量积为 0：2x+1×(-2)=0，x=1。"},
{"qtype":"填空题","difficulty":3,"stem":"把 a=(2,3) 用基底 e1=(1,0)、e2=(0,1) 线性表示为 a=________。","answer":"2e1+3e2","analysis":"标准基底下向量坐标就是分解系数。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 a=(1,2)，b=(-2,y)，若 |a+b|=√5，则 y=________。","answer":"1 或 -3","analysis":"a+b=(-1,2+y)，平方得 1+(2+y)^2=5，解得 y=1 或 y=-3。"},
{"qtype":"解答题","difficulty":3,"stem":"已知 A(1,2)，B(3,-1)，C(5,3)。(1)求 AB 向量与 AC 向量；(2)判断三角形 ABC 是否为直角三角形。","answer":"解：(1)AB=(3-1,-1-2)=(2,-3)，AC=(5-1,3-2)=(4,1)。(2)AB·AC=2×4+(-3)×1=5≠0，不垂直；再看 BC=(2,4)，AB·BC=2×2+(-3)×4=-8≠0，AC·BC=4×2+1×4=12≠0。故没有两边垂直，三角形不是直角三角形。","analysis":"向量用终点减起点；判断直角就是看是否有两边对应的向量数量积为 0，要逐一检查三个内角。"},
{"qtype":"解答题","difficulty":4,"stem":"已知 a=(cos α,sin α)，b=(cos β,sin β)。(1)求证：a⊥b 的充要条件是 α-β=π/2+kπ；(2)若 α=π/3，β=π，求 |a-b|。","answer":"解：(1)a·b=cos α cos β+sin α sin β=cos(α-β)。a⊥b 等价于 a·b=0，即 cos(α-β)=0，故 α-β=π/2+kπ（k∈Z）。(2)a=(1/2,√3/2)，b=(-1,0)，a-b=(3/2,√3/2)，|a-b|=√(9/4+3/4)=√3。","analysis":"单位向量数量积恰为两角差的余弦，垂直转化为余弦为 0；求模先算坐标差再平方开方。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_line_eq": [
{"qtype":"选择题","difficulty":1,"stem":"过点 (1,2) 且斜率为 3 的直线方程为（ ）","options":["A. y-2=3(x-1)","B. y+2=3(x+1)","C. y=3x-1","D. y=3x+2"],"answer":"A","analysis":"点斜式 y-y0=k(x-x0)。"},
{"qtype":"选择题","difficulty":1,"stem":"直线 y=2x-3 在 y 轴上的截距是（ ）","options":["A. 2","B. 3","C. -3","D. -2"],"answer":"C","analysis":"斜截式 y=kx+b 中 b 为 y 轴截距。"},
{"qtype":"选择题","difficulty":2,"stem":"过两点 (0,0)、(2,4) 的直线斜率为（ ）","options":["A. 1","B. 2","C. 1/2","D. -2"],"answer":"B","analysis":"k=(4-0)/(2-0)=2。"},
{"qtype":"选择题","difficulty":2,"stem":"直线 2x+y-4=0 的斜率为（ ）","options":["A. 2","B. -2","C. 1/2","D. 4"],"answer":"B","analysis":"化为 y=-2x+4，斜率为 -2。"},
{"qtype":"选择题","difficulty":2,"stem":"直线 x=1 与直线 y=2 的位置关系是（ ）","options":["A. 平行","B. 垂直","C. 重合","D. 相交但不垂直"],"answer":"B","analysis":"x=1 垂直 x 轴，y=2 平行 x 轴，二者垂直。"},
{"qtype":"选择题","difficulty":2,"stem":"与直线 y=2x+1 平行且过点 (0,0) 的直线是（ ）","options":["A. y=2x","B. y=-1/2 x","C. y=2x+2","D. y=-2x"],"answer":"A","analysis":"平行斜率相同，过原点截距为 0。"},
{"qtype":"选择题","difficulty":3,"stem":"点 (1,1) 到直线 3x+4y-2=0 的距离是（ ）","options":["A. 1/5","B. 1","C. 5","D. 3/5"],"answer":"B","analysis":"d=|3×1+4×1-2|/√(9+16)=5/5=1。"},
{"qtype":"选择题","difficulty":3,"stem":"直线 x-y+1=0 与直线 x+y-3=0 的交点为（ ）","options":["A. (1,2)","B. (2,1)","C. (-1,0)","D. (0,3)"],"answer":"A","analysis":"联立解得 x=1，y=2。"},
{"qtype":"填空题","difficulty":1,"stem":"过点 (0,1)、斜率为 -2 的直线方程为 y=________。","answer":"-2x+1","analysis":"斜截式直接写出。"},
{"qtype":"填空题","difficulty":2,"stem":"直线 3x-4y=12 在 x 轴上的截距为________。","answer":"4","analysis":"令 y=0 得 x=4。"},
{"qtype":"填空题","difficulty":2,"stem":"直线 y=3x+2 与 y=-1/3 x+1 的位置关系是________。","answer":"垂直","analysis":"斜率乘积为 3×(-1/3)=-1，两直线垂直。"},
{"qtype":"填空题","difficulty":3,"stem":"过点 (2,3) 且与直线 2x-y+1=0 平行的直线方程为________。","answer":"2x-y-1=0","analysis":"平行斜率为 2，点斜式化简为 2x-y-1=0。"},
{"qtype":"填空题","difficulty":3,"stem":"已知 A(1,0)、B(3,2)，则 AB 垂直平分线方程为________。","answer":"x+y-4=0","analysis":"AB 中点 (2,1)，AB 斜率 1，垂直平分线斜率 -1，即 y-1=-(x-2)。"},
{"qtype":"解答题","difficulty":3,"stem":"求过点 P(2,3) 且在两坐标轴上截距相等的直线方程。","answer":"解：分两种情况。(1)截距都为 0，直线过原点，斜率 k=3/2，方程为 3x-2y=0。(2)截距不为 0，设 x/a+y/a=1，代入 (2,3) 得 a=5，方程为 x+y-5=0。综上，所求直线为 3x-2y=0 或 x+y-5=0。","analysis":"截距相等要注意截距为 0 与不为 0 两种情况，漏掉过原点的直线是常见错误。"},
{"qtype":"解答题","difficulty":4,"stem":"已知直线 l 过点 P(1,2)，且与两坐标轴围成的三角形面积为 4，求直线 l 的方程。","answer":"解：设 l: y-2=k(x-1)。令 x=0 得 y=2-k；令 y=0 得 x=1-2/k。三角形面积 S=1/2|(2-k)(1-2/k)|=4。化简 |(2-k)^2/k|=8。当 k>0 时 (k-2)^2/k=8，即 k^2-12k+4=0，k=6±4√2；当 k<0 时方程同样成立。验证 k=-2：(2-(-2))^2/(-2)=-8，绝对值 8 成立。故 l 为 y-2=(6+4√2)(x-1)、y-2=(6-4√2)(x-1) 或 y-2=-2(x-1)。","analysis":"设点斜式求两截距，按面积列方程，注意绝对值要分情况讨论，避免漏解。"}
],
"mat_circle_eq": [
{"qtype":"选择题","difficulty":1,"stem":"圆心为 (0,0)、半径为 3 的圆方程是（ ）","options":["A. x^2+y^2=9","B. x^2+y^2=3","C. x^2+y^2=6","D. (x-3)^2+y^2=1"],"answer":"A","analysis":"标准方程 x^2+y^2=r^2。"},
{"qtype":"选择题","difficulty":2,"stem":"圆 (x-1)^2+(y+2)^2=4 的圆心和半径为（ ）","options":["A. (1,-2)，2","B. (-1,2)，2","C. (1,-2)，4","D. (-1,2)，4"],"answer":"A","analysis":"标准式直接读出圆心 (a,b) 与半径 r。"},
{"qtype":"选择题","difficulty":2,"stem":"圆 x^2+y^2-2x+4y=0 的圆心是（ ）","options":["A. (1,-2)","B. (-1,2)","C. (1,2)","D. (-1,-2)"],"answer":"A","analysis":"配方得 (x-1)^2+(y+2)^2=5，圆心 (1,-2)。"},
{"qtype":"选择题","difficulty":2,"stem":"点 P(1,1) 与圆 x^2+y^2=4 的位置关系是（ ）","options":["A. 在圆内","B. 在圆上","C. 在圆外","D. 无法判断"],"answer":"A","analysis":"1+1=2<4，点在圆内。"},
{"qtype":"选择题","difficulty":3,"stem":"直线 y=x 与圆 x^2+y^2=2 的位置关系是（ ）","options":["A. 相交","B. 相切","C. 相离","D. 无法判断"],"answer":"A","analysis":"圆心到直线距离 d=|0|/√2=0<√2，直线过圆心必相交。"},
{"qtype":"选择题","difficulty":3,"stem":"圆 x^2+y^2=1 与圆 (x-3)^2+y^2=4 的位置关系是（ ）","options":["A. 外切","B. 内切","C. 相交","D. 外离"],"answer":"A","analysis":"圆心距 3，半径和 1+2=3，等于圆心距，外切。"},
{"qtype":"选择题","difficulty":3,"stem":"过原点且圆心在 (1,0) 的圆方程为（ ）","options":["A. (x-1)^2+y^2=1","B. (x-1)^2+y^2=2","C. x^2+(y-1)^2=1","D. (x+1)^2+y^2=1"],"answer":"A","analysis":"半径=圆心到原点距离=1。"},
{"qtype":"选择题","difficulty":3,"stem":"圆 x^2+y^2=4 上一点 P(1,√3) 处的切线方程为（ ）","options":["A. x+√3 y=4","B. x+√3 y=2","C. x-√3 y=4","D. √3 x+y=4"],"answer":"A","analysis":"切点处切线 xx0+yy0=r^2，即 x+√3 y=4。"},
{"qtype":"填空题","difficulty":1,"stem":"圆 x^2+y^2=16 的半径为________。","answer":"4","analysis":"r^2=16，r=4。"},
{"qtype":"填空题","difficulty":2,"stem":"圆 (x+2)^2+(y-3)^2=9 的圆心坐标为________。","answer":"(-2,3)","analysis":"标准式读出。"},
{"qtype":"填空题","difficulty":2,"stem":"圆 x^2+y^2-4x=0 的半径为________。","answer":"2","analysis":"配方 (x-2)^2+y^2=4，r=2。"},
{"qtype":"填空题","difficulty":3,"stem":"圆心为 (1,1) 且过点 (2,3) 的圆方程为________。","answer":"(x-1)^2+(y-1)^2=5","analysis":"半径平方=(2-1)^2+(3-1)^2=5。"},
{"qtype":"填空题","difficulty":3,"stem":"直线 x+y+b=0 与圆 x^2+y^2=2 相切，则 b=________。","answer":"±2","analysis":"圆心到直线距离 |b|/√2=√2，得 b=±2。"},
{"qtype":"解答题","difficulty":3,"stem":"求过三点 O(0,0)、A(1,1)、B(4,2) 的圆的方程，并指出圆心与半径。","answer":"解：设圆方程 x^2+y^2+Dx+Ey+F=0。代入 O 得 F=0；代入 A 得 1+1+D+E=0，即 D+E=-2；代入 B 得 16+4+4D+2E=0，即 2D+E=-10。两式相减得 D=-8，E=6。圆方程为 x^2+y^2-8x+6y=0，配方 (x-4)^2+(y+3)^2=25，圆心 (4,-3)，半径 5。","analysis":"用一般式列三元方程组，解出 D、E、F 再配方成标准式，便于读圆心和半径。"},
{"qtype":"解答题","difficulty":4,"stem":"已知圆 C: x^2+y^2-4x-5=0，点 P(1,2)。(1)求过点 P 的最短弦所在直线方程；(2)求过圆上点 Q(5,2) 的切线方程。","answer":"解：圆 C 配方为 (x-2)^2+y^2=9，圆心 C(2,0)，半径 3。(1)P 到圆心距离 √((1-2)^2+(2-0)^2)=√5<3，P 在圆内。过 P 的弦中最短弦与 CP 垂直。CP 斜率=(2-0)/(1-2)=-2，故所求直线斜率为 1/2，方程 y-2=(1/2)(x-1)，即 x-2y+3=0。(2)Q(5,2) 在圆上，CQ 斜率=(2-0)/(5-2)=2/3，切线斜率为 -3/2，切线方程 y-2=(-3/2)(x-5)，即 3x+2y-19=0。","analysis":"过圆内定点的最短弦与该点和圆心连线垂直；过圆上一点的切线与该点和半径垂直，用点斜式写出。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_solid": [
{"qtype":"选择题","difficulty":1,"stem":"正方体有（ ）条棱","options":["A. 6","B. 8","C. 12","D. 10"],"answer":"C","analysis":"正方体 12 条棱、6 个面、8 个顶点。"},
{"qtype":"选择题","difficulty":1,"stem":"圆柱的侧面展开图是（ ）","options":["A. 圆","B. 长方形","C. 扇形","D. 梯形"],"answer":"B","analysis":"圆柱侧面沿母线展开为长方形。"},
{"qtype":"选择题","difficulty":2,"stem":"长方体长、宽、高分别为 3、2、1，则其体积为（ ）","options":["A. 6","B. 12","C. 18","D. 24"],"answer":"A","analysis":"体积=长×宽×高=6。"},
{"qtype":"选择题","difficulty":2,"stem":"球的半径为 1，则其表面积为（ ）","options":["A. 4π","B. 2π","C. 4π/3","D. π"],"answer":"A","analysis":"球表面积 S=4πr^2=4π。"},
{"qtype":"选择题","difficulty":2,"stem":"圆锥底面半径为 1，高为 √3，则其母线长为（ ）","options":["A. 1","B. 2","C. 3","D. √3"],"answer":"B","analysis":"母线 l=√(r^2+h^2)=√(1+3)=2。"},
{"qtype":"选择题","difficulty":3,"stem":"下列命题正确的是（ ）","options":["A. 平行于同一平面的两条直线平行","B. 垂直于同一平面的两条直线平行","C. 垂直于同一直线的两条直线平行","D. 平行于同一直线的两个平面平行"],"answer":"B","analysis":"垂直于同一平面的两直线平行是线面垂直性质；其余命题在空间中均不成立。"},
{"qtype":"选择题","difficulty":3,"stem":"正方体 ABCD-A1B1C1D1 中，直线 AA1 与平面 ABCD 的位置关系是（ ）","options":["A. 平行","B. 垂直","C. 在平面内","D. 斜交"],"answer":"B","analysis":"侧棱 AA1 垂直于底面 ABCD。"},
{"qtype":"选择题","difficulty":3,"stem":"一个棱锥被平行于底面的平面所截，截面面积与底面面积之比为 1:4，则截得的小棱锥与原棱锥体积之比为（ ）","options":["A. 1:2","B. 1:4","C. 1:8","D. 1:16"],"answer":"C","analysis":"面积比=相似比平方=1:4，相似比=1:2，体积比=相似比立方=1:8。"},
{"qtype":"填空题","difficulty":1,"stem":"圆柱底面半径为 1，高为 2，则其体积为________。","answer":"2π","analysis":"V=πr^2h=π×1×2=2π。"},
{"qtype":"填空题","difficulty":2,"stem":"球的体积为 32π/3，则其半径为________。","answer":"2","analysis":"V=4/3 πr^3=32π/3，得 r^3=8，r=2。"},
{"qtype":"填空题","difficulty":2,"stem":"正三棱锥底面边长为 2，侧棱长为 2，则其斜高为________。","answer":"√3","analysis":"侧面为正三角形，斜高即正三角形高 √3。"},
{"qtype":"填空题","difficulty":3,"stem":"圆柱与圆锥底面积相等，体积也相等，则圆柱高与圆锥高之比为________。","answer":"1:3","analysis":"πr^2h_柱=(1/3)πr^2h_锥，得 h_柱:h_锥=1:3。"},
{"qtype":"填空题","difficulty":3,"stem":"正方体棱长为 a，则其外接球半径为________。","answer":"√3 a/2","analysis":"外接球直径=体对角线 √3 a。"},
{"qtype":"解答题","difficulty":3,"stem":"已知正四棱锥底面边长为 2，侧棱长为 √3，求它的表面积与体积。","answer":"解：底面正方形面积为 4。底面中心到顶点距离为 √2，斜高=√((√3)^2-(√2)^2/2)=√(3-1)=√2。每个侧面为等腰三角形，面积=1/2×2×√2=√2，四个侧面共 4√2，表面积=4+4√2。高 h=√((√3)^2-(√2)^2)=1。体积=1/3×底面积×高=1/3×4×1=4/3。","analysis":"正棱锥问题要抓住高、斜高、底面外接圆半径构成的直角三角形；体积别忘了乘 1/3。"},
{"qtype":"解答题","difficulty":4,"stem":"正方体 ABCD-A1B1C1D1 棱长为 2，E 为棱 CC1 的中点。(1)求证：BD⊥平面 ACC1A1；(2)求三棱锥 E-ABD 的体积。","answer":"解：(1)正方体中 BD⊥AC（正方形对角线互相垂直），又 AA1⊥底面，故 AA1⊥BD。AC 与 AA1 相交于 A，所以 BD⊥平面 ACC1A1。(2)E 到底面 ABD 的距离即 E 到底面距离，E 是 CC1 中点，底面 z=0，C1 高 2，E 高 1。三角形 ABD 面积=1/2×2×2=2。V=1/3×S×h=1/3×2×1=2/3。","analysis":"线面垂直证明用线线垂直即两条相交直线都垂直；求棱锥体积先找顶点到底面的高，再用 V=1/3Sh。"}
],
"mat_seq": [
{"qtype":"选择题","difficulty":1,"stem":"数列 2,4,6,8,… 的一个通项公式是（ ）","options":["A. a_n=2n","B. a_n=n+1","C. a_n=2n+1","D. a_n=n^2"],"answer":"A","analysis":"偶数数列，a_n=2n。"},
{"qtype":"选择题","difficulty":1,"stem":"等差数列 1,3,5,7,… 的公差是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"相邻两项差为 2。"},
{"qtype":"选择题","difficulty":2,"stem":"等差数列 a1=2，d=3，则 a5=（ ）","options":["A. 11","B. 14","C. 15","D. 17"],"answer":"B","analysis":"a5=2+4×3=14。"},
{"qtype":"选择题","difficulty":2,"stem":"等比数列 1,2,4,8,… 的公比是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"后项与前项之比为 2。"},
{"qtype":"选择题","difficulty":2,"stem":"等比数列 a1=1，q=2，则 a4=（ ）","options":["A. 4","B. 8","C. 16","D. 32"],"answer":"B","analysis":"a4=1×2^3=8。"},
{"qtype":"选择题","difficulty":2,"stem":"等差数列 1,2,3,…,100 的前 100 项和为（ ）","options":["A. 4950","B. 5000","C. 5050","D. 5100"],"answer":"C","analysis":"S_100=100(1+100)/2=5050。"},
{"qtype":"选择题","difficulty":3,"stem":"等比数列 1,2,4,… 的前 n 项和 S_n=（ ）","options":["A. 2^n-1","B. 2^n","C. 2^(n-1)","D. 2^(n+1)-1"],"answer":"A","analysis":"S_n=(1-2^n)/(1-2)=2^n-1。"},
{"qtype":"选择题","difficulty":3,"stem":"等差数列中 a3=5，a7=13，则 a10=（ ）","options":["A. 16","B. 17","C. 19","D. 21"],"answer":"C","analysis":"d=(13-5)/(7-3)=2，a10=a7+3d=13+6=19。"},
{"qtype":"填空题","difficulty":1,"stem":"数列 1,4,9,16,… 的一个通项公式为 a_n=________。","answer":"n^2","analysis":"平方数数列。"},
{"qtype":"填空题","difficulty":2,"stem":"等差数列 a1=3，d=-2，则 a10=________。","answer":"-15","analysis":"a10=3+9×(-2)=-15。"},
{"qtype":"填空题","difficulty":2,"stem":"等比数列 a2=6，a3=18，则 q=________。","answer":"3","analysis":"q=a3/a2=3。"},
{"qtype":"填空题","difficulty":3,"stem":"等差数列前 n 项和 S_n=n^2+2n，则 a_n=________。","answer":"2n+1","analysis":"a_n=S_n-S_{n-1}=n^2+2n-((n-1)^2+2(n-1))=2n+1。"},
{"qtype":"填空题","difficulty":3,"stem":"在 2 与 8 之间插入一个数使三者成等比数列，该数为________。","answer":"±4","analysis":"中间项平方=2×8=16，中间项=±4。"},
{"qtype":"解答题","difficulty":3,"stem":"已知等差数列 a_n 中，a2=3，a5=9。(1)求通项 a_n；(2)求前 n 项和 S_n。","answer":"解：(1)d=(a5-a2)/(5-2)=(9-3)/3=2，a1=a2-d=1，故 a_n=1+(n-1)×2=2n-1。(2)S_n=n(a1+a_n)/2=n(1+2n-1)/2=n^2。","analysis":"先由两项差除以项数差求公差，再求首项；求和用首项加末项乘项数除以 2。"},
{"qtype":"解答题","difficulty":4,"stem":"已知等比数列 a_n 各项均为正数，a2=2，a4=8。(1)求 a_n；(2)若 b_n=log_2 a_n，求数列 b_n 的前 n 项和 T_n。","answer":"解：(1)q^2=a4/a2=4，各项为正故 q=2，a1=a2/q=1，a_n=2^(n-1)。(2)b_n=log_2 2^(n-1)=n-1，b_n 是首项 0、公差 1 的等差数列，T_n=n(0+n-1)/2=n(n-1)/2。","analysis":"等比数列先求公比注意各项为正取正根；取对数后指数变系数，化为等差数列再求和。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_count": [
{"qtype":"选择题","difficulty":1,"stem":"从甲地到乙地有 3 条路，从乙地到丙地有 2 条路，则从甲经乙到丙共有（ ）种走法","options":["A. 5","B. 6","C. 9","D. 8"],"answer":"B","analysis":"分步乘法，3×2=6。"},
{"qtype":"选择题","difficulty":1,"stem":"从 5 人中选 2 人排队，共有（ ）种排法","options":["A. 10","B. 20","C. 25","D. 32"],"answer":"B","analysis":"排列 A(5,2)=5×4=20。"},
{"qtype":"选择题","difficulty":2,"stem":"C(6,2)=（ ）","options":["A. 12","B. 15","C. 30","D. 36"],"answer":"B","analysis":"C(6,2)=6×5/(2×1)=15。"},
{"qtype":"选择题","difficulty":2,"stem":"从 4 男 3 女中选 3 人，要求男女都有，共有（ ）种选法","options":["A. 30","B. 31","C. 34","D. 35"],"answer":"A","analysis":"男女都有=总选法-全男-全女=C(7,3)-C(4,3)-C(3,3)=35-4-1=30。"},
{"qtype":"选择题","difficulty":2,"stem":"(x+1)^4 展开式中 x^2 的系数是（ ）","options":["A. 4","B. 6","C. 8","D. 12"],"answer":"B","analysis":"C(4,2)=6。"},
{"qtype":"选择题","difficulty":3,"stem":"(2x-1)^5 展开式中 x^3 的系数是（ ）","options":["A. 80","B. -80","C. 40","D. -40"],"answer":"A","analysis":"通项 C(5,k)(2x)^(5-k)(-1)^k，x^3 对应 5-k=3，k=2，系数=C(5,2)×2^3×(-1)^2=10×8=80。"},
{"qtype":"选择题","difficulty":3,"stem":"5 人站成一排，甲乙两人必须相邻，共有（ ）种排法","options":["A. 48","B. 72","C. 96","D. 120"],"answer":"A","analysis":"捆绑法：甲乙看作一人共 4 个元素全排列，甲乙内部再排，A(4,4)×A(2,2)=24×2=48。"},
{"qtype":"选择题","difficulty":3,"stem":"(1+x)^n 展开式所有二项式系数和为 64，则 n=（ ）","options":["A. 4","B. 5","C. 6","D. 7"],"answer":"C","analysis":"系数和为 2^n=64，n=6。"},
{"qtype":"填空题","difficulty":1,"stem":"A(4,2)=________。","answer":"12","analysis":"A(4,2)=4×3=12。"},
{"qtype":"填空题","difficulty":2,"stem":"(a+b)^5 展开式共有________项。","answer":"6","analysis":"n 次二项式展开共 n+1 项。"},
{"qtype":"填空题","difficulty":2,"stem":"从 10 件产品中抽 3 件，共有________种抽法。","answer":"120","analysis":"C(10,3)=120。"},
{"qtype":"填空题","difficulty":3,"stem":"(x+2)^6 展开式的常数项为________。","answer":"64","analysis":"常数项即 x^0 项，对应 k=6，C(6,6)×2^6=64。"},
{"qtype":"填空题","difficulty":3,"stem":"5 人站成一排，甲乙不相邻的排法有________种。","answer":"72","analysis":"先排其余 3 人 A(3,3)，再把甲乙插入 4 个空 A(4,2)=12，共 6×12=72。"},
{"qtype":"解答题","difficulty":3,"stem":"用 0,1,2,3,4 这五个数字可以组成多少个没有重复数字的三位偶数？","answer":"解：分个位为 0 与个位为 2 或 4 两类。(1)个位为 0：百位有 4 种、十位有 3 种，共 4×3=12 个。(2)个位为 2 或 4：个位 2 种，百位不能为 0 有 3 种，十位有 3 种，共 2×3×3=18 个。合计 12+18=30 个。","analysis":"数字排列要优先考虑 0 不能在首位和偶数个位必须是偶数这两个限制，分类讨论避免重复遗漏。"},
{"qtype":"解答题","difficulty":4,"stem":"求 (x-1/(2x))^6 展开式中的常数项。","answer":"解：通项 T_{k+1}=C(6,k)x^(6-k)·(-1/(2x))^k=C(6,k)(-1/2)^k x^(6-2k)。令 6-2k=0，得 k=3。常数项=C(6,3)(-1/2)^3=20×(-1/8)=-5/2。","analysis":"写出通项令 x 的指数为 0 解出 k，再代回计算系数，注意负号和分数系数。"}
],
"mat_prob": [
{"qtype":"选择题","difficulty":1,"stem":"掷一枚均匀骰子，出现点数为 3 的概率是（ ）","options":["A. 1/2","B. 1/3","C. 1/6","D. 1"],"answer":"C","analysis":"6 个等可能结果中只有 1 个。"},
{"qtype":"选择题","difficulty":1,"stem":"掷一枚硬币两次，两次都是正面的概率是（ ）","options":["A. 1/2","B. 1/4","C. 1/3","D. 3/4"],"answer":"B","analysis":"共 4 种等可能结果，只有 1 种。"},
{"qtype":"选择题","difficulty":2,"stem":"袋中有 3 红 2 白共 5 球，任取一球为红球的概率是（ ）","options":["A. 2/5","B. 3/5","C. 1/2","D. 3/10"],"answer":"B","analysis":"古典概型，3/5。"},
{"qtype":"选择题","difficulty":2,"stem":"A、B 互斥，P(A)=0.3，P(B)=0.4，则 P(A∪B)=（ ）","options":["A. 0.12","B. 0.7","C. 0.1","D. 0.5"],"answer":"B","analysis":"互斥事件概率可加。"},
{"qtype":"选择题","difficulty":2,"stem":"A、B 独立，P(A)=0.5，P(B)=0.4，则 P(AB)=（ ）","options":["A. 0.9","B. 0.2","C. 0.1","D. 0.5"],"answer":"B","analysis":"独立事件同时发生概率相乘。"},
{"qtype":"选择题","difficulty":3,"stem":"掷两枚骰子，点数和为 7 的概率是（ ）","options":["A. 1/6","B. 1/9","C. 5/36","D. 7/36"],"answer":"A","analysis":"和为 7 的情况有 (1,6)(2,5)(3,4)(4,3)(5,2)(6,1) 共 6 种，6/36=1/6。"},
{"qtype":"选择题","difficulty":3,"stem":"已知 P(A)=0.6，P(B|A)=0.5，则 P(AB)=（ ）","options":["A. 0.3","B. 0.1","C. 0.55","D. 0.6"],"answer":"A","analysis":"P(AB)=P(A)P(B|A)=0.6×0.5=0.3。"},
{"qtype":"选择题","difficulty":3,"stem":"某射手每次命中概率 0.8，独立射击 3 次，恰好命中 2 次的概率是（ ）","options":["A. 0.384","B. 0.512","C. 0.256","D. 0.128"],"answer":"A","analysis":"C(3,2)×0.8^2×0.2=3×0.64×0.2=0.384。"},
{"qtype":"填空题","difficulty":1,"stem":"掷一枚均匀硬币，出现反面的概率为________。","answer":"1/2","analysis":"两种等可能结果。"},
{"qtype":"填空题","difficulty":2,"stem":"100 件产品中有 5 件次品，任取一件为次品的概率是________。","answer":"1/20","analysis":"5/100=1/20。"},
{"qtype":"填空题","difficulty":2,"stem":"A、B 对立，P(A)=0.7，则 P(B)=________。","answer":"0.3","analysis":"对立事件概率和为 1。"},
{"qtype":"填空题","difficulty":3,"stem":"从 1,2,3,4,5 中任取两个不同数，其和为偶数的概率是________。","answer":"2/5","analysis":"共 C(5,2)=10 种，和为偶数需两奇或两偶：C(3,2)+C(2,2)=3+1=4，概率 4/10=2/5。"},
{"qtype":"填空题","difficulty":3,"stem":"甲乙独立解题，甲解出概率 1/2，乙解出概率 1/3，则恰有一人解出的概率为________。","answer":"1/2","analysis":"P=1/2×2/3+1/2×1/3=1/3+1/6=1/2。"},
{"qtype":"解答题","difficulty":3,"stem":"袋中有 3 个红球、2 个白球，从中不放回地依次取 2 个球。求：(1)两个都是红球的概率；(2)取出的两球颜色相同的概率。","answer":"解：(1)共 C(5,2)=10 种取法，两红有 C(3,2)=3 种，概率 3/10。(2)两色相同=两红+两白，两白有 C(2,2)=1 种，共 4 种，概率 4/10=2/5。","analysis":"用组合数算等可能结果数，颜色相同要把两红和两白两种互斥情形相加。"},
{"qtype":"解答题","difficulty":4,"stem":"甲乙两人独立破译一份密码，甲破译成功概率 1/3，乙破译成功概率 1/4。求：(1)两人都破译成功的概率；(2)密码被破译（至少一人成功）的概率；(3)恰有一人破译成功的概率。","answer":"解：(1)P(都成功)=1/3×1/4=1/12。(2)P(被破译)=1-P(都失败)=1-(2/3)(3/4)=1-1/2=1/2。(3)P(恰一人)=1/3×3/4+2/3×1/4=1/4+1/6=5/12。","analysis":"独立事件同时发生概率相乘；至少一人成功用对立事件更简单；恰有一人分甲成乙败、甲败乙成两类相加。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_stat2": [
{"qtype":"选择题","difficulty":1,"stem":"数据 1,2,3,4,5 的平均数是（ ）","options":["A. 2","B. 3","C. 4","D. 5"],"answer":"B","analysis":"平均数=(1+2+3+4+5)/5=3。"},
{"qtype":"选择题","difficulty":1,"stem":"数据 2,3,3,4,5 的众数是（ ）","options":["A. 2","B. 3","C. 4","D. 5"],"answer":"B","analysis":"出现次数最多的是 3。"},
{"qtype":"选择题","difficulty":2,"stem":"数据 1,2,3,4,5 的中位数是（ ）","options":["A. 2","B. 3","C. 4","D. 3.5"],"answer":"B","analysis":"按顺序排列后中间的数是 3。"},
{"qtype":"选择题","difficulty":2,"stem":"数据 1,2,3 的方差是（ ）","options":["A. 2/3","B. 1","C. 2","D. 0"],"answer":"A","analysis":"均值 2，方差=((1-2)^2+(2-2)^2+(3-2)^2)/3=2/3。"},
{"qtype":"选择题","difficulty":2,"stem":"茎叶图中数据 1,2,3 的标准差为（ ）","options":["A. 2/3","B. √(2/3)","C. √2","D. 1"],"answer":"B","analysis":"标准差是方差的算术平方根。"},
{"qtype":"选择题","difficulty":3,"stem":"若数据 x_1,…,x_n 的平均数为 x̄，方差为 s^2，则数据 2x_i+1 的方差为（ ）","options":["A. 2s^2","B. 2s^2+1","C. 4s^2","D. 4s^2+1"],"answer":"C","analysis":"线性变换 y=ax+b 后方差变为 a^2s^2，常数不影响方差。"},
{"qtype":"选择题","difficulty":3,"stem":"在回归分析中，相关系数 r 的取值范围是（ ）","options":["A. [0,1]","B. [-1,1]","C. [-1,0]","D. R"],"answer":"B","analysis":"相关系数范围为 [-1,1]，绝对值越接近 1 线性相关越强。"},
{"qtype":"选择题","difficulty":3,"stem":"回归直线方程 y=bx+a 必过点（ ）","options":["A. (0,0)","B. (x̄,0)","C. (0,ȳ)","D. (x̄,ȳ)"],"answer":"D","analysis":"回归直线一定过样本中心点 (x̄,ȳ)。"},
{"qtype":"填空题","difficulty":1,"stem":"数据 5,5,5,5 的方差为________。","answer":"0","analysis":"所有数据相同，没有波动。"},
{"qtype":"填空题","difficulty":2,"stem":"数据 3,4,5 的平均数是________。","answer":"4","analysis":"(3+4+5)/3=4。"},
{"qtype":"填空题","difficulty":2,"stem":"样本 1,2,3,4,5 的极差为________。","answer":"4","analysis":"极差=最大值-最小值=5-1=4。"},
{"qtype":"填空题","difficulty":3,"stem":"若一组数据方差为 3，则每个数据都乘以 2 后，新方差为________。","answer":"12","analysis":"乘以 2 后方差乘以 4，3×4=12。"},
{"qtype":"填空题","difficulty":3,"stem":"已知回归直线斜率为 2，样本中心点为 (1,3)，则截距为________。","answer":"1","analysis":"代入 (1,3)：3=2×1+a，a=1。"},
{"qtype":"解答题","difficulty":3,"stem":"某班 5 名同学数学成绩为 80,85,90,95,100，求：(1)平均分；(2)方差。","answer":"解：(1)x̄=(80+85+90+95+100)/5=90。(2)s^2=((80-90)^2+(85-90)^2+(90-90)^2+(95-90)^2+(100-90)^2)/5=(100+25+0+25+100)/5=50。","analysis":"先算平均数再算方差，方差是各数据与平均数差的平方的平均。"},
{"qtype":"解答题","difficulty":4,"stem":"已知 x 与 y 的 4 组数据为 (1,2)、(2,3)、(3,5)、(4,6)。(1)求 x̄ 与 ȳ；(2)若 b=1.4，求回归直线方程 y=bx+a；(3)预测 x=5 时 y 的值。","answer":"解：(1)x̄=(1+2+3+4)/4=2.5，ȳ=(2+3+5+6)/4=4。(2)a=ȳ-bx̄=4-1.4×2.5=4-3.5=0.5，回归直线为 y=1.4x+0.5。(3)x=5 时 y=1.4×5+0.5=7.5。","analysis":"先求样本中心点，再用中心点求截距 a；回归方程用于预测时把 x 代回即可。"}
],
"mat_conic": [
{"qtype":"选择题","difficulty":1,"stem":"椭圆 x^2/25+y^2/9=1 的焦点在（ ）","options":["A. x 轴上","B. y 轴上","C. 原点","D. 无法判断"],"answer":"A","analysis":"x^2 分母大，焦点在 x 轴。"},
{"qtype":"选择题","difficulty":2,"stem":"椭圆 x^2/25+y^2/16=1 中，a=（ ）","options":["A. 5","B. 4","C. 3","D. 25"],"answer":"A","analysis":"标准式 x^2/a^2+y^2/b^2=1，a^2=25，a=5。"},
{"qtype":"选择题","difficulty":2,"stem":"椭圆 x^2/25+y^2/9=1 的焦距为（ ）","options":["A. 4","B. 6","C. 8","D. 10"],"answer":"C","analysis":"c^2=25-9=16，c=4，焦距 2c=8。"},
{"qtype":"选择题","difficulty":2,"stem":"椭圆 x^2/25+y^2/16=1 的离心率为（ ）","options":["A. 3/5","B. 4/5","C. 3/4","D. 5/4"],"answer":"A","analysis":"c=3，e=c/a=3/5。"},
{"qtype":"选择题","difficulty":2,"stem":"双曲线 x^2/9-y^2/16=1 的渐近线方程为（ ）","options":["A. y=±4/3 x","B. y=±3/4 x","C. y=±3x","D. y=±4x"],"answer":"A","analysis":"x^2/a^2-y^2/b^2=1 的渐近线 y=±(b/a)x=±4/3 x。"},
{"qtype":"选择题","difficulty":3,"stem":"双曲线 x^2/16-y^2/9=1 的离心率为（ ）","options":["A. 5/4","B. 4/5","C. 3/4","D. 4/3"],"answer":"A","analysis":"c^2=16+9=25，c=5，e=c/a=5/4。"},
{"qtype":"选择题","difficulty":3,"stem":"椭圆两焦点为 (-3,0)、(3,0)，且过点 (0,4)，则椭圆方程为（ ）","options":["A. x^2/25+y^2/16=1","B. x^2/16+y^2/25=1","C. x^2/25+y^2/9=1","D. x^2/9+y^2/16=1"],"answer":"A","analysis":"c=3，点 (0,4) 在椭圆上得 b=4，a^2=b^2+c^2=25。"},
{"qtype":"选择题","difficulty":3,"stem":"双曲线 x^2/m-y^2/4=1 的离心率为 √3，则 m=（ ）","options":["A. 2","B. 4","C. 8","D. 16"],"answer":"A","analysis":"c^2=m+4，e^2=(m+4)/m=3，解得 m+4=3m，m=2。"},
{"qtype":"填空题","difficulty":1,"stem":"椭圆 x^2/4+y^2/3=1 的长轴长为________。","answer":"4","analysis":"a=2，长轴长 2a=4。"},
{"qtype":"填空题","difficulty":2,"stem":"椭圆 x^2/9+y^2/25=1 的焦点坐标为________。","answer":"(0,±4)","analysis":"y 轴上 b^2=9，a^2=25，c=4。"},
{"qtype":"填空题","difficulty":2,"stem":"双曲线 x^2-y^2=1 的焦点坐标为________。","answer":"(±√2,0)","analysis":"a=b=1，c=√2。"},
{"qtype":"填空题","difficulty":3,"stem":"椭圆两焦点为 (-2,0)、(2,0)，离心率为 1/2，则其短轴长为________。","answer":"4√3","analysis":"c=2，e=c/a=1/2 得 a=4，b=√(a^2-c^2)=√12=2√3，短轴长 2b=4√3。"},
{"qtype":"填空题","difficulty":3,"stem":"双曲线实轴长为 6，焦距为 10，则其渐近线方程为________。","answer":"y=±4/3 x","analysis":"2a=6，a=3；2c=10，c=5；b=4，渐近线 y=±4/3 x。"},
{"qtype":"解答题","difficulty":3,"stem":"求椭圆方程，使其长轴长为 8，离心率为 1/2，且焦点在 x 轴上。","answer":"解：2a=8 得 a=4。e=c/a=1/2 得 c=2。b^2=a^2-c^2=16-4=12。焦点在 x 轴上，椭圆方程为 x^2/16+y^2/12=1。","analysis":"由长轴长定 a，由离心率定 c，再用 a^2=b^2+c^2 求 b^2；注意焦点位置决定方程形式。"},
{"qtype":"解答题","difficulty":4,"stem":"已知双曲线过点 (3,√2)，且渐近线为 y=±(2/3)x。求该双曲线的标准方程。","answer":"解：渐近线 y=±(2/3)x，可设双曲线为 x^2/9-y^2/4=λ。代入 (3,√2)：9/9-2/4=1-1/2=1/2=λ。故双曲线方程为 x^2/9-y^2/4=1/2，即 x^2/(9/2)-y^2/2=1。","analysis":"已知渐近线时先设共渐近线的双曲线系 x^2/a^2-y^2/b^2=λ，再用已知点定 λ，避免先验焦点在 x 轴。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_parabola": [
{"qtype":"选择题","difficulty":1,"stem":"抛物线 y^2=4x 的焦点坐标是（ ）","options":["A. (1,0)","B. (-1,0)","C. (0,1)","D. (0,-1)"],"answer":"A","analysis":"y^2=2px 中 2p=4，p=2，焦点 (p/2,0)=(1,0)。"},
{"qtype":"选择题","difficulty":1,"stem":"抛物线 y^2=8x 的准线方程是（ ）","options":["A. x=-2","B. x=2","C. y=-2","D. y=2"],"answer":"A","analysis":"p=4，准线 x=-p/2=-2。"},
{"qtype":"选择题","difficulty":2,"stem":"抛物线 x^2=4y 的焦点到准线的距离是（ ）","options":["A. 1","B. 2","C. 4","D. 8"],"answer":"B","analysis":"x^2=2py 中 2p=4，p=2，焦点到准线距离就是 p。"},
{"qtype":"选择题","difficulty":2,"stem":"抛物线 y^2=2px 过点 (2,4)，则 p=（ ）","options":["A. 1","B. 2","C. 4","D. 8"],"answer":"C","analysis":"代入 16=4p，p=4。"},
{"qtype":"选择题","difficulty":2,"stem":"顶点在原点、对称轴为 x 轴、且过点 (1,-2) 的抛物线方程是（ ）","options":["A. y^2=4x","B. y^2=-4x","C. x^2=4y","D. x^2=-4y"],"answer":"A","analysis":"设 y^2=2px，代入 (1,-2) 得 4=2p，p=2，即 y^2=4x。"},
{"qtype":"选择题","difficulty":3,"stem":"抛物线 y^2=4x 上一点 P 到焦点距离为 3，则 P 到准线距离为（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"C","analysis":"抛物线定义：到焦点距离等于到准线距离。"},
{"qtype":"选择题","difficulty":3,"stem":"抛物线 y^2=4x 上点 P 的横坐标为 2，则 P 到焦点距离为（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"C","analysis":"准线 x=-1，P 到准线距离=2-(-1)=3，即到焦点距离。"},
{"qtype":"选择题","difficulty":3,"stem":"过抛物线 y^2=4x 焦点的直线交抛物线于 A、B 两点，则 |AB| 的最小值为（ ）","options":["A. 2","B. 4","C. 6","D. 8"],"answer":"B","analysis":"过焦点弦中以通径最短，长为 2p=4。"},
{"qtype":"填空题","difficulty":1,"stem":"抛物线 x^2=8y 的焦点坐标为________。","answer":"(0,2)","analysis":"2p=8，p=4，焦点 (0,p/2)=(0,2)。"},
{"qtype":"填空题","difficulty":2,"stem":"抛物线 y^2=12x 的准线方程为________。","answer":"x=-3","analysis":"p=6，准线 x=-p/2=-3。"},
{"qtype":"填空题","difficulty":2,"stem":"抛物线 y=4x^2 的焦点坐标为________。","answer":"(0,1/16)","analysis":"化为 x^2=1/4 y，2p=1/4，p=1/8，焦点 (0,p/2)=(0,1/16)。"},
{"qtype":"填空题","difficulty":3,"stem":"抛物线顶点在原点、焦点为 (0,-3)，则其标准方程为________。","answer":"x^2=-12y","analysis":"p/2=3，p=6，开口向下，x^2=-2py=-12y。"},
{"qtype":"填空题","difficulty":3,"stem":"抛物线 y^2=2px 上横坐标为 1 的点到焦点距离为 2，则 p=________。","answer":"2","analysis":"该点到准线 x=-p/2 距离为 1+p/2=2，得 p=2。"},
{"qtype":"解答题","difficulty":3,"stem":"已知抛物线顶点在原点，焦点在 x 轴正半轴上，且过点 M(2,-2√2)。求：(1)抛物线标准方程；(2)焦点坐标与准线方程。","answer":"解：(1)设 y^2=2px。代入 M：8=4p，p=2，故 y^2=4x。(2)焦点 (1,0)，准线 x=-1。","analysis":"由焦点位置设对应标准方程，用已知点定 p；再按公式读焦点和准线。"},
{"qtype":"解答题","difficulty":4,"stem":"已知抛物线 C: y^2=4x，直线 l 过焦点 F 且斜率为 1，交 C 于 A、B 两点。求：(1)|AB|；(2)△AOB 的面积（O 为原点）。","answer":"解：(1)F(1,0)，l:y=x-1。代入 y^2=4x：(x-1)^2=4x，即 x^2-6x+1=0。设 A(x1,y1)、B(x2,y2)，x1+x2=6。|AB|=x1+x2+p=6+2=8。(2)|OF|=1，A、B 纵坐标差：y1-y2=(x1-1)-(x2-1)=x1-x2=√((x1+x2)^2-4x1x2)=√(36-4)=4√2。S=1/2×|OF|×|y1-y2|=1/2×1×4√2=2√2。","analysis":"过焦点弦长用 x1+x2+p 计算；三角形 AOB 以 OF 为底、A、B 纵坐标差为高。"}
],
"mat_deriv": [
{"qtype":"选择题","difficulty":1,"stem":"函数 f(x)=x^2 的导数 f′(x)=（ ）","options":["A. x","B. 2x","C. 2","D. x^2"],"answer":"B","analysis":"幂函数求导 (x^n)′=nx^(n-1)。"},
{"qtype":"选择题","difficulty":1,"stem":"f(x)=3 的导数 f′(x)=（ ）","options":["A. 3","B. 0","C. 1","D. 3x"],"answer":"B","analysis":"常数的导数为 0。"},
{"qtype":"选择题","difficulty":2,"stem":"f(x)=x^3，则 f′(2)=（ ）","options":["A. 4","B. 6","C. 8","D. 12"],"answer":"D","analysis":"f′(x)=3x^2，f′(2)=12。"},
{"qtype":"选择题","difficulty":2,"stem":"f(x)=1/x 的导数 f′(x)=（ ）","options":["A. 1/x^2","B. -1/x^2","C. 1/x","D. -1/x"],"answer":"B","analysis":"1/x=x^(-1)，导数=-x^(-2)=-1/x^2。"},
{"qtype":"选择题","difficulty":2,"stem":"曲线 y=x^2 在点 (1,1) 处的切线斜率为（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"k=f′(1)=2。"},
{"qtype":"选择题","difficulty":2,"stem":"f(x)=x^2-2x 的单调递增区间是（ ）","options":["A. (-∞,1)","B. (1,+∞)","C. (-∞,-1)","D. (-1,+∞)"],"answer":"B","analysis":"f′(x)=2x-2>0 得 x>1。"},
{"qtype":"选择题","difficulty":3,"stem":"f(x)=x^3-3x 的极小值点是（ ）","options":["A. x=0","B. x=1","C. x=-1","D. x=3"],"answer":"B","analysis":"f′=3x^2-3=0 得 x=±1；x=1 处导数由负变正，为极小值点。"},
{"qtype":"选择题","difficulty":3,"stem":"函数 f(x)=x^3-3x^2+1 的单调递减区间是（ ）","options":["A. (0,2)","B. (-∞,0)","C. (2,+∞)","D. (-∞,2)"],"answer":"A","analysis":"f′=3x^2-6x=3x(x-2)<0，得 0<x<2。"},
{"qtype":"填空题","difficulty":1,"stem":"f(x)=x^4 的导数为________。","answer":"4x^3","analysis":"幂函数求导。"},
{"qtype":"填空题","difficulty":2,"stem":"f(x)=2x+1，则 f′(0)=________。","answer":"2","analysis":"一次函数导数为斜率。"},
{"qtype":"填空题","difficulty":2,"stem":"曲线 y=x^3 在点 (1,1) 处的切线方程为________。","answer":"y=3x-2","analysis":"k=3，点斜式 y-1=3(x-1)。"},
{"qtype":"填空题","difficulty":3,"stem":"f(x)=x^2+ax 在 x=1 处取极值，则 a=________。","answer":"-2","analysis":"f′=2x+a=0 在 x=1 成立，a=-2。"},
{"qtype":"填空题","difficulty":3,"stem":"f(x)=x^3-3x 在 [-2,0] 上的最大值为________。","answer":"2","analysis":"f′=3x^2-3=0 得 x=±1；在 [-2,0] 内 x=-1 为极大点，f(-1)=2，端点 f(-2)=-2，f(0)=0，最大为 2。"},
{"qtype":"解答题","difficulty":3,"stem":"求函数 f(x)=x^3-3x^2-9x+1 的单调区间与极值。","answer":"解：f′(x)=3x^2-6x-9=3(x-3)(x+1)。令 f′=0 得 x=-1 或 x=3。当 x<-1 时 f′>0 递增；-1<x<3 时 f′<0 递减；x>3 时 f′>0 递增。故极大值 f(-1)=6，极小值 f(3)=-26。","analysis":"先求导数并因式分解，再按导数符号列表判断单调区间；由左增右减得极大、左减右增得极小。"},
{"qtype":"解答题","difficulty":4,"stem":"已知曲线 y=x^3+ax+b 在点 (1,3) 处的切线为 y=2x+1。求 a、b 的值。","answer":"解：点 (1,3) 在曲线上：1+a+b=3，即 a+b=2。又 y′=3x^2+a，切线斜率在 x=1 处为 3+a。由切线 y=2x+1 斜率为 2，得 3+a=2，a=-1。代回 a+b=2 得 b=3。","analysis":"切点同时在曲线和切线上给出一个方程；切线斜率等于导数值给出另一个方程，联立解参数。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_space_vec": [
{"qtype":"选择题","difficulty":1,"stem":"空间向量 a=(1,2,3)，b=(2,-1,0)，则 a+b=（ ）","options":["A. (3,1,3)","B. (3,3,3)","C. (-1,3,3)","D. (3,1,-3)"],"answer":"A","analysis":"对应分量相加。"},
{"qtype":"选择题","difficulty":2,"stem":"a=(1,0,0)，b=(0,1,0)，则 a·b=（ ）","options":["A. 0","B. 1","C. √2","D. 2"],"answer":"A","analysis":"单位坐标向量互相垂直，数量积为 0。"},
{"qtype":"选择题","difficulty":2,"stem":"a=(1,2,2)，则 |a|=（ ）","options":["A. 3","B. 9","C. √5","D. √6"],"answer":"A","analysis":"|a|=√(1+4+4)=3。"},
{"qtype":"选择题","difficulty":2,"stem":"点 A(1,0,0)、B(0,1,0)，则 |AB|=（ ）","options":["A. 1","B. √2","C. 2","D. 3"],"answer":"B","analysis":"AB=(-1,1,0)，|AB|=√2。"},
{"qtype":"选择题","difficulty":3,"stem":"a=(1,1,0)，b=(0,1,1)，则 a 与 b 的夹角余弦为（ ）","options":["A. 1/2","B. √2/2","C. 1","D. 0"],"answer":"A","analysis":"a·b=1，|a|=|b|=√2，cos θ=1/2。"},
{"qtype":"选择题","difficulty":3,"stem":"正方体 ABCD-A1B1C1D1 棱长为 1，则 AC1 的长为（ ）","options":["A. √2","B. √3","C. 2","D. 3"],"answer":"B","analysis":"体对角线 √(1+1+1)=√3。"},
{"qtype":"选择题","difficulty":3,"stem":"a=(2,-1,3)，b=(x,2,y)，若 a∥b，则（ ）","options":["A. x=-4，y=-6","B. x=4，y=-6","C. x=1，y=1","D. x=-1，y=1"],"answer":"A","analysis":"两向量平行则对应分量成比例：x/2=2/(-1)=y/3，由公比 2/(-1)=-2 得 x=2×(-2)=-4，y=3×(-2)=-6，即 b=-2a，故选A。"},
{"qtype":"选择题","difficulty":3,"stem":"a=(1,2,3)，b=(-2,1,0)，则 a·b=（ ）","options":["A. 0","B. 1","C. 2","D. 3"],"answer":"A","analysis":"1×(-2)+2×1+3×0=0。"},
{"qtype":"填空题","difficulty":1,"stem":"a=(1,2,3)，则 2a=________。","answer":"(2,4,6)","analysis":"数乘各分量乘 2。"},
{"qtype":"填空题","difficulty":2,"stem":"a=(1,-2,2)，则 |a|=________。","answer":"3","analysis":"√(1+4+4)=3。"},
{"qtype":"填空题","difficulty":2,"stem":"a=(1,0,-1)，b=(2,1,k)，若 a⊥b，则 k=________。","answer":"2","analysis":"数量积=2+0-k=0，k=2。"},
{"qtype":"填空题","difficulty":3,"stem":"点 A(1,1,1)、B(2,3,4)，则 AB 的中点坐标为________。","answer":"(3/2,2,5/2)","analysis":"中点坐标为两端点坐标平均。"},
{"qtype":"填空题","difficulty":3,"stem":"a=(2,-3,1)，b=(1,2,-1)，则 a·b=________。","answer":"-5","analysis":"2×1+(-3)×2+1×(-1)=2-6-1=-5。"},
{"qtype":"解答题","difficulty":3,"stem":"已知 a=(1,1,0)，b=(0,1,1)，c=(1,0,1)。求：(1)a·b；(2)|a+b+c|；(3)a 与 b 的夹角。","answer":"解：(1)a·b=1×0+1×1+0×1=1。(2)a+b+c=(2,2,2)，|a+b+c|=√(4+4+4)=2√3。(3)|a|=|b|=√2，cos θ=a·b/(|a||b|)=1/2，故 θ=60°。","analysis":"空间向量数量积、模、夹角公式与平面向量一致，只是分量多一维。"},
{"qtype":"解答题","difficulty":4,"stem":"正方体 ABCD-A1B1C1D1 棱长为 2，以 D 为原点，DA、DC、DD1 分别为 x、y、z 轴建系。(1)写出向量 A1B 与 B1C 的坐标；(2)求异面直线 A1B 与 B1C 所成角的余弦值。","answer":"解：(1)D(0,0,0)，A(2,0,0)，B(2,2,0)，C(0,2,0)，A1(2,0,2)，B1(2,2,2)。A1B=B-A1=(0,2,-2)，B1C=C-B1=(-2,0,-2)。(2)A1B·B1C=0×(-2)+2×0+(-2)×(-2)=4。|A1B|=|B1C|=2√2。cos θ=4/(2√2×2√2)=4/8=1/2。故异面直线所成角余弦为 1/2。","analysis":"建系后写出各点坐标，用向量坐标求异面直线所成角；注意所成角取锐角或直角，余弦取绝对值。"}
],
"mat_solve_tri": [
{"qtype":"选择题","difficulty":1,"stem":"在△ABC 中，A=30°，B=60°，则 C=（ ）","options":["A. 60°","B. 90°","C. 120°","D. 30°"],"answer":"B","analysis":"三角形内角和 180°。"},
{"qtype":"选择题","difficulty":2,"stem":"正弦定理 a/sin A=（ ）","options":["A. b/sin B","B. c/sin C","C. 2R","D. 以上都对"],"answer":"D","analysis":"正弦定理三种写法等价，R 为外接圆半径。"},
{"qtype":"选择题","difficulty":2,"stem":"△ABC 中，a=2，A=30°，则外接圆半径 R=（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"2R=a/sin A=2/(1/2)=4，R=2。"},
{"qtype":"选择题","difficulty":2,"stem":"余弦定理 a^2=（ ）","options":["A. b^2+c^2-2bc cos A","B. b^2+c^2+2bc cos A","C. b^2+c^2-2bc sin A","D. b^2-c^2"],"answer":"A","analysis":"余弦定理标准形式。"},
{"qtype":"选择题","difficulty":2,"stem":"△ABC 中，a=3，b=4，c=5，则角 C=（ ）","options":["A. 30°","B. 60°","C. 90°","D. 120°"],"answer":"C","analysis":"3-4-5 直角三角形，c 为斜边对直角 C。"},
{"qtype":"选择题","difficulty":3,"stem":"△ABC 中，a=1，b=√3，A=30°，则 B=（ ）","options":["A. 60°","B. 30°","C. 60°或 120°","D. 120°"],"answer":"C","analysis":"sin B=b sin A/a=√3×(1/2)/1=√3/2，B=60° 或 120°，两解均成立。"},
{"qtype":"选择题","difficulty":3,"stem":"△ABC 面积 S=（ ）","options":["A. 1/2 ab sin C","B. ab sin C","C. 1/2 ab cos C","D. 1/2(a+b+c)"],"answer":"A","analysis":"两边及其夹角面积公式。"},
{"qtype":"选择题","difficulty":3,"stem":"△ABC 中，a=2，b=3，C=60°，则其面积为（ ）","options":["A. 3√3/2","B. 3√3","C. √3/2","D. 3/2"],"answer":"A","analysis":"S=1/2×2×3×sin 60°=3√3/2。"},
{"qtype":"填空题","difficulty":1,"stem":"△ABC 中，A=45°，B=45°，则 C=________。","answer":"90°","analysis":"内角和 180°。"},
{"qtype":"填空题","difficulty":2,"stem":"△ABC 中，a=√2，b=√2，A=45°，则 B=________。","answer":"45°","analysis":"a=b 等腰，B=A=45°。"},
{"qtype":"填空题","difficulty":3,"stem":"△ABC 中，a=2，b=2√3，A=30°，则 c=________。","answer":"4 或 2","analysis":"sin B=b sin A/a=√3/2，B=60° 或 120°。B=60° 时 C=90°，c=4；B=120° 时 C=30°，c=2。两解均成立。"},
{"qtype":"填空题","difficulty":3,"stem":"△ABC 中，a=3，b=5，c=7，则最大角为________。","answer":"120°","analysis":"最大边 c 对最大角 C，cos C=(a^2+b^2-c^2)/(2ab)=(9+25-49)/30=-1/2，C=120°。"},
{"qtype":"填空题","difficulty":3,"stem":"△ABC 中，a=2，b=2，C=60°，则 c=________。","answer":"2","analysis":"由余弦定理 c^2=4+4-8×(1/2)=4，c=2。"},
{"qtype":"解答题","difficulty":3,"stem":"△ABC 中，已知 a=2√3，b=2，A=60°。求 B 及边 c。","answer":"解：由正弦定理 sin B=b sin A/a=2×(√3/2)/(2√3)=1/2。因 b<a，B<A，故 B=30°（舍去 150°）。C=180°-60°-30°=90°，c=a sin C/sin A=2√3×1/(√3/2)=4。","analysis":"用正弦定理求 B 后要根据大边对大角判断取舍，再求 C 与 c。"},
{"qtype":"解答题","difficulty":4,"stem":"△ABC 中，已知 a=7，b=5，c=3。(1)求最大角；(2)求△ABC 的面积。","answer":"解：(1)最大边 a 对最大角 A。cos A=(b^2+c^2-a^2)/(2bc)=(25+9-49)/(2×5×3)=-15/30=-1/2，故 A=120°。(2)S=1/2 bc sin A=1/2×5×3×sin 120°=15√3/4。","analysis":"大边对大角先定最大角；用余弦定理求角，再用两边夹角求面积，注意 120° 的正弦值为 √3/2。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_jr_num": [
{"qtype":"选择题","difficulty":1,"stem":"下列各数中是无理数的是（ ）","options":["A. 0","B. 1/3","C. √2","D. -2"],"answer":"C","analysis":"√2 是无限不循环小数，为无理数。"},
{"qtype":"选择题","difficulty":1,"stem":"|-3|=（ ）","options":["A. 3","B. -3","C. 1/3","D. ±3"],"answer":"A","analysis":"负数的绝对值是它的相反数。"},
{"qtype":"选择题","difficulty":1,"stem":"4 的算术平方根是（ ）","options":["A. 2","B. ±2","C. √2","D. 16"],"answer":"A","analysis":"算术平方根取非负。"},
{"qtype":"选择题","difficulty":2,"stem":"√9 的值是（ ）","options":["A. 3","B. -3","C. ±3","D. 81"],"answer":"A","analysis":"√9 表示 9 的算术平方根。"},
{"qtype":"选择题","difficulty":2,"stem":"计算 (-2)^3=（ ）","options":["A. -6","B. 6","C. -8","D. 8"],"answer":"C","analysis":"负数奇次幂为负，(-2)^3=-8。"},
{"qtype":"选择题","difficulty":2,"stem":"下列各式正确的是（ ）（题组2）","options":["A. √16=±4","B. √(-4)^2=-4","C. (√4)^2=4","D. √(-4)=-2"],"answer":"C","analysis":"A 应为 4；B 应为 4；D 负数不能开平方。"},
{"qtype":"选择题","difficulty":2,"stem":"用科学记数法表示 35000 为（ ）","options":["A. 3.5×10^4","B. 3.5×10^3","C. 35×10^3","D. 0.35×10^5"],"answer":"A","analysis":"科学记数法 a×10^n 中 1≤|a|<10。"},
{"qtype":"选择题","difficulty":3,"stem":"已知 |a|=3，|b|=2，且 ab<0，则 a+b=（ ）","options":["A. 1","B. -1","C. 1 或 -1","D. 5"],"answer":"C","analysis":"ab<0 异号，a=3,b=-2 或 a=-3,b=2，和为 1 或 -1。"},
{"qtype":"填空题","difficulty":1,"stem":"-5 的相反数是________。","answer":"5","analysis":"只有符号不同的两个数互为相反数。"},
{"qtype":"填空题","difficulty":1,"stem":"16 的平方根是________。","answer":"±4","analysis":"平方根有两个，互为相反数。"},
{"qtype":"填空题","difficulty":2,"stem":"计算：(-1)^2026=________。","answer":"1","analysis":"偶数次幂为 1。"},
{"qtype":"填空题","difficulty":2,"stem":"比较大小：√5________2（填 >、< 或 =）。","answer":">","analysis":"√5≈2.236>2。"},
{"qtype":"填空题","difficulty":3,"stem":"若 √(a-2)+|b+1|=0，则 a+b=________。","answer":"1","analysis":"两个非负项同时为 0：a=2，b=-1，和为 1。"},
{"qtype":"解答题","difficulty":2,"stem":"计算：(1)(-3)+5-(-2)；(2)(-2)^2×(-3)；(3)|-5|+√16-(-1)^2。","answer":"解：(1)原式=-3+5+2=4。(2)原式=4×(-3)=-12。(3)原式=5+4-1=8。","analysis":"按先乘方、再乘除、后加减的顺序计算；绝对值和算术平方根先化简。"},
{"qtype":"解答题","difficulty":3,"stem":"已知实数 a、b 在数轴上的位置如图：a 在原点左侧，b 在原点右侧，且 |a|>|b|。化简 |a+b|+|a-b|。","answer":"解：由题意 a<0<b 且 |a|>|b|，故 a+b<0，a-b<0。|a+b|=-(a+b)，|a-b|=-(a-b)，原式=-a-b-a+b=-2a。","analysis":"先根据数轴判断 a+b、a-b 的符号，再去绝对值；去绝对值时注意符号。"}
],
"mat_jr_alg": [
{"qtype":"选择题","difficulty":1,"stem":"单项式 -3x^2y 的系数是（ ）","options":["A. 3","B. -3","C. 3x^2","D. -3x^2"],"answer":"B","analysis":"单项式的数字因数叫系数。"},
{"qtype":"选择题","difficulty":1,"stem":"化简 3a+2a=（ ）","options":["A. 5a","B. 6a","C. 5a^2","D. 1"],"answer":"A","analysis":"合并同类项，系数相加字母不变。"},
{"qtype":"选择题","difficulty":2,"stem":"计算 (a^2)^3=（ ）","options":["A. a^5","B. a^6","C. a^8","D. 3a^2"],"answer":"B","analysis":"幂的乘方，指数相乘。"},
{"qtype":"选择题","difficulty":2,"stem":"计算 a^3·a^2=（ ）","options":["A. a^5","B. a^6","C. a^1","D. 2a^5"],"answer":"A","analysis":"同底数幂相乘，指数相加。"},
{"qtype":"选择题","difficulty":2,"stem":"分解因式 x^2-4=（ ）","options":["A. (x-2)^2","B. (x+2)(x-2)","C. (x+4)(x-1)","D. (x-4)(x+1)"],"answer":"B","analysis":"平方差公式。"},
{"qtype":"选择题","difficulty":2,"stem":"分解因式 x^2+2x+1=（ ）","options":["A. (x+1)^2","B. (x-1)^2","C. (x+1)(x-1)","D. x(x+2)+1"],"answer":"A","analysis":"完全平方公式。"},
{"qtype":"选择题","difficulty":3,"stem":"计算 (x+2)(x-3)=（ ）","options":["A. x^2-x-6","B. x^2+x-6","C. x^2-6","D. x^2-5x-6"],"answer":"A","analysis":"展开得 x^2-3x+2x-6=x^2-x-6。"},
{"qtype":"选择题","difficulty":3,"stem":"若 x^2+kx+9 是完全平方式，则 k=（ ）","options":["A. 6","B. ±6","C. 3","D. ±3"],"answer":"B","analysis":"9=3^2，中间项 ±2×3=±6。"},
{"qtype":"填空题","difficulty":1,"stem":"计算：2a·3a=________。","answer":"6a^2","analysis":"系数相乘，同字母幂相加。"},
{"qtype":"填空题","difficulty":2,"stem":"分解因式：x^2-3x=________。","answer":"x(x-3)","analysis":"提取公因式 x。"},
{"qtype":"填空题","difficulty":2,"stem":"计算：(x+1)^2=________。","answer":"x^2+2x+1","analysis":"完全平方公式。"},
{"qtype":"填空题","difficulty":3,"stem":"分解因式：x^2-6x+9=________。","answer":"(x-3)^2","analysis":"完全平方公式。"},
{"qtype":"填空题","difficulty":3,"stem":"若 a+b=3，ab=2，则 a^2+b^2=________。","answer":"5","analysis":"a^2+b^2=(a+b)^2-2ab=9-4=5。"},
{"qtype":"解答题","difficulty":2,"stem":"计算：(1)(2a^2)^3；(2)(x+3)(x-3)；(3)(2x-1)^2。","answer":"解：(1)原式=8a^6。(2)原式=x^2-9。(3)原式=4x^2-4x+1。","analysis":"幂的乘方与积的乘方、平方差公式、完全平方公式分别应用；注意系数和符号。"},
{"qtype":"解答题","difficulty":3,"stem":"分解因式：(1)3x^2-12；(2)x^3-2x^2+x；(3)a^2-2ab+b^2-c^2。","answer":"解：(1)原式=3(x^2-4)=3(x+2)(x-2)。(2)原式=x(x^2-2x+1)=x(x-1)^2。(3)原式=(a-b)^2-c^2=(a-b+c)(a-b-c)。","analysis":"因式分解先提公因式再用公式，做到分解彻底；第三题分组后用平方差。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_jr_frac": [
{"qtype":"选择题","difficulty":1,"stem":"分式 1/(x-1) 有意义的条件是（ ）","options":["A. x≠1","B. x=1","C. x>1","D. x<1"],"answer":"A","analysis":"分母不为 0。"},
{"qtype":"选择题","difficulty":1,"stem":"分式 (x-2)/(x+3) 的值为 0，则 x=（ ）","options":["A. 2","B. -3","C. 3","D. -2"],"answer":"A","analysis":"值为 0 需分子为 0 且分母不为 0。"},
{"qtype":"选择题","difficulty":2,"stem":"化简 (a^2-ab)/a=（ ）","options":["A. a-b","B. a+b","C. a^2-b","D. a-1"],"answer":"A","analysis":"分子提取 a 后约分。"},
{"qtype":"选择题","difficulty":2,"stem":"计算 1/x+1/x=（ ）","options":["A. 2/x","B. 1/x^2","C. 2/x^2","D. 2x"],"answer":"A","analysis":"同分母分式相加。"},
{"qtype":"选择题","difficulty":2,"stem":"√8 化简结果为（ ）","options":["A. 2√2","B. 4√2","C. 2","D. √4"],"answer":"A","analysis":"√8=√(4×2)=2√2。"},
{"qtype":"选择题","difficulty":2,"stem":"计算 √2×√8=（ ）","options":["A. 4","B. 2√2","C. √10","D. 16"],"answer":"A","analysis":"√2×√8=√16=4。"},
{"qtype":"选择题","difficulty":3,"stem":"计算 √18-√2=（ ）","options":["A. 2√2","B. 4√2","C. √2","D. 2"],"answer":"A","analysis":"√18=3√2，3√2-√2=2√2。"},
{"qtype":"选择题","difficulty":3,"stem":"分式方程 2/(x-1)=1 的解为（ ）","options":["A. x=3","B. x=2","C. x=1","D. x=-1"],"answer":"A","analysis":"去分母得 2=x-1，x=3，检验分母不为 0。"},
{"qtype":"填空题","difficulty":1,"stem":"当 x=________ 时，分式 (x+1)/(x-2) 无意义。","answer":"2","analysis":"分母为 0 时无意义。"},
{"qtype":"填空题","difficulty":2,"stem":"化简：(x^2-1)/(x+1)=________。","answer":"x-1","analysis":"分子因式分解后约分。"},
{"qtype":"填空题","difficulty":2,"stem":"√12=________（化为最简二次根式）。","answer":"2√3","analysis":"√12=√(4×3)。"},
{"qtype":"填空题","difficulty":3,"stem":"计算：√27+√(1/3)=________。","answer":"10√3/3","analysis":"√27=3√3，√(1/3)=√3/3，合并得 10√3/3。"},
{"qtype":"填空题","difficulty":3,"stem":"若分式 (|x|-1)/(x-1) 的值为 0，则 x=________。","answer":"-1","analysis":"|x|-1=0 得 x=±1，又 x≠1，故 x=-1。"},
{"qtype":"解答题","difficulty":2,"stem":"计算：(1)(1/a+1/b)·ab；(2)√12+√27-√3；(3)(√5+√3)(√5-√3)。","answer":"解：(1)原式=(b+a)/(ab)·ab=a+b。(2)原式=2√3+3√3-√3=4√3。(3)原式=5-3=2。","analysis":"分式混合运算注意通分约分；二次根式先化最简再合并；平方差公式直接应用。"},
{"qtype":"解答题","difficulty":3,"stem":"解分式方程：2/(x-1)=4/(x^2-1)。","answer":"解：最简公分母为 (x+1)(x-1)。两边同乘 (x+1)(x-1) 得 2(x+1)=4，解得 x=1。检验：当 x=1 时公分母为 0，故 x=1 是增根，原方程无解。","analysis":"分式方程必须检验，使公分母为 0 的根是增根要舍去。"}
],
"mat_jr_eq": [
{"qtype":"选择题","difficulty":1,"stem":"方程 2x+3=7 的解是（ ）","options":["A. x=2","B. x=3","C. x=4","D. x=5"],"answer":"A","analysis":"移项得 2x=4，x=2。"},
{"qtype":"选择题","difficulty":1,"stem":"方程 x^2-4=0 的解是（ ）","options":["A. x=2","B. x=-2","C. x=±2","D. x=4"],"answer":"C","analysis":"x^2=4，开方取正负。"},
{"qtype":"选择题","difficulty":2,"stem":"方程 x^2-5x+6=0 的解是（ ）","options":["A. x=2 或 x=3","B. x=-2 或 x=-3","C. x=1 或 x=6","D. x=2 或 x=-3"],"answer":"A","analysis":"(x-2)(x-3)=0。"},
{"qtype":"选择题","difficulty":2,"stem":"不等式 2x-6>0 的解集是（ ）","options":["A. x>3","B. x<3","C. x>-3","D. x<-3"],"answer":"A","analysis":"移项系数化为 1。"},
{"qtype":"选择题","difficulty":2,"stem":"一元二次方程 x^2-2x+m=0 有两个相等实根，则 m=（ ）","options":["A. 1","B. -1","C. 2","D. 0"],"answer":"A","analysis":"Δ=4-4m=0，m=1。"},
{"qtype":"选择题","difficulty":3,"stem":"不等式组 x-1>0，x-3<0 的解集是（ ）","options":["A. 1<x<3","B. x>1","C. x<3","D. 无解"],"answer":"A","analysis":"取两个不等式解集的公共部分。"},
{"qtype":"选择题","difficulty":3,"stem":"方程 x^2-3x-4=0 的两根之和为（ ）","options":["A. 3","B. -3","C. 4","D. -4"],"answer":"A","analysis":"韦达定理 x1+x2=-b/a=3。"},
{"qtype":"选择题","difficulty":3,"stem":"某商品原价 100 元，连续两次降价后为 81 元，平均每次降价率为（ ）","options":["A. 10%","B. 9%","C. 9.5%","D. 20%"],"answer":"A","analysis":"100(1-x)^2=81，(1-x)^2=0.81，1-x=0.9，x=10%。"},
{"qtype":"填空题","difficulty":1,"stem":"方程 3x-1=5 的解为 x=________。","answer":"2","analysis":"移项得 3x=6。"},
{"qtype":"填空题","difficulty":2,"stem":"方程 x(x-2)=0 的解为________。","answer":"x=0 或 x=2","analysis":"至少一个因式为 0。"},
{"qtype":"填空题","difficulty":2,"stem":"不等式 -2x>4 的解集是________。","answer":"x<-2","analysis":"除以负数要变号。"},
{"qtype":"填空题","difficulty":3,"stem":"方程 x^2-5x+6=0 的两根之积为________。","answer":"6","analysis":"韦达定理 x1x2=c/a=6。"},
{"qtype":"填空题","difficulty":3,"stem":"若关于 x 的方程 x^2+2x+k=0 有两个不相等实根，则 k 的取值范围是________。","answer":"k<1","analysis":"Δ=4-4k>0。"},
{"qtype":"解答题","difficulty":2,"stem":"解下列方程：(1)3(x-2)=x+4；(2)x^2-4x+3=0。","answer":"解：(1)去括号 3x-6=x+4，移项 2x=10，x=5。(2)因式分解 (x-1)(x-3)=0，x=1 或 x=3。","analysis":"一元一次方程按去括号移项求解；一元二次方程优先因式分解。"},
{"qtype":"解答题","difficulty":3,"stem":"某班学生分组活动，若每组 7 人，则余 2 人；若每组 8 人，则缺 4 人。求组数和学生数。","answer":"解：设组数为 x。由题意 7x+2=8x-4，解得 x=6。学生数=7×6+2=44。答：共 6 组，44 人。","analysis":"两种分组方式学生总数相等，据此列一元一次方程；解后检验合理性。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_jr_func1": [
{"qtype":"选择题","difficulty":1,"stem":"正比例函数 y=2x 的图象经过（ ）","options":["A. 第一、三象限","B. 第一、二象限","C. 第二、四象限","D. 第三、四象限"],"answer":"A","analysis":"k>0 过一、三象限。"},
{"qtype":"选择题","difficulty":1,"stem":"一次函数 y=x+1 的图象与 y 轴交点为（ ）","options":["A. (0,1)","B. (1,0)","C. (0,-1)","D. (-1,0)"],"answer":"A","analysis":"令 x=0 得 y=1。"},
{"qtype":"选择题","difficulty":2,"stem":"一次函数 y=-2x+3 中，y 随 x 增大而（ ）","options":["A. 增大","B. 减小","C. 不变","D. 先增后减"],"answer":"B","analysis":"k=-2<0，y 随 x 增大而减小。"},
{"qtype":"选择题","difficulty":2,"stem":"反比例函数 y=6/x 的图象位于（ ）","options":["A. 第一、三象限","B. 第一、二象限","C. 第二、四象限","D. 第三、四象限"],"answer":"A","analysis":"k=6>0，图象在一、三象限。"},
{"qtype":"选择题","difficulty":2,"stem":"反比例函数 y=k/x 过点 (2,3)，则 k=（ ）","options":["A. 6","B. 2/3","C. 3/2","D. 1"],"answer":"A","analysis":"k=xy=6。"},
{"qtype":"选择题","difficulty":2,"stem":"一次函数 y=kx+b 图象过一、二、三象限，则（ ）","options":["A. k>0，b>0","B. k>0，b<0","C. k<0，b>0","D. k<0，b<0"],"answer":"A","analysis":"k>0 递增，b>0 与 y 轴正半轴相交。"},
{"qtype":"选择题","difficulty":3,"stem":"函数 y=1/x 与 y=x 的图象交点个数为（ ）","options":["A. 0","B. 1","C. 2","D. 3"],"answer":"C","analysis":"联立 x=1/x 得 x^2=1，x=±1，两个交点。"},
{"qtype":"选择题","difficulty":3,"stem":"反比例函数 y=k/x 在每一支上 y 随 x 增大而增大，则 k 的取值范围是（ ）","options":["A. k>0","B. k<0","C. k≥0","D. k≤0"],"answer":"B","analysis":"k<0 时在每个象限内 y 随 x 增大而增大。"},
{"qtype":"填空题","difficulty":1,"stem":"一次函数 y=3x-2 与 x 轴交点坐标为________。","answer":"(2/3,0)","analysis":"令 y=0 得 x=2/3。"},
{"qtype":"填空题","difficulty":2,"stem":"正比例函数 y=kx 过点 (1,-3)，则 k=________。","answer":"-3","analysis":"代入得 k=-3。"},
{"qtype":"填空题","difficulty":2,"stem":"反比例函数 y=4/x，当 x=2 时 y=________。","answer":"2","analysis":"y=4/2=2。"},
{"qtype":"填空题","difficulty":3,"stem":"一次函数 y=2x+b 过点 (1,3)，则 b=________。","answer":"1","analysis":"代入 3=2+b。"},
{"qtype":"填空题","difficulty":3,"stem":"反比例函数 y=k/x 经过点 (-2,3)，则 k=________。","answer":"-6","analysis":"k=xy=-6。"},
{"qtype":"解答题","difficulty":2,"stem":"已知一次函数图象经过点 A(0,2) 和 B(1,0)。(1)求该一次函数解析式；(2)判断点 C(2,-2) 是否在该图象上。","answer":"解：(1)设 y=kx+b。代入 A 得 b=2；代入 B 得 0=k+2，k=-2。故 y=-2x+2。(2)x=2 时 y=-4+2=-2，与 C 的纵坐标相同，故 C 在图象上。","analysis":"用待定系数法列方程组求 k、b；判断点是否在图象上只需代入验证。"},
{"qtype":"解答题","difficulty":3,"stem":"反比例函数 y=k/x 的图象经过点 A(2,3)。(1)求 k；(2)当 x=3 时求 y；(3)判断点 B(-3,-2) 是否在该图象上。","answer":"解：(1)k=2×3=6。(2)y=6/3=2。(3)x=-3 时 y=6/(-3)=-2，与 B 纵坐标相同，故 B 在图象上。","analysis":"反比例函数中 k=xy 是定值；判断点在图象上即验证 xy 是否等于 k。"}
],
"mat_jr_quad": [
{"qtype":"选择题","difficulty":1,"stem":"抛物线 y=x^2 的开口方向是（ ）","options":["A. 向上","B. 向下","C. 向左","D. 向右"],"answer":"A","analysis":"a=1>0，开口向上。"},
{"qtype":"选择题","difficulty":1,"stem":"抛物线 y=(x-1)^2 的顶点坐标是（ ）","options":["A. (1,0)","B. (-1,0)","C. (0,1)","D. (0,-1)"],"answer":"A","analysis":"顶点式直接读出。"},
{"qtype":"选择题","difficulty":2,"stem":"抛物线 y=x^2-2x+3 的对称轴是（ ）","options":["A. x=1","B. x=-1","C. x=2","D. x=-2"],"answer":"A","analysis":"对称轴 x=-b/(2a)=2/2=1。"},
{"qtype":"选择题","difficulty":2,"stem":"抛物线 y=-x^2+4x-3 的最大值是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"A","analysis":"顶点 x=2，y=-4+8-3=1。"},
{"qtype":"选择题","difficulty":2,"stem":"二次函数 y=x^2-4x+3 与 x 轴交点个数为（ ）","options":["A. 0","B. 1","C. 2","D. 3"],"answer":"C","analysis":"Δ=16-12=4>0，两个交点。"},
{"qtype":"选择题","difficulty":3,"stem":"抛物线 y=2(x+1)^2-3 是由 y=2x^2 如何平移得到（ ）","options":["A. 左移 1 下移 3","B. 右移 1 下移 3","C. 左移 1 上移 3","D. 右移 1 上移 3"],"answer":"A","analysis":"左加右减、上加下减。"},
{"qtype":"选择题","difficulty":3,"stem":"二次函数 y=ax^2+bx+c 图象开口向下，对称轴在 y 轴右侧，则（ ）","options":["A. a<0，b<0","B. a<0，b>0","C. a>0，b<0","D. a>0，b>0"],"answer":"B","analysis":"开口向下 a<0；对称轴 x=-b/(2a)>0，a<0 故 b>0。"},
{"qtype":"选择题","difficulty":3,"stem":"二次函数 y=x^2-2x-3，当 y<0 时 x 的取值范围是（ ）","options":["A. -1<x<3","B. x<-1 或 x>3","C. x<3","D. x>-1"],"answer":"A","analysis":"开口向上，y<0 取两根之间。"},
{"qtype":"填空题","difficulty":1,"stem":"抛物线 y=x^2+1 的顶点坐标为________。","answer":"(0,1)","analysis":"直接由顶点式读出。"},
{"qtype":"填空题","difficulty":2,"stem":"抛物线 y=-2x^2 的开口向________。","answer":"下","analysis":"a=-2<0。"},
{"qtype":"填空题","difficulty":2,"stem":"二次函数 y=x^2-4 的最小值为________。","answer":"-4","analysis":"顶点在 (0,-4)。"},
{"qtype":"填空题","difficulty":3,"stem":"抛物线 y=x^2+bx+3 的对称轴为 x=1，则 b=________。","answer":"-2","analysis":"-b/2=1，b=-2。"},
{"qtype":"填空题","difficulty":3,"stem":"二次函数 y=x^2-2x-3 与 y 轴交点坐标为________。","answer":"(0,-3)","analysis":"令 x=0 得 y=-3。"},
{"qtype":"解答题","difficulty":2,"stem":"已知二次函数 y=x^2-2x-3。(1)求顶点坐标和对称轴；(2)求与 x 轴交点；(3)求 y 的最小值。","answer":"解：(1)配方 y=(x-1)^2-4，顶点 (1,-4)，对称轴 x=1。(2)令 y=0：x^2-2x-3=0，(x-3)(x+1)=0，交点为 (3,0)、(-1,0)。(3)开口向上，最小值为 -4。","analysis":"先配方成顶点式读顶点对称轴；求 x 轴交点解二次方程；最小值即顶点纵坐标。"},
{"qtype":"解答题","difficulty":4,"stem":"某商品进价 40 元，售价 50 元时每月可卖 500 件。售价每涨 1 元少卖 10 件。设涨价 x 元，利润 y 元。(1)求 y 与 x 的函数关系式；(2)售价定为多少时利润最大？最大利润是多少？","answer":"解：(1)每件利润 (50-40+x)=(10+x) 元，销量 (500-10x) 件，y=(10+x)(500-10x)=-10x^2+400x+5000。(2)a=-10<0，顶点 x=-b/(2a)=400/20=20。此时售价 50+20=70 元，最大利润 y=-10×400+400×20+5000=9000 元。","analysis":"利润=每件利润×销量列函数；二次项系数为负时顶点取最大值，注意实际意义 x 使销量非负。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_jr_geo": [
{"qtype":"选择题","difficulty":1,"stem":"一个三角形内角和等于（ ）","options":["A. 90°","B. 180°","C. 270°","D. 360°"],"answer":"B","analysis":"三角形内角和定理。"},
{"qtype":"选择题","difficulty":1,"stem":"等边三角形每个内角等于（ ）","options":["A. 60°","B. 90°","C. 45°","D. 30°"],"answer":"A","analysis":"三个内角相等且和为 180°。"},
{"qtype":"选择题","difficulty":2,"stem":"两直线平行，同位角（ ）","options":["A. 相等","B. 互补","C. 互余","D. 不确定"],"answer":"A","analysis":"平行线性质：同位角相等。"},
{"qtype":"选择题","difficulty":2,"stem":"直角三角形两锐角之和为（ ）","options":["A. 30°","B. 60°","C. 90°","D. 180°"],"answer":"C","analysis":"两锐角互余。"},
{"qtype":"选择题","difficulty":2,"stem":"下列条件不能判定两三角形全等的是（ ）","options":["A. SSS","B. SAS","C. ASA","D. SSA"],"answer":"D","analysis":"SSA 不能判定全等。"},
{"qtype":"选择题","difficulty":2,"stem":"等腰三角形一个底角为 50°，则顶角为（ ）","options":["A. 50°","B. 80°","C. 60°","D. 100°"],"answer":"B","analysis":"顶角=180°-2×50°=80°。"},
{"qtype":"选择题","difficulty":3,"stem":"三角形两边长为 3 和 5，则第三边 x 的取值范围是（ ）","options":["A. 2<x<8","B. 3<x<5","C. x>2","D. x<8"],"answer":"A","analysis":"三角形三边关系：两边之差小于第三边小于两边之和。"},
{"qtype":"选择题","difficulty":3,"stem":"n 边形内角和为 1080°，则 n=（ ）","options":["A. 6","B. 7","C. 8","D. 9"],"answer":"C","analysis":"(n-2)×180°=1080°，n=8。"},
{"qtype":"填空题","difficulty":1,"stem":"70° 角的余角等于________。","answer":"20°","analysis":"互余两角和为 90°。"},
{"qtype":"填空题","difficulty":2,"stem":"三角形三个内角度数比为 1:2:3，则最大角为________。","answer":"90°","analysis":"180°×3/6=90°。"},
{"qtype":"填空题","difficulty":2,"stem":"正六边形每个内角等于________。","answer":"120°","analysis":"(6-2)×180°/6=120°。"},
{"qtype":"填空题","difficulty":3,"stem":"等腰三角形两边长为 4 和 9，则周长为________。","answer":"22","analysis":"腰只能为 9（4 作腰时 4+4<9 不成立），周长=9+9+4=22。"},
{"qtype":"填空题","difficulty":3,"stem":"直角三角形两直角边为 6 和 8，则斜边为________。","answer":"10","analysis":"勾股定理 6^2+8^2=100=10^2。"},
{"qtype":"解答题","difficulty":2,"stem":"如图，在△ABC 中，∠A=70°，∠B=50°，CD 平分∠ACB 交 AB 于 D。求∠BCD 的度数。","answer":"解：∠ACB=180°-70°-50°=60°。CD 平分∠ACB，故∠BCD=1/2×60°=30°。","analysis":"先用内角和求第三角，再用角平分线性质求一半角。"},
{"qtype":"解答题","difficulty":3,"stem":"已知 AB=AD，BC=DC。求证：△ABC≌△ADC。","answer":"证明：在△ABC 和△ADC 中，AB=AD（已知），BC=DC（已知），AC=AC（公共边）。由 SSS 得△ABC≌△ADC。","analysis":"找齐三组对应边相等，注意公共边 AC 是隐含条件，用 SSS 判定。"}
],
"mat_jr_circle": [
{"qtype":"选择题","difficulty":1,"stem":"圆的周长公式 C=（ ）","options":["A. 2πr","B. πr^2","C. πd^2","D. πr"],"answer":"A","analysis":"周长=2πr。"},
{"qtype":"选择题","difficulty":1,"stem":"半径为 2 的圆面积为（ ）","options":["A. 2π","B. 4π","C. 8π","D. 16π"],"answer":"B","analysis":"S=πr^2=4π。"},
{"qtype":"选择题","difficulty":2,"stem":"同弧所对的圆周角等于圆心角的（ ）","options":["A. 一半","B. 相等","C. 两倍","D. 三倍"],"answer":"A","analysis":"圆周角定理。"},
{"qtype":"选择题","difficulty":2,"stem":"90° 的圆周角所对的弦是圆的（ ）","options":["A. 半径","B. 直径","C. 切线","D. 不确定"],"answer":"B","analysis":"90° 圆周角所对弦为直径。"},
{"qtype":"选择题","difficulty":2,"stem":"圆的切线垂直于过切点的（ ）","options":["A. 半径","B. 弦","C. 直径","D. 弧"],"answer":"A","analysis":"切线性质定理。"},
{"qtype":"选择题","difficulty":2,"stem":"半径为 6 的圆中，圆心角为 60° 的扇形面积为（ ）","options":["A. 6π","B. 12π","C. 3π","D. 24π"],"answer":"A","analysis":"S=60/360×π×36=6π。"},
{"qtype":"选择题","difficulty":3,"stem":"⊙O 半径为 5，圆心 O 到直线 l 距离为 3，则直线 l 与圆的位置关系是（ ）","options":["A. 相交","B. 相切","C. 相离","D. 无法确定"],"answer":"A","analysis":"d=3<r=5，相交。"},
{"qtype":"选择题","difficulty":3,"stem":"PA 切⊙O 于 A，PO=13，OA=5，则 PA=（ ）","options":["A. 12","B. 8","C. 18","D. 14"],"answer":"A","analysis":"切线垂直半径，勾股定理 PA=√(13^2-5^2)=12。"},
{"qtype":"填空题","difficulty":1,"stem":"圆的直径为 10，则半径为________。","answer":"5","analysis":"半径是直径一半。"},
{"qtype":"填空题","difficulty":2,"stem":"半径为 3 的圆周长为________。","answer":"6π","analysis":"C=2πr=6π。"},
{"qtype":"填空题","difficulty":2,"stem":"一条弧所对圆心角为 80°，则它所对圆周角为________。","answer":"40°","analysis":"圆周角是圆心角一半。"},
{"qtype":"填空题","difficulty":3,"stem":"⊙O 半径为 4，圆心 O 到直线 l 距离为 4，则 l 与圆的位置关系是________。","answer":"相切","analysis":"d=r 时相切。"},
{"qtype":"填空题","difficulty":3,"stem":"圆锥底面半径为 3，母线长为 5，则其侧面积为________。","answer":"15π","analysis":"侧面积=πrl=π×3×5=15π。"},
{"qtype":"解答题","difficulty":2,"stem":"在⊙O 中，弦 AB=8，圆心 O 到 AB 的距离为 3，求⊙O 的半径。","answer":"解：过 O 作 OC⊥AB 于 C，则 AC=1/2 AB=4。在 Rt△OAC 中，OA=√(OC^2+AC^2)=√(9+16)=5。故⊙O 半径为 5。","analysis":"垂径定理构造直角三角形，半弦、弦心距、半径构成勾股数。"},
{"qtype":"解答题","difficulty":3,"stem":"PA、PB 分别切⊙O 于 A、B，∠P=60°，PA=3。求：(1)∠AOB；(2)弦 AB 的长。","answer":"解：(1)PA、PB 为切线，OA⊥PA，OB⊥PB。四边形 OAPB 中∠OAP=∠OBP=90°，故∠AOB=360°-90°-90°-60°=120°。(2)由切线长定理 PA=PB=3，又∠P=60°，故△PAB 为等边三角形，AB=PA=3。","analysis":"切线垂直半径得两个直角；切线长定理得 PA=PB，夹角 60° 推出等边三角形。"}
]
})

# -*- coding: utf-8 -*-
BANK.update({
"mat_jr_sim": [
{"qtype":"选择题","difficulty":1,"stem":"相似三角形对应边的比叫做（ ）","options":["A. 相似比","B. 比值","C. 比例","D. 周长比"],"answer":"A","analysis":"相似三角形对应边比即相似比。"},
{"qtype":"选择题","difficulty":1,"stem":"sin 30°=（ ）（题组2）","options":["A. 1/2","B. √2/2","C. √3/2","D. 1"],"answer":"A","analysis":"特殊角三角函数值。"},
{"qtype":"选择题","difficulty":2,"stem":"已知△ABC∽△DEF，相似比为 2:3，则周长比为（ ）","options":["A. 2:3","B. 4:9","C. √2:√3","D. 2:9"],"answer":"A","analysis":"相似三角形周长比等于相似比。"},
{"qtype":"选择题","difficulty":2,"stem":"cos 60°=（ ）（题组2）","options":["A. 1/2","B. √2/2","C. √3/2","D. 1"],"answer":"A","analysis":"特殊角值。"},
{"qtype":"选择题","difficulty":2,"stem":"tan 45°=（ ）","options":["A. 1/2","B. √2/2","C. 1","D. √3"],"answer":"C","analysis":"特殊角值。"},
{"qtype":"选择题","difficulty":3,"stem":"两个相似三角形面积比为 4:9，则相似比为（ ）","options":["A. 2:3","B. 4:9","C. 16:81","D. √2:√3"],"answer":"A","analysis":"面积比等于相似比平方。"},
{"qtype":"选择题","difficulty":3,"stem":"在 Rt△ABC 中，∠C=90°，AC=3，BC=4，则 sin A=（ ）","options":["A. 3/5","B. 4/5","C. 3/4","D. 4/3"],"answer":"B","analysis":"AB=5，sin A=BC/AB=4/5。"},
{"qtype":"选择题","difficulty":3,"stem":"小明身高 1.6 米，影长 2 米，同一时刻旗杆影长 10 米，则旗杆高（ ）","options":["A. 6 米","B. 8 米","C. 10 米","D. 12 米"],"answer":"B","analysis":"物高与影长成正比：1.6/2=h/10，h=8。"},
{"qtype":"填空题","difficulty":1,"stem":"tan 30°=________。","answer":"√3/3","analysis":"特殊角值。"},
{"qtype":"填空题","difficulty":2,"stem":"相似三角形对应高的比等于________。","answer":"相似比","analysis":"相似三角形对应线段比都等于相似比。"},
{"qtype":"填空题","difficulty":2,"stem":"在 Rt△ABC 中，∠C=90°，AB=5，AC=3，则 cos A=________。","answer":"3/5","analysis":"cos A=AC/AB=3/5。"},
{"qtype":"填空题","difficulty":3,"stem":"两个相似三角形对应边比为 1:2，较小三角形面积为 3，则较大三角形面积为________。","answer":"12","analysis":"面积比为 1:4，较大面积=3×4=12。"},
{"qtype":"填空题","difficulty":3,"stem":"在 Rt△ABC 中，∠C=90°，AC=BC=1，则 sin A=________。","answer":"√2/2","analysis":"AB=√2，sin A=BC/AB=1/√2=√2/2。"},
{"qtype":"解答题","difficulty":2,"stem":"在 Rt△ABC 中，∠C=90°，AB=10，BC=6。求：(1)AC；(2)sin A 和 cos B。","answer":"解：(1)由勾股定理 AC=√(AB^2-BC^2)=√(100-36)=8。(2)sin A=BC/AB=6/10=3/5；cos B=BC/AB=6/10=3/5。","analysis":"先用勾股定理求直角边，再按定义写出正弦余弦；注意 sin A=cos B（同角余角关系）。"},
{"qtype":"解答题","difficulty":3,"stem":"如图，在△ABC 中，DE∥BC，AD=2，DB=3，DE=4。求 BC 的长。","answer":"解：因 DE∥BC，故△ADE∽△ABC。相似比=AD/AB=2/(2+3)=2/5。所以 DE/BC=2/5，即 4/BC=2/5，BC=10。","analysis":"由平行得相似，对应边成比例；注意 AB=AD+DB 不要漏加 DB。"}
],
"mat_jr_stat": [
{"qtype":"选择题","difficulty":1,"stem":"数据 1,2,3 的平均数是（ ）","options":["A. 1","B. 2","C. 3","D. 6"],"answer":"B","analysis":"(1+2+3)/3=2。"},
{"qtype":"选择题","difficulty":1,"stem":"数据 2,2,3,4,4,4 的众数是（ ）","options":["A. 2","B. 3","C. 4","D. 2 和 4"],"answer":"C","analysis":"4 出现次数最多。"},
{"qtype":"选择题","difficulty":2,"stem":"数据 1,3,5,7,9 的中位数是（ ）","options":["A. 3","B. 5","C. 7","D. 4"],"answer":"B","analysis":"中间位置的数是 5。"},
{"qtype":"选择题","difficulty":2,"stem":"下列调查适合普查的是（ ）","options":["A. 了解一批灯泡使用寿命","B. 了解某班学生身高","C. 了解全国中学生视力","D. 了解河水质量"],"answer":"B","analysis":"班级人数少适合普查，其余适合抽样。"},
{"qtype":"选择题","difficulty":2,"stem":"抛一枚均匀硬币，正面朝上的概率是（ ）","options":["A. 1","B. 1/2","C. 1/3","D. 1/4"],"answer":"B","analysis":"两种等可能结果。"},
{"qtype":"选择题","difficulty":3,"stem":"数据 3,4,5,6,7 的方差是（ ）","options":["A. 1","B. 2","C. 3","D. 4"],"answer":"B","analysis":"均值 5，方差=((3-5)^2+...)/5=(4+1+0+1+4)/5=2。"},
{"qtype":"选择题","difficulty":3,"stem":"从 1,2,3,4,5 中随机抽一个数，抽到偶数的概率是（ ）","options":["A. 1/5","B. 2/5","C. 3/5","D. 4/5"],"answer":"B","analysis":"偶数 2、4 共 2 个，2/5。"},
{"qtype":"选择题","difficulty":3,"stem":"扇形统计图中，某部分占总体 30%，则该部分圆心角为（ ）","options":["A. 30°","B. 54°","C. 108°","D. 180°"],"answer":"C","analysis":"360°×30%=108°。"},
{"qtype":"填空题","difficulty":1,"stem":"数据 5,5,5 的平均数为________。","answer":"5","analysis":"所有数都是 5。"},
{"qtype":"填空题","difficulty":2,"stem":"数据 1,2,3,4,5 的极差为________。","answer":"4","analysis":"最大值减最小值。"},
{"qtype":"填空题","difficulty":2,"stem":"掷一枚均匀骰子，点数为偶数的概率是________。","answer":"1/2","analysis":"2、4、6 三个，3/6=1/2。"},
{"qtype":"填空题","difficulty":3,"stem":"一组数据方差为 0，则这组数据都________。","answer":"相等","analysis":"方差为 0 表示无波动。"},
{"qtype":"填空题","difficulty":3,"stem":"100 件产品中有 5 件次品，随机抽一件为正品的概率是________。","answer":"19/20","analysis":"正品 95 件，95/100=19/20。"},
{"qtype":"解答题","difficulty":2,"stem":"某班 10 名同学数学成绩为 80,85,90,75,90,95,85,90,80,100。求：(1)平均分；(2)众数；(3)中位数。","answer":"解：(1)总分=80+85+90+75+90+95+85+90+80+100=870，平均分=87。(2)90 出现 3 次最多，众数为 90。(3)从小到大排：75,80,80,85,85,90,90,90,95,100，中位数=(85+90)/2=87.5。","analysis":"平均数用总分除以个数；众数找出现最多；偶数个数据中位数取中间两数平均。"},
{"qtype":"解答题","difficulty":3,"stem":"甲袋有 2 红 1 白共 3 球，乙袋有 1 红 1 白共 2 球。从两袋各摸一球。求：(1)都是红球的概率；(2)至少有一个红球的概率。","answer":"解：(1)共 3×2=6 种等可能结果。都是红球：2×1=2 种，概率 2/6=1/3。(2)对立事件为都是白球：1×1=1 种，概率 1/6。故至少一红=1-1/6=5/6。","analysis":"用列表法或树状图列举所有等可能结果；至少有一个用对立事件更简便。"}
]
})
