# 從人數到混合 Capacity：建立 AI 原生營運模型

數十年來，組織主要透過人數來規劃 productive capacity。

Business 領導者預測 demand。Functions 將 demand 轉化為 workload。管理者提出 positions。Finance 批准部分 positions。Technology budget 與此過程並行，但主要作為一個獨立的類別：tools 和 infrastructure 支持 doing the work 的 people。

AI 正在挑戰這種分離。

隨著生成式 AI 從 copilots 發展成為能夠執行多步驟工作的 agents，組織越來越有兩種部分可 interchangeable 的 cognitive capacity 來源：people 和 machines。

這創建了一個新的 resource-allocation 問題：

**組織應該部署什麼樣的人類 judgment 與 AI capacity 來實現特定的 business outcome？**

對於許多公司而言，回答這個問題需要的不僅僅是採用新工具。它需要 redesigning the operating model。

## 傳統的 operating model 面臨極限

Traditional 組織通常對待三種資源的方式不同。

Human labor 透過 headcount 進行分配。

Technology 透過 IT budget 進行分配。

Capital 透過 investment 流程進行分配。

AI 越來越切穿所有三種。

考慮一個 software 組織，它收到了額外的 100 萬美元 budget。

Historically，可能的問題是：

**我們應該雇佣多少工程師？**

今天的 alternatives 可能包括：

- 雇佣四位額外的工程師；
- 增加現有 team 的 AI-agent capacity；
- 雇佣一位資深工程師並提供 substantial agent capacity；
- 重新設計 workflow 以減少所需的人員；
- 投資測試、架構或客戶驗證，因為編碼不再是 bottleneck。

budget 沒有改變。

改變的是公司將 budget 轉化為 productive capacity 的方式數。

因此，組織需要從 **headcount planning** 轨向 **hybrid-capacity planning**。

## 五個 shift 定義 AI 原生 operating model

AI 原生 operating model 需要在五個維度上進行改變。

### 1. 從 positions 到 outcomes

大多數 workforce planning 從 roles 開始。

一位管理者會請求六位工程師、三位分析師或 20 位客服人員。

AI 原生組織從更高的一層開始：

**What output 或 business outcome is constrained？**

如果一個 software team 需要增加 release velocity，管理者首先確定了什麼限制 releases。

如果編碼是 bottleneck，agents 可能會幫助。

如果架構是 bottleneck，更多 agents 可能會使問題更糟。

如果 product judgment 是 bottleneck，最高回報的投資可能是一位有經驗的人類。

resource 應該跟隨 constraint，而非 job categories。

### 2. 從 equal AI access 到 differentiated allocation

Early AI programs 通常給予員工相似的模型存取權。

這在 experiment 階段是合理的。

但不太可能保持經濟上的 optimal。

想象兩位員工，各自的年薪都是 25 萬美元。

第一位員工可以 Productively 使用 5 萬美元的 AI inference 和 agent capacity 來創造數十萬美元的增量價值。

第二位員工在消耗 5000 美元後，幾乎看不到額外的 Productivity。

給予他們相同的限制將相當於給每位管理者相同的 headcount，無論機會或能力如何。

AI capacity 應該越來越多地被視為 allocatable 的 economic resource。

### 3. 從 task automation 到 workflow redesign

Organizations 通常從自動化個別任務開始 AI 轉型。

這可以帶來快速的勝利，但也會有 ceiling。

如果 AI 讓某項活動快 5 倍而下一階段保持不變，bottleneck 就會 shift。

更快的代碼生成不一定會 proportionally 提升 product releases。

更快的分析不一定會改善 decisions。

更多的 sales content 不一定會帶來更多的 revenue。

目標不應該是 maximize local automation。

而應該是 redesign end-to-end workflow。

### 4. 從 span of control 到 span of agency

Traditionally，管理者根據他們能 effectively 領導的人數和複雜度來評估。

AI 引入了另一個維度：

**一個人可以 Productively 指揮多少 artificial capacity？**

一位能力出眾的工程師可能會監督幾個編碼 agents。

一位分析師可能會 orchestrate 研究、建模和 document-generation agents。

一位 product 領導者可能會指揮持續分析客戶 feedback、test 假設和生成 prototypes 的系統。

在 AI 原生組織中，最好的個別貢獻者可能 increasingly 像管理者，但沒有人類報告。

