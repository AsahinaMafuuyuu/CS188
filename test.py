import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

# 燃料电池堆
fc = d.add(elm.SourceV(label='燃料电池堆', toplabel='H₂ + O₂', botlabel='主电源'))
d.add(elm.Line().right())

# DC-DC 转换器
dcdc = d.add(elm.RBox(w=2.5, h=1.5, anchor='W', label='DC-DC转换器'))
d.add(elm.Line().right())

# 负载（电机）
motor = d.add(elm.Motor(label='电机'))
d.add(elm.Line().down())

# 负载（示意）
load = d.add(elm.Resistor(label='负载'))
d.add(elm.Line().left().length(3))
d.add(elm.Line().up().to(fc.start))

# 储能电池
d.add(elm.Line().down().at(dcdc.S))
battery = d.add(elm.BatteryCell(label='储能电池'))
d.add(elm.Line().left().length(2))
d.add(elm.Line().up().to(fc.start))

# 传感器
d.add(elm.Line().down().at(motor.S))
sensor = d.add(elm.Resistor(label='传感器'))
d.add(elm.Line().left().to(battery.S))

# 控制电路
d.add(elm.Line().down().at(dcdc.S))
control = d.add(elm.Box(w=2, h=1, label='控制电路'))
d.add(elm.Line().left().length(2))
d.add(elm.Line().up().to(fc.start))

# 冷却系统
d.add(elm.Line().down().at(control.S))
cooling = d.add(elm.Box(w=2, h=1, label='冷却系统'))
d.add(elm.Line().left().length(2))
d.add(elm.Line().up().to(battery.S))

# 绘制电路
d.draw()
