# 马尔可夫模型
## 1 马尔可夫链
如果我们将Wi定义为代表第i天天气的随机变量，那么天气示例的马尔可夫模型将是这样的：
![alt text](image-123.png)
由于马尔可夫链模型中：
![alt text](image-124.png)
因此，
![alt text](image-125.png)
也可以简化为：
![alt text](image-126.png)
这样，我们得到了一个通式：
![alt text](image-127.png)
因此在马尔可夫链中我们仅需要存储P(W0)和P（W<sub>i+1</sub>|W<sub>i</sub>）即可，即：
![alt text](image-130.png)
## 2 迷你的前向算法
比如我想要知道第i+1天的天气，那么可以用：
![alt text](image-128.png)
同时，我们可以将该式子从第i天的条件分布开始计算：
![alt text](image-129.png)
**为了计算时间步长i+1的天气分布，我们查看时间步长i由P（W<sub>i</sub>）给出的概率分布，并使用我们的过渡模型P（W<sub>i+1</sub>|W<sub>i</sub>）将该模型“推进”到时间步长。**
## 3 平稳概率分布（也称收敛概率分布）
![alt text](image-131.png)
上述式子也是我们达到收敛时的条件，通过马尔可夫链进行变形，可得：
![alt text](image-132.png)
对于我们天气的例子而言：
![alt text](image-133.png)
其中还有一个条件（**同一变量的所有可能发生的事件的概率和为1**）为：
![alt text](image-134.png)
解得：
![alt text](image-135.png)
因此，稳定概率分布为：
![alt text](image-136.png)
## 4 隐马尔可夫模型
它允许我们在每个时间步观察一些**证据**，这些证据可能会影响每个状态下的**分布**。
与普通的马尔可夫模型不同，我们现在有两种不同类型的节点。为了进行区分，**我们将每个Wi称为状态变量(state varible)，将每个天气预报Fi称为证据变量(evidence varible)**。
![alt text](image-137.png)
并且有以下关系（可以参考之前的Bayes Network中的三种基本独立模型）：
![alt text](image-138.png)
在隐马尔可夫模型中，我们是假设**过度模型（P（W<sub>i+1</sub>|W<sub>i</sub>））** 是平稳的。并且**传感模型（P（F<sub>i</sub>|W<sub>i</sub>））** 也是平稳的。
定义 **信念分布（belief distribution）** 为：
![alt text](image-139.png)
同时定义：
![alt text](image-140.png)
定义**e<sub>i</sub>为在时间步长为i时观测到的证据变量**，时间步长1≤i≤t的聚合证据重新表示为以下形式：
![alt text](image-141.png)
在这个符号下：
![alt text](image-142.png)
可以写作：
![alt text](image-143.png)
对于上述式子，我们可以进行一定程度的延伸：
![alt text](image-144.png)
上式可以表示为：
![alt text](image-145.png)
注意到：
![alt text](image-146.png)
并且：
![alt text](image-147.png)
因此最终可以化简为：
![alt text](image-148.png)
对于B(W<SUB>i+1</SUB>)，有：
![alt text](image-149.png)
变形后可得：
![alt text](image-150.png)
因此，**前向算法为：**
![alt text](image-151.png)
### 4.1 summary
公式1：
![alt text](image-148.png)
公式2：
![alt text](image-150.png)
这两个公式分别对应了：
**时间推移更新对应于从B（Wi）确定B'（Wi+1）和观测更新对应于从B’（Wi+1）确定B（Wi+1）。**
对此，考虑以下**初等模型、过渡模型和传感模型**：
![alt text](image-152.png)
为了计算B(W1),我们需要先计算B'(W1),则：
![alt text](image-153.png)
![alt text](image-154.png)
接下来，我们假设第一天的天气预报很好（即F1 =好），并执行观测更新以获得B(W1)：
![alt text](image-155.png)
![alt text](image-156.png)
因此，我们最终的表为（**表中的B'(W1)应该为B(W1)**）：
![alt text](image-157.png)
具体思路总结为：
![alt text](image-169.png)
## 5 Viterbi算法
Q:给定到目前为止观察到的证据变量，系统遵循的最可能的隐藏状态序列是什么？
即求解：argmax<sub>x<sub>1:N</sub></sub>P(x<sub>1:N</sub>|e<sub>1:N</sub>) = argmax<sub>x<sub>1:N</sub></sub>P（x<sub>1:N</sub>, e<sub>1:N</sub>）
在Viterbi算法中，我们希望求得：
![alt text](image-160.png)
举个例子，在以下给定的状态模型中：
![alt text](image-161.png)
在这个有两种可能的隐藏状态（太阳或雨）的HMM中，我们想要计算从X1到XN的最高概率路径（每个时间步长分配一个状态）。
**从X<sub>t-1</sub>到X<sub>t</sub>的边权值等于P(X<SUB>t</SUB>|X<SUB>t-1</SUB>)P(E<SUB>t</SUB>|X<SUB>t</SUB>)**
权重公式中的第一项表示特定转变的可能性，第二项表示观察到的证据与结果状态的匹配程度。
对于概率论密度，有：
![alt text](image-158.png)
根据前向算法，可得：
![alt text](image-159.png)