Organizations 需要 recognize 這種新的 leverage。

### 5. 從 productivity metrics 到 economic outcomes

AI 創造了 enormous 的可衡量 activity。

消耗的 tokens。

提交的 prompts。

生成的代碼。

創建的 documents。

完成的 agent runs。

這些是 operational metrics，不是 business outcomes。

一個 team 可以 double AI consumption 而幾乎不創造增量價值。

更相關的指標是：

**per dollar of combined human and AI capacity** 的 valuable output。

這可能是每個 engineering dollar 的 releases，每個 sales-capacity dollar 的 revenue，每個 service dollar 的 resolved cases，或每個 analytical dollar 的 decision quality。

## Human-AI production 函數

The difficulty is，organizations 還不知道 human labor 與 AI capacity 之間的 conversion rate。

也不太可能有一個 universal rate。

對於某些 work，AI 會主要 complement people。

對於其他 work，它會 substitute for some labor。

對於其他 work，additional AI 幾乎沒有影響，因為另一個 constraint 占主導。

因此，management 需要發現可能被稱為 organization 的 **human-AI production 函數**。

在簡化的 level：

**Output = f(human judgment, AI capacity, other constraints)**

目的不是建立一個數學上的完美模型。

而是創建一個有紀律的方式來學習，哪個 incremental dollar 創造最大的回報。

這暗示了三個 zones：

**Complementarity zone：** Additional AI materially 增加 existing employees 的 output。

**Substitution zone：** Additional AI 允許 organization 以 less human labor 實現相同 output。

**Saturation zone：** Additional AI 幾乎沒有額外價值，因為另一個 constraint 變得更為重要。

這些 zones 之間的邊界會隨著 model 的改進和 organization 對其使用的學習而 shift。

這讓系統變得 dynamic。

## 為什麼這對財務很重要

Implications 不僅限於 productivity。

Historically，rapid growth 和 operating leverage 往往代表著相互對立的目標。

A venture-backed company prioritized growth and tolerated rising headcount。

A private-equity-owned company emphasized margins, cost discipline, and EBITDA。

AI 創造了 possibility，讓 organizations 可以同時 pursue 兩者。

如果 revenue 可以成長得比 labor costs 更快，companies 可以 produce：

**VC 風格的成長與 PE 風格的 operating leverage。**

這改變了 scaling 的 economics。

A business that previously needed 10,000 people to reach a certain level of revenue might eventually require materially fewer。

Enterprise value 可能受到 significant 影響。

Organizational structure 可能 equally large。

## 四個實踐的轉變

Companies不需要在 overnight redesign 組織。

They can begin with four practical moves。

**Firstly，separate demand from staffing。**

要求 business units 描述所需的 outcomes 和 constraints，然後再申請 headcount。

**Secondly，create a flexible AI-capacity pool。**

Allow leaders 根據 measurable opportunities 請求 incremental agent 和 inference capacity，而非分發固定的 allowances。

**Thirdly，measure marginal returns。**

Track 當 teams 收到更多 human 或 AI capacity 時會發生什麼。Identify 哪裡 productivity 上升，哪裡 substitution 發生，哪裡 bottleneck 會移動。

**Fourthly，redesign incentives。**

Managers 不應該僅因為建立更大的組織而受到獎勵。Productively orchestrate large amounts of AI capacity 的個別貢獻者可能創造比擁有大團隊的傳統管理者更多的價值。

## Headcount 之後的組織

Headcount 將不會消失作為 management metric。

Human beings 仍然負責 judgment、accountability、relationships、leadership，和許多 AI 無法 reliably 複製的 expertise。

但是，headcount 將越來越成為 incomplete 的 organizational capability 描述。

50 人的兩個 team 可能有 radically 不同的 productive capacity，這取決於他們如何 effectively 部署 AI。

一個擁有 1,000 名員工的公司可能 eventually 超越一個擁有 5,000 名員工的競爭對手，不僅是因為員工更努力工作，而是因為每位員工控制的 artificial capacity 更多。

Defining management question 因此改變。

舊的問題是：

**我們需要多少人？**

新的問題是：

**我們需要多少人類 judgment 與 artificial capacity 來 deliver outcome？**

Companies that learn to answer that question systematically will not merely use AI more effectively。

They will operate differently。
