# Draw.io 图表模板库

本文件包含各种常见图表的完整 XML 模板，可直接复制修改使用。

## 目录
- [基础流程图](#基础流程图)
- [决策流程图](#决策流程图)
- [泳道图](#泳道图)
- [序列图](#序列图)
- [网络拓扑图](#网络拓扑图)
- [AWS 架构图](#aws-架构图)
- [数据流图](#数据流图)
- [组织结构图](#组织结构图)
- [状态机图](#状态机图)
- [ER 图](#er-图)

---

## 基础流程图

简单的线性流程：开始 → 步骤 → 结束

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Basic Flowchart">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <mxCell id="start" value="开始" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="200" y="40" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="step1" value="步骤 1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="190" y="130" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="step2" value="步骤 2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="190" y="230" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="step3" value="步骤 3" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="190" y="330" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="end" value="结束" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="200" y="430" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="start" target="step1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="step1" target="step2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="step2" target="step3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="step3" target="end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 决策流程图

包含条件判断的流程：输入 → 判断 → 分支处理 → 结束

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Decision Flowchart">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <mxCell id="start" value="开始" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="input" value="输入数据" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="220" y="130" width="140" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="decision" value="条件判断?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="230" y="220" width="120" height="80" as="geometry"/>
        </mxCell>

        <mxCell id="yes_action" value="是 - 处理 A" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="400" y="230" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="no_action" value="否 - 处理 B" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="60" y="230" width="120" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="merge" value="合并结果" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="220" y="350" width="140" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="end" value="结束" style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="240" y="440" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="start" target="input">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="input" target="decision">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e3" value="是" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="decision" target="yes_action">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e4" value="否" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="decision" target="no_action">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="yes_action" target="merge">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="460" y="375"/>
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="no_action" target="merge">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="120" y="375"/>
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="merge" target="end">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 泳道图

跨部门/角色的流程协作

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Swimlane Diagram">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Swimlanes -->
        <mxCell id="lane1" value="客户" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="600" height="120" as="geometry"/>
        </mxCell>

        <mxCell id="lane2" value="销售" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="40" y="160" width="600" height="120" as="geometry"/>
        </mxCell>

        <mxCell id="lane3" value="仓库" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="40" y="280" width="600" height="120" as="geometry"/>
        </mxCell>

        <!-- Customer actions -->
        <mxCell id="c1" value="下单" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane1">
          <mxGeometry x="60" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="c2" value="收货确认" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane1">
          <mxGeometry x="480" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <!-- Sales actions -->
        <mxCell id="s1" value="审核订单" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane2">
          <mxGeometry x="180" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="s2" value="通知发货" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane2">
          <mxGeometry x="300" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <!-- Warehouse actions -->
        <mxCell id="w1" value="拣货包装" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane3">
          <mxGeometry x="300" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="w2" value="发货" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="lane3">
          <mxGeometry x="420" y="35" width="80" height="50" as="geometry"/>
        </mxCell>

        <!-- Connections (use absolute coordinates) -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="c1" target="s1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="s1" target="s2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="s2" target="w1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="w1" target="w2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="w2" target="c2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 序列图

时序交互图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Sequence Diagram">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Participants -->
        <mxCell id="user" value="用户" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="100" height="400" as="geometry"/>
        </mxCell>

        <mxCell id="frontend" value="前端" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="240" y="40" width="100" height="400" as="geometry"/>
        </mxCell>

        <mxCell id="backend" value="后端 API" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="400" y="40" width="100" height="400" as="geometry"/>
        </mxCell>

        <mxCell id="db" value="数据库" style="shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="560" y="40" width="100" height="400" as="geometry"/>
        </mxCell>

        <!-- Messages -->
        <mxCell id="m1" value="1. 点击登录" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="130" y="120" as="sourcePoint"/>
            <mxPoint x="290" y="120" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="m2" value="2. POST /api/login" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="290" y="160" as="sourcePoint"/>
            <mxPoint x="450" y="160" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="m3" value="3. SELECT user" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="450" y="200" as="sourcePoint"/>
            <mxPoint x="610" y="200" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="m4" value="4. user data" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;dashed=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="610" y="240" as="sourcePoint"/>
            <mxPoint x="450" y="240" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="m5" value="5. JWT token" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;dashed=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="450" y="280" as="sourcePoint"/>
            <mxPoint x="290" y="280" as="targetPoint"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="m6" value="6. 登录成功" style="html=1;verticalAlign=bottom;endArrow=block;rounded=0;dashed=1;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="290" y="320" as="sourcePoint"/>
            <mxPoint x="130" y="320" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 网络拓扑图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Network Topology">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Internet -->
        <mxCell id="internet" value="Internet" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;" vertex="1" parent="1">
          <mxGeometry x="240" y="20" width="120" height="60" as="geometry"/>
        </mxCell>

        <!-- Firewall -->
        <mxCell id="firewall" value="防火墙" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="250" y="120" width="100" height="40" as="geometry"/>
        </mxCell>

        <!-- Router -->
        <mxCell id="router" value="路由器" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="250" y="200" width="100" height="40" as="geometry"/>
        </mxCell>

        <!-- Switch -->
        <mxCell id="switch" value="交换机" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="250" y="280" width="100" height="40" as="geometry"/>
        </mxCell>

        <!-- Servers -->
        <mxCell id="web1" value="Web Server 1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="60" y="370" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="web2" value="Web Server 2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="370" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="app" value="App Server" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="340" y="370" width="100" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="db" value="Database" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#e1d5e7;strokeColor=#9673a6;" vertex="1" parent="1">
          <mxGeometry x="480" y="360" width="80" height="70" as="geometry"/>
        </mxCell>

        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="internet" target="firewall">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c2" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="firewall" target="router">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c3" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="router" target="switch">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c4" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="switch" target="web1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c5" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="switch" target="web2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c6" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="switch" target="app">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c7" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="switch" target="db">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## AWS 架构图

三层 Web 应用架构

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="AWS Architecture">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Users -->
        <mxCell id="users" value="Users" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="180" width="40" height="80" as="geometry"/>
        </mxCell>

        <!-- CloudFront -->
        <mxCell id="cf" value="CloudFront" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="1">
          <mxGeometry x="140" y="180" width="60" height="60" as="geometry"/>
        </mxCell>

        <!-- ALB -->
        <mxCell id="alb" value="ALB" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elastic_load_balancing;" vertex="1" parent="1">
          <mxGeometry x="260" y="180" width="60" height="60" as="geometry"/>
        </mxCell>

        <!-- EC2 instances -->
        <mxCell id="ec2_1" value="EC2" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;" vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="60" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="ec2_2" value="EC2" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ec2;" vertex="1" parent="1">
          <mxGeometry x="380" y="240" width="60" height="60" as="geometry"/>
        </mxCell>

        <!-- RDS -->
        <mxCell id="rds" value="RDS" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;" vertex="1" parent="1">
          <mxGeometry x="520" y="180" width="60" height="60" as="geometry"/>
        </mxCell>

        <!-- S3 -->
        <mxCell id="s3" value="S3" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#7AA116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;" vertex="1" parent="1">
          <mxGeometry x="520" y="320" width="60" height="60" as="geometry"/>
        </mxCell>

        <!-- Connections -->
        <mxCell id="c1" style="endArrow=classic;html=1;" edge="1" parent="1" source="users" target="cf">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c2" style="endArrow=classic;html=1;" edge="1" parent="1" source="cf" target="alb">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c3" style="endArrow=classic;html=1;" edge="1" parent="1" source="alb" target="ec2_1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c4" style="endArrow=classic;html=1;" edge="1" parent="1" source="alb" target="ec2_2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c5" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="ec2_1" target="rds">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c6" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="ec2_2" target="rds">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c7" style="endArrow=classic;startArrow=classic;html=1;" edge="1" parent="1" source="ec2_2" target="s3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 数据流图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Data Flow Diagram">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- External Entity -->
        <mxCell id="customer" value="客户" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="160" width="80" height="60" as="geometry"/>
        </mxCell>

        <!-- Processes -->
        <mxCell id="p1" value="1.0&#xa;处理订单" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="200" y="150" width="100" height="80" as="geometry"/>
        </mxCell>

        <mxCell id="p2" value="2.0&#xa;验证库存" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="380" y="80" width="100" height="80" as="geometry"/>
        </mxCell>

        <mxCell id="p3" value="3.0&#xa;生成发票" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="380" y="220" width="100" height="80" as="geometry"/>
        </mxCell>

        <!-- Data Stores -->
        <mxCell id="ds1" value="D1 | 产品库" style="shape=partialRectangle;whiteSpace=wrap;html=1;left=1;right=0;top=0;bottom=0;fillColor=#d5e8d4;strokeColor=#82b366;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="540" y="100" width="120" height="40" as="geometry"/>
        </mxCell>

        <mxCell id="ds2" value="D2 | 订单库" style="shape=partialRectangle;whiteSpace=wrap;html=1;left=1;right=0;top=0;bottom=0;fillColor=#d5e8d4;strokeColor=#82b366;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="540" y="240" width="120" height="40" as="geometry"/>
        </mxCell>

        <!-- Data Flows -->
        <mxCell id="f1" value="订单请求" style="endArrow=classic;html=1;" edge="1" parent="1" source="customer" target="p1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="f2" value="订单信息" style="endArrow=classic;html=1;" edge="1" parent="1" source="p1" target="p2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="f3" value="确认订单" style="endArrow=classic;html=1;" edge="1" parent="1" source="p1" target="p3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="f4" value="查询" style="endArrow=classic;html=1;" edge="1" parent="1" source="p2" target="ds1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="f5" value="保存" style="endArrow=classic;html=1;" edge="1" parent="1" source="p3" target="ds2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="f6" value="发票" style="endArrow=classic;html=1;dashed=1;" edge="1" parent="1" source="p3" target="customer">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="430" y="360"/>
              <mxPoint x="80" y="360"/>
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 组织结构图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="Org Chart">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- CEO -->
        <mxCell id="ceo" value="CEO&#xa;张三" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="260" y="40" width="100" height="60" as="geometry"/>
        </mxCell>

        <!-- Directors -->
        <mxCell id="cto" value="CTO&#xa;李四" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="80" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="cfo" value="CFO&#xa;王五" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="260" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="coo" value="COO&#xa;赵六" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="440" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <!-- Managers -->
        <mxCell id="dev" value="研发经理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="20" y="280" width="90" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="qa" value="测试经理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="130" y="280" width="90" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="fin" value="财务经理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="265" y="280" width="90" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="hr" value="HR经理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="400" y="280" width="90" height="50" as="geometry"/>
        </mxCell>

        <mxCell id="ops" value="运营经理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="510" y="280" width="90" height="50" as="geometry"/>
        </mxCell>

        <!-- Connections -->
        <mxCell id="c1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="ceo" target="cto">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c2" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="ceo" target="cfo">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c3" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="ceo" target="coo">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c4" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="cto" target="dev">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c5" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="cto" target="qa">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c6" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="cfo" target="fin">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c7" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="coo" target="hr">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="c8" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;" edge="1" parent="1" source="coo" target="ops">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 状态机图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="State Machine">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Initial State -->
        <mxCell id="init" value="" style="ellipse;html=1;shape=startState;fillColor=#000000;strokeColor=#ff0000;" vertex="1" parent="1">
          <mxGeometry x="40" y="175" width="30" height="30" as="geometry"/>
        </mxCell>

        <!-- States -->
        <mxCell id="idle" value="空闲" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="120" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="processing" value="处理中" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="280" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="waiting" value="等待确认" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;" vertex="1" parent="1">
          <mxGeometry x="440" y="160" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="completed" value="已完成" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="360" y="280" width="100" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="error" value="错误" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;" vertex="1" parent="1">
          <mxGeometry x="200" y="280" width="100" height="60" as="geometry"/>
        </mxCell>

        <!-- Final State -->
        <mxCell id="final" value="" style="ellipse;html=1;shape=endState;fillColor=#000000;strokeColor=#ff0000;" vertex="1" parent="1">
          <mxGeometry x="550" y="295" width="30" height="30" as="geometry"/>
        </mxCell>

        <!-- Transitions -->
        <mxCell id="t1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="init" target="idle">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="t2" value="开始" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="idle" target="processing">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="t3" value="完成处理" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="processing" target="waiting">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="t4" value="确认" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="waiting" target="completed">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="t5" value="失败" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="processing" target="error">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <mxCell id="t6" value="重试" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;curved=1;" edge="1" parent="1" source="error" target="idle">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="170" y="310"/>
              <mxPoint x="170" y="130"/>
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="t7" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=classic;" edge="1" parent="1" source="completed" target="final">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## ER 图

实体关系图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile>
  <diagram name="ER Diagram">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- User Entity -->
        <mxCell id="user" value="User" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="60" y="120" width="140" height="130" as="geometry"/>
        </mxCell>
        <mxCell id="user_pk" value="+ id: INT (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontStyle=1;" vertex="1" parent="user">
          <mxGeometry y="26" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user_f1" value="  username: VARCHAR" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="user">
          <mxGeometry y="52" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user_f2" value="  email: VARCHAR" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="user">
          <mxGeometry y="78" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="user_f3" value="  created_at: DATETIME" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="user">
          <mxGeometry y="104" width="140" height="26" as="geometry"/>
        </mxCell>

        <!-- Order Entity -->
        <mxCell id="order" value="Order" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;fillColor=#d5e8d4;strokeColor=#82b366;" vertex="1" parent="1">
          <mxGeometry x="280" y="120" width="140" height="156" as="geometry"/>
        </mxCell>
        <mxCell id="order_pk" value="+ id: INT (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontStyle=1;" vertex="1" parent="order">
          <mxGeometry y="26" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order_fk" value="+ user_id: INT (FK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontStyle=2;" vertex="1" parent="order">
          <mxGeometry y="52" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order_f1" value="  total: DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="order">
          <mxGeometry y="78" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order_f2" value="  status: VARCHAR" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="order">
          <mxGeometry y="104" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="order_f3" value="  created_at: DATETIME" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="order">
          <mxGeometry y="130" width="140" height="26" as="geometry"/>
        </mxCell>

        <!-- Product Entity -->
        <mxCell id="product" value="Product" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
          <mxGeometry x="500" y="120" width="140" height="130" as="geometry"/>
        </mxCell>
        <mxCell id="product_pk" value="+ id: INT (PK)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontStyle=1;" vertex="1" parent="product">
          <mxGeometry y="26" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product_f1" value="  name: VARCHAR" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="product">
          <mxGeometry y="52" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product_f2" value="  price: DECIMAL" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="product">
          <mxGeometry y="78" width="140" height="26" as="geometry"/>
        </mxCell>
        <mxCell id="product_f3" value="  stock: INT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" vertex="1" parent="product">
          <mxGeometry y="104" width="140" height="26" as="geometry"/>
        </mxCell>

        <!-- Relationships -->
        <mxCell id="r1" value="1" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;endFill=0;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" edge="1" parent="1" source="user_pk" target="order_fk">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="r1_label" value="n" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="r1">
          <mxGeometry x="0.8" relative="1" as="geometry">
            <mxPoint x="-10" as="offset"/>
          </mxGeometry>
        </mxCell>

        <mxCell id="r2" value="n" style="edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;endFill=0;exitX=1;exitY=0.5;entryX=0;entryY=0.5;dashed=1;" edge="1" parent="1" source="order_f1" target="product_f2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="r2_label" value="m" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="r2">
          <mxGeometry x="0.8" relative="1" as="geometry">
            <mxPoint x="-10" as="offset"/>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## 使用说明

1. **复制模板**: 选择适合你需求的模板，复制整个 XML 代码
2. **修改内容**: 替换 `value` 属性中的文本为你的实际内容
3. **调整布局**: 修改 `mxGeometry` 中的 x, y, width, height 值
4. **添加元素**: 复制现有 mxCell 并修改 id（保持唯一）
5. **保存文件**: 保存为 `.drawio` 或 `.xml` 文件
6. **导入使用**: 在 draw.io 中打开文件

## 快速修改指南

**修改文本**: 更改 `value="..."` 中的内容

**修改颜色**: 更改 `fillColor=#hex` 和 `strokeColor=#hex`

**修改位置**: 更改 `x="..."` 和 `y="..."` 值

**修改大小**: 更改 `width="..."` 和 `height="..."` 值

**添加新节点**: 复制一个 mxCell，修改其 id 和 value

**添加新连接**: 添加 edge mxCell，设置 source 和 target 为节点 id